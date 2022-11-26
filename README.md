# Python-Kafka-using-Multithreading

Kafka is a distributed publish-subscribe messaging system that maintains feeds of messages in partitioned and replicated topics. In simple terms, kafka consists
of three important concepts:

Producer : Producers produce messages to a topic of their choice. 
Topics : Topics are logs that receive data from the producers and store them across their partitions.
Consumer : Consumers read the messages of a set of partitions of a topic of their choice at their own pace

In this project there are two files: producer.py and consumer.py. The aim of the project is to use kafka system for communication between different systems easily
and efficiently. The producer publishes the message into a topic using json format as per the requirement.

The consumer is written to subscribe to the topic on which messages are published and convert it into json format and send the message to desired
url. The consumer here is modified to handle bulk messages and send it to desired url simultaneously so saving time and making an efficient communication.
Multithreading in python is used to cater to handle this requirement.

Steps  to run code : 
1) Start the zookeeper server on your command prompt.
2) Run the publishe python code in another terminal and start publishing the messages.
3) In another terminal run the consumer code by navigating to its path and start consuming continous messages.  
