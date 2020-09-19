#!/usr/bin/python
# -*- coding: utf-8 -*-
# Import package
import paho.mqtt.client as mqtt
#add for output
import sys

state = sys.argv[1]

broker_address="172.16.116.150"
#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker
client.publish("raspi/pin24",state)#publish

