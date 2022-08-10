#!/usr/bin/python3
from paho.mqtt import client as mqtt
import ssl

path_to_root_cert = "./root.cer"
device_id = "POC_device1"
sas_token = "SharedAccessSignature sr=MSFTEdgeHub.azure-devices.net%2Fdevices%2FPOC_device1&sig=9loWHOajIYuR6i8oBpkKTZ1adp5ScM7GOykJYVKrr%2BM%3D&se=1656017690"
iot_hub_name = "MSFTEdgeHub"
def on_connect(client, userdata, flags, rc):
    print("Device connected with result code: " + str(rc))


def on_disconnect(client, userdata, rc):
    print("Device disconnected with result code: " + str(rc))


def on_publish(client, userdata, mid):
    print("Device sent message")


client = mqtt.Client(client_id=device_id, protocol=mqtt.MQTTv311)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
'''
MQTT HOST name: "MSFTEdgeHub.azure-devices.net"
MQTT HOST PORT:  8883
MQTT Username: "MSFTEdgeHub.azure-devices.net/POC_device1/api-version=2021-04-12"
MQTT Password: "SharedAccessSignature sr=MSFTEdgeHub.azure-devices.net%2Fdevices%2FPOC_device1&sig=9loWHOajIYuR6i8oBpkKTZ1adp5ScM7GOykJYVKrr%2BM%3D&se=1656017690"
MQTT certificate: "root.cer"
MQTT topic to publish message: "devices/POC_device1/messages/events/"
'''
client.username_pw_set(username="MSFTEdgeHub.azure-devices.net/POC_device1/api-version=2021-04-12",
                       password="SharedAccessSignature sr=MSFTEdgeHub.azure-devices.net%2Fdevices%2FPOC_device1&sig=9loWHOajIYuR6i8oBpkKTZ1adp5ScM7GOykJYVKrr%2BM%3D&se=1656017690")
# client.username_pw_set(username=iot_hub_name+".azure-devices.net/" +
#                      device_id + "/?api-version=2021-04-12", password=sas_token)

client.tls_set(ca_certs=path_to_root_cert, certfile=None, keyfile=None,
               cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
client.tls_insecure_set(False)
client.connect("MSFTEdgeHub.azure-devices.net", port=8883)
# client.connect(iot_hub_name+".azure-devices.net", port=8883)
message_mm = '{ "Time":1650306628585, // Timestamp – Current Millis "MAC":"0011220011223344",  "DeviceType":21,"Incount":2,  "Outcount":5  }'
client.publish("devices/POC_device1/messages/events/", message_mm, qos=1)
# client.publish("devices/" + device_id + "/messages/events/", '{"id":123}', qos=1)
client.loop_forever()

'''
from paho.mqtt import client as mqtt
import ssl
import json
import sys
import getopt
import time
import os
def on_connect(client, userdata, flags, rc):
  print ("Device connected with result code: " + str(rc))
def on_disconnect(client, userdata, rc):
  print ("Device disconnected with result code: " + str(rc))
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))
def main():
  try:
      client = mqtt.Client(client_id="POC_device1", protocol=mqtt.MQTTv311)
      client.on_connect = on_connect
      client.on_message=on_message
      print("connected")
      client.on_disconnect = on_disconnect
      print("connected 1")
      client.username_pw_set(username= "MSFTEdgeHub.azure-devices.net/POC_device1/api-version=2021-04-12" , password="SharedAccessSignature sr=MSFTEdgeHub.azure-devices.net%2Fdevices%2FPOC_device1&sig=9loWHOajIYuR6i8oBpkKTZ1adp5ScM7GOykJYVKrr%2BM%3D&se=1656017690")
      client.connect("MSFTEdgeHub.azure-devices.net", port=8883)
      client.loop_start()
      client.subscribe("*")
      client.publish("test","test_topic")
      while True:
        client.publish("test","test_topic")
        time.sleep(2)
  except Exception as e:
      print ("An error has occured: %s" % e)
  client.disconnect()
if __name__ == "__main__":
  main()
'''
