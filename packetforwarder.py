#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import sys
import os
import json

local_broker = "localhost"
local_port = 1883
db_broker = "20.204.142.77"
db_port = 1883
db_username = "db2user"
db_password = "db2user"
ltts_client_id = "Flamencotech_device1"
ltts_broker = "MSFT-POC-Flamencotech.azure-devices.net"
ltts_port = 8883  # to establish a connection.
ltts_topic = 'devices/Flamencotech_device1/messages/events/$.ct=application%2Fjson&$.ce=utf-8'  # enter the MQTT topic on which to subscribe.
ltts_username = "MSFT-POC-Flamencotech.azure-devices.net/Flamencotech_device1/api-version=2021-04-12"
ltts_password = "SharedAccessSignature sr=MSFT-POC-Flamencotech.azure-devices.net%2Fdevices%2FFlamencotech_device1&sig=VhMhLeg33B4SRTtHsG930zSQXakDucS7kn10vgyU1LY%3D&se=1660548535"
path_to_cert_file = "./root.cer"


def db_on_connect(client: mqtt.Client, userdata, flags, rc):
    print(f'Connected to DB with result code: {rc}')


def ltts_on_connect(client: mqtt.Client, userdata, flags, rc):
    print(f'Connected to LTTS with result code: {rc}')


def local_on_connect(client: mqtt.Client, userdata, flags, rc:int):
    print(f'Connected to local with result code: {rc}')
    # client.subscribe([('/ltts/dwpc/space_occupancy', 0), ('/ltts/iba/data', 0), ('/ltts/desk_occupancy', 0)])
    client.subscribe('#', 1)


def db_on_disconnect(client: mqtt.Client, userdata, rc):
    print(f"Disconnected from DB with result code: {rc}")


def local_on_disconnect(client: mqtt.Client, userdata, rc):
    print(f"Disconnected from local with result code: {rc}")


def ltts_on_disconnect(client: mqtt.Client, userdata, rc):
    print(f"Disconnected from LTTS with result code: {rc}")


def ltts_on_publish(client: mqtt.Client, userdata, mid):
    print("Published to LTTS")
    
    
def db_on_publish(client: mqtt.Client, userdata, mid):
    print("Published to DB")


def local_on_subscribe(client: mqtt.Client, userdata, mid, granted_qos):
    print("Subscribed to Local broker")


def local_on_message(client: mqtt.Client, userdata, msg):
    if msg.topic in ['/ltts/dwpc/space_occupancy', '/ltts/iba/data', '/ltts/desk_occupancy']:
        ltts_client.publish(ltts_topic, msg.payload, 1)
    # print(json.loads(msg.payload))
    db_client.publish(msg.topic, msg.payload, 0)
    print(msg.topic)


local_client = mqtt.Client()
db_client = mqtt.Client()
ltts_client = mqtt.Client(client_id=ltts_client_id, protocol=mqtt.MQTTv311)
db_client.on_connect = db_on_connect
db_client.on_disconnect = db_on_disconnect
db_client.on_publish = db_on_publish
db_client.username_pw_set(username=db_username, password=db_password)
local_client.on_connect = local_on_connect
local_client.on_disconnect = local_on_disconnect
local_client.on_message = local_on_message
local_client.on_subscribe = local_on_subscribe
ltts_client.on_connect = ltts_on_connect
ltts_client.on_disconnect = ltts_on_disconnect
ltts_client.on_publish = ltts_on_publish
ltts_client.username_pw_set(username=ltts_username,
                   password=ltts_password)
ltts_client.tls_set(path_to_cert_file)
ltts_client.tls_insecure_set(False)
try:
    local_client.connect(local_broker, local_port, 60)
    db_client.connect(db_broker, db_port, 60)
    ltts_client.connect(ltts_broker, ltts_port, 60)
    db_client.loop_start()
    ltts_client.loop_start()
    local_client.loop_forever()
except KeyboardInterrupt:
    ltts_client.disconnect()
    local_client.disconnect()
    print("Stopped")
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
