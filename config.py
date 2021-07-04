import os
from dotenv import load_dotenv

def prepareConfiguration():
  load_dotenv()
  config = {}

  config['SOCKET_SERVER'] = os.environ.get('SOCKET_SERVER')
  config['MLSERVER_URL'] = os.environ.get('MLSERVER_URL')
  config['MONGODB_CONNECTION_STRING'] = os.environ.get('MONGODB_CONNECTION_STRING')
  config['MONGODB_DATABASE'] = os.environ.get('MONGODB_DATABASE')
  config['KAFKA_CONSUMER_TOPIC'] = os.environ.get('KAFKA_CONSUMER_TOPIC')
  config['KAFKA_PORT'] = os.environ.get('KAFKA_PORT')
  config['KAFKA_HOST'] = os.environ.get('KAFKA_HOST')
  config['KAFKA_CLIENT_ID'] = os.environ.get('KAFKA_CLIENT_ID')
  config['KAFKA_GROUP_ID'] = os.environ.get('KAFKA_GROUP_ID')
  config['SENSOR_SERIAL'] = os.environ.get('SENSOR_SERIAL')

  return config