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
from config import prepareConfiguration

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
logging.info('Starting seer')
config = prepareConfiguration();

sio = socketio.Client()
sio.connect("http://localhost:4444/socket.io/?sensor_serial=b969e73e-6880-4a78-ad55-13fc32694948", namespaces='/sensor')

@sio.event(namespace='/sensor')
def connect():
    logging.info('connection to server established')

@sio.event(namespace='/sensor')
def disconnect():
    logging.info('disconnected from server')

mongoClient = MongoClient("mongodb://ta:ta@192.168.100.29:27018/?authSource=admin&readPreference=primary&ssl=false")
logging.info('Connected to mongodb server')

db = mongoClient["iot_malware_detection"]

consumer = KafkaConsumer(
    "sensor_lab_1",
    bootstrap_servers=["{}:{}".format("192.168.100.29", "19092")],
    group_id="RTD",
    value_deserializer=lambda v: loads(v.decode('utf-8')),
    key_deserializer=lambda v: loads(v.decode('utf-8'))
)

# Get information about sensor tied with this processor
api_call = requests.get("{}/api/v1/sensor/{}".format("http://mlserver.lokal", "b969e73e-6880-4a78-ad55-13fc32694948"))
response = loads(api_call.content)

features = str(response['data']['model']['features']).replace('\'', '').split(', ')
clf = load(urlopen("{}/api/v1/sensor/{}/model".format("http://mlserver.lokal", "b969e73e-6880-4a78-ad55-13fc32694948")))

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
