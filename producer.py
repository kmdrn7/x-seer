import json
import pandas as pd
from kafka import KafkaProducer
from sklearn.preprocessing import MinMaxScaler

producer = KafkaProducer(
    bootstrap_servers="192.168.100.29:29092",
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=lambda v: json.dumps(v).encode('utf-8')
)

datates = pd.read_csv("/media/kmdr7/Seagate/TA/DATASETS/UnseenDatasetEncoded.csv")
X = datates.drop(columns=["Label"])
y = datates["Label"]
scaler = MinMaxScaler()
X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
features = ['Protocol', 'Fwd Packet Length Max', 'Bwd Packet Length Max',
'Bwd Packet Length Mean', 'Flow Packets/s', 'Fwd Packets/s',
'Packet Length Max', 'Packet Length Mean', 'Packet Length Std',
'FIN Flag Count', 'SYN Flag Count', 'Down/Up Ratio',
'Bwd Segment Size Avg', 'Subflow Fwd Packets', 'FWD Init Win Bytes',
'Fwd Seg Size Min', 'Idle Mean', 'Idle Max', 'Idle Min']
X = X[features]

data = X.iloc[:1000].to_numpy()

for dd in data:
  producer.send(topic="pizza_order", value={
    "data": dd.tolist()
  })
producer.flush()
