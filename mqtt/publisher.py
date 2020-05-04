# Thanks to: https://techtutorialsx.com/2017/04/14/python-publishing-messages-to-mqtt-topic/
"""Publish a Topic to MQTT Broker"""

import paho.mqtt.client as mqttClient
import time
 
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected to broker')
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print('Connection failed')
 
Connected = False   #global variable for the state of the connection

# After you successfully the publisher and subscribe code, 
# try to create your own MQTT broker by create an account at cloudmqtt.com
broker_address= 'mqtt.eclipse.org'
port = 1883 # do not type string, but change to integer
#username = 'your username'
#password = 'your password'
 
client = mqttClient.Client()               #create new instance
#client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(2)
 
try:
    while True: 
        #value = input('Enter the message:')
        client.publish('python/CA171/mqtt', '#170010108 #CA171')
        client.publish('python/CA171/socket', '#Wiryantara #CA171')
 
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()