# -*- coding: utf-8 -*-
"""
@author: Vinay Krishna
"""


from kafka import KafkaProducer
from json import dumps

'''
Creating a producer object my_producer with the bootstrap server onto which data needs to 
be published. 
Value serializer is used to convert user supplied value into utf-8 byte format.
Below, we first converted a dictionary data into Json structure using dumps function as per the
requirement.
'''
my_producer = KafkaProducer(  
    bootstrap_servers = ['localhost:808'],  
    value_serializer = lambda x:dumps(x).encode('utf-8')
    )  
 
for i in range(100):
    my_data = {"company": " abc","source":"A"}
    #Topic name test1 should be used if you want to subscribe from this server or the message published through this code.
    my_producer.send('test1', value = my_data)  
