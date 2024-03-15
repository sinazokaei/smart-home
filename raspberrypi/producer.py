#!/usr/bin/env python
import pika
import time

# If you want to have a more secure SSL authentication, use ExternalCredentials object instead
credentials = pika.PlainCredentials(username= 'admin', password='adminadmin', erase_on_connect=True)
parameters = pika.ConnectionParameters(host='sub.example.com', port=5672, virtual_host='/home', credentials=credentials)

# We are using BlockingConnection adapter to start a session. It uses a procedural approach to using Pika and has most of the asynchronous expectations removed
connection = pika.BlockingConnection(parameters)
# A channel provides a wrapper for interacting with RabbitMQ
channel = connection.channel()

# Check for a queue and create it, if necessary
channel.queue_declare(queue='queue')
# For the sake of simplicity, we are not declaring an exchange, so the subsequent publish call will be sent to a Default exchange that is predeclared by the broker
i=1
while(True):
    i+=1
    channel.basic_publish(exchange='', routing_key='queue', body= '{"temp":"31" , "hum":"52" , "o2":"12" , "co2":"5"}')
    print(" [x] Sent data")
    time.sleep(5)

# Safely disconnect from RabbitMQ
connection.close() 
