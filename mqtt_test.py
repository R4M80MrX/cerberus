# -*- coding: utf-8 -*-

from core.MyLog.log import LOGGER
import time
import paho.mqtt.client as mqtt
import json


MQTTHOST = "47.94.140.36"
MQTTPORT = 1883
mqttClient = mqtt.Client()


def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))
    client.subscribe('test')


def on_message(client, userdata, msg):
    print(f'msg.topic ${msg.payload}')
    print(json.loads(msg.payload))


if __name__ == '__main__':
    client = mqttClient
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(MQTTHOST, MQTTPORT)
        client.loop_forever()
    except KeyboardInterrupt:
        client.disconnect()
