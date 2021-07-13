import os
import requests
from dotenv import load_dotenv
from json import loads

def prepareConfiguration():
  load_dotenv()
  config = {}
  config['SOCKET_SERVER'] = "http://localhost:4444"
  config['MLSERVER_URL'] = "http://mlserver.lokal"
  config['MONGODB_CONNECTION_STRING'] = "mongodb://ta:ta@192.168.100.29:27018/?authSource=admin&readPreference=primary&ssl=false"
  config['MONGODB_DATABASE'] = os.environ.get('MONGODB_DATABASE')
  config['MONGODB_COLLECTION'] = os.environ.get('MONGODB_COLLECTION')
  config['KAFKA_CONSUMER_TOPIC'] = os.environ.get('KAFKA_CONSUMER_TOPIC')
  config['KAFKA_PORT'] = os.environ.get('KAFKA_PORT')
  config['KAFKA_HOST'] = os.environ.get('KAFKA_HOST')
  config['KAFKA_GROUP_ID'] = os.environ.get('KAFKA_GROUP_ID')
  config['SENSOR_SERIAL'] = os.environ.get('SENSOR_SERIAL')

  return config

def getOnlineConfiguration(config):
  call = requests.get("{}/api/v1/sensor/{}/config".format(config['MLSERVER_URL'], config['SENSOR_SERIAL']))
  response = loads(call.content)
  rconf = loads(response['data']['config'])
  config['KAFKA_HOST'] = rconf['KAFKA_HOST']
  config['KAFKA_PORT'] = rconf['KAFKA_PORT']
  config['KAFKA_GROUP_ID'] = rconf['KAFKA_GROUP']
  config['KAFKA_CONSUMER_TOPIC'] = rconf['KAFKA_TOPIC']
  config['MONGODB_DATABASE'] = rconf['MONGODB_DATABASE']
  config['MONGODB_COLLECTION'] = rconf['MONGODB_COLLECTION']
  return config