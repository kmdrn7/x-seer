import pandas as pd
import socketio
import requests
from joblib import load
from urllib.request import urlopen
from json import loads
from kafka import KafkaConsumer
from pymongo import MongoClient
from formatter import formatRawData
from config import prepareConfiguration

config = prepareConfiguration();

sio = socketio.Client()
sio.connect(config['SOCKET_SERVER'], namespaces='/sensor')

@sio.event(namespace='/sensor')
def connect():
    print('connection to server established')

@sio.event(namespace='/sensor')
def disconnect():
    print('disconnected from server')

mongoClient = MongoClient(config['MONGODB_CONNECTION_STRING'])
db = mongoClient[config['MONGODB_DATABASE']]

consumer = KafkaConsumer(
    config['KAFKA_CONSUMER_TOPIC'],
    bootstrap_servers=["{}:{}".format(config['KAFKA_HOST'], config['KAFKA_PORT'])],
    client_id=config['KAFKA_CLIENT_ID'],
    group_id=config['KAFKA_GROUP_ID'],
    value_deserializer=lambda v: loads(v.decode('utf-8')),
    key_deserializer=lambda v: loads(v.decode('utf-8'))
)

# Get information about sensor tied with this processor
api_call = requests.get("{}/api/v1/sensor/{}".format(config['MLSERVER_URL'], config['SENSOR_SERIAL']))
response = loads(api_call.content)
features = str(response['data']['model']['features']).replace('\'', '').split(', ')
clf = load(urlopen(response['data']['model']['joblib']))

for message in consumer:
    data = pd.DataFrame([formatRawData(message.value)])[features].to_numpy()[0]
    data = data.tolist()
    res = clf.predict([data])
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
    db.realtime_result.insert_one(payload)
    print(payload)
