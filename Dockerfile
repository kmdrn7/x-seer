FROM python:3.8-slim-buster

# PREPARE DEPENDENCIES AND APP
WORKDIR /app
RUN pip install wheel pandas python-socketio[client] \
    python-dotenv joblib kafka-python pymongo requests
COPY . .

# SET ENVIRONMENT
ENV SOCKET_SERVER http://localhost:4444
ENV MLSERVER_URL http://localhost:8000
ENV MONGODB_CONNECTION_STRING mongodb://ta:ta@192.168.100.29:27018/?authSource=admin&readPreference=primary&ssl=false
ENV MONGODB_DATABASE iot_malware_detection
ENV KAFKA_CONSUMER_TOPIC iot_gateway_netflow
ENV KAFKA_HOST 192.168.100.29
ENV KAFKA_PORT 19092
ENV KAFKA_CLIENT_ID RTD-1
ENV KAFKA_GROUP_ID RTD
ENV SENSOR_SERIAL 95fe60ed-9754-4579-be92-943da7bd0fda

# LAUNCH
CMD [ "python", "/app/main.py" ]