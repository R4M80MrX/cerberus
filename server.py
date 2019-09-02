# import paho.mqtt.client as mqtt
from paho.mqtt.publish import mqtt
import json
mqttc = mqtt.client()
mqttc.connect('127.0.0.1', port=1883)
msg = {
    'pin': 17,
    'value': 10
}
msg = json.dumps(msg)

print(mqttc.publish('test', payload=msg))
mqttc.loop(2)
