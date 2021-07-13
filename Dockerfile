FROM python:3.8-slim-buster

# PREPARE DEPENDENCIES AND APP
WORKDIR /app
RUN pip install wheel pandas python-socketio[client] \
    python-dotenv joblib kafka-python pymongo requests
COPY . .

# LAUNCH
CMD [ "python", "/app/main.py" ]