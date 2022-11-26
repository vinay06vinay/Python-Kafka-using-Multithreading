from json import loads  
from kafka import KafkaConsumer 
from concurrent.futures import ThreadPoolExecutor
import requests
import threading
import time
from requests.auth import HTTPBasicAuth

"""
Messages are consumed from test1 topic and stored in my_consumer object. This my_consumer is passed to a multiple_requests function 
where a multi thread is run so as to consume large number of messages simultaneously and used. The thread pool executor has 50 multiple threads
which can process 100000 messages in around 5 minutes.
The 50 threads call request function simultaneously and send messages in json format to desired site or can be stored in database or excel file.

The use of multiple threads to process large amount of data simultaneously is what differs this python consumer from other consumer.
"""


def request(my_consumer):
    message = my_consumer.value
    try :
       r=requests.post(url='https://xyz.com',json=message,auth=HTTPBasicAuth('username','password'))
    except requests.exceptions.HTTPError :
       print("Error while connecting to the url")
    except requests.exceptions.ConnectionError :
       print("Error while establishing connection with the server")
    except requests.exceptions.Timeout :
       print("Error due to message could not be sent in time")
    except requests.exceptions.RequestException :
       print("Error while making a post request")
def multiple_requests(my_consumer):
    with ThreadPoolExecutor(max_workers=50) as executor:
        a= {executor.map(request, my_consumer)}
if __name__ == "__main__":

    '''
    setting auto offset reset to earliest will allow the consumer to start reading from the latest committed offset. This means whenever
    a message is consumed the master is updated by the offset. 
    Enabling auto commit as true  makes sure the consumer commits its read offset every interval.
    Group Id is given since we have enabled auto commit. This helps when a different consumer to consume the message from where this consumer left off.    
    '''
    my_consumer = KafkaConsumer( 
        'test1',  
         bootstrap_servers = ['localhost : 808'],  
         auto_offset_reset = 'earliest',  
         enable_auto_commit = True,  
         group_id = 'my-group',
         value_deserializer=lambda x: loads(x.decode('utf-8'))
         ) 
    
    multiple_requests(my_consumer)
    