import pandas as pd
import socketio
from joblib import load
from json import loads
from kafka import KafkaConsumer
from pymongo import MongoClient
from formatter import formatRawData

sio = socketio.Client()
sio.connect("http://0.0.0.0:4444", namespaces='/sensor')

@sio.event(namespace='/sensor')
def connect():
    print('connection to server established')

@sio.event(namespace='/sensor')
def disconnect():
    print('disconnected from server')

mongoClient = MongoClient("mongodb://ta:ta@192.168.100.29:27018/?authSource=admin&readPreference=primary&ssl=false")
db = mongoClient.iot_malware_detection

consumer = KafkaConsumer(
    "iot_gateway_netflow",
    bootstrap_servers=["192.168.100.29:19092"],
    client_id="PZ-001",
    group_id="PZ",
    value_deserializer=lambda v: loads(v.decode('utf-8')),
    key_deserializer=lambda v: loads(v.decode('utf-8'))
)

features = ['Protocol', 'Flow Duration', 'Fwd Packet Length Max',
    'Fwd Packet Length Mean', 'Bwd Packet Length Mean', 'Fwd IAT Total',
    'Bwd IAT Total', 'Packet Length Max', 'Packet Length Mean',
    'Packet Length Std', 'FIN Flag Count', 'SYN Flag Count',
    'Down/Up Ratio', 'Average Packet Size', 'Fwd Segment Size Avg',
    'Bwd Segment Size Avg', 'FWD Init Win Bytes', 'Fwd Seg Size Min',
    'Idle Mean', 'Idle Max', 'Idle Min']

clf = load("/media/kmdr7/Seagate/TA/MODELS/BACKUP/LogisticRegression.joblib")

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
