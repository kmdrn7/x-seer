import pandas as pd
import socketio
import requests
import logging
from joblib import load
from urllib.request import urlopen
from json import loads
from kafka import KafkaConsumer
from pymongo import MongoClient
from formatter import formatRawData
from config import prepareConfiguration, getOnlineConfiguration

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
logging.info('Starting seer')
config = prepareConfiguration()
config = getOnlineConfiguration(config)

sio = socketio.Client()
sio.connect("{}/socket.io/?sensor_serial={}".format(config['SOCKET_SERVER'], config['SENSOR_SERIAL']), namespaces='/sensor')

@sio.event(namespace='/sensor')
def connect():
    logging.info('connection to server established')

@sio.event(namespace='/sensor')
def disconnect():
    logging.info('disconnected from server')

mongoClient = MongoClient(config['MONGODB_CONNECTION_STRING'])
logging.info('Connected to mongodb server')

db = mongoClient[config['MONGODB_DATABASE']]

consumer = KafkaConsumer(
    config['KAFKA_CONSUMER_TOPIC'],
    bootstrap_servers=["{}:{}".format(config['KAFKA_HOST'], config['KAFKA_PORT'])],
    group_id=config['KAFKA_GROUP_ID'],
    value_deserializer=lambda v: loads(v.decode('utf-8')),
    key_deserializer=lambda v: loads(v.decode('utf-8'))
)

# Get information about sensor tied with this processor
api_call = requests.get("{}/api/v1/sensor/{}".format(config['MLSERVER_URL'], config['SENSOR_SERIAL']))
response = loads(api_call.content)

features = str(response['data']['model']['features']).replace('\'', '').split(', ')
clf = load(urlopen("{}/api/v1/sensor/{}/model".format(config['MLSERVER_URL'], config['SENSOR_SERIAL'])))

for message in consumer:
    data = pd.DataFrame([formatRawData(message.value)])[features].to_numpy()[0]
    if "XG" in response["data"]["model"]["name"]:
        x = pd.DataFrame([data.tolist()])
    else:
        x = [data.tolist()]
    res = clf.predict(x)
    payload = {
        'sensor_serial': message.value['metadata']['serial'],
        'src_ip': message.value["src_ip"],
        'dst_ip': message.value["dst_ip"],
        'src_port': int(message.value["src_port"]),
        'dst_port': int(message.value["dst_port"]),
        'protocol': int(message.value["protocol"]),
        'timestamp': message.value["timestamp"],
        'prediction': int(res[0]),
    }
    sio.emit('sink', payload, namespace='/sensor')
    db[config['MONGODB_COLLECTION']].insert_one(payload)
