import os
import sys
import time
import yaml
from logger import logger
from azure.servicebus import ServiceBusClient, ServiceBusMessage


def send_a_list_of_messages(sender):
    messages = [ServiceBusMessage(f"Message in list {i}") for i in range(1000)]
    sender.send_messages(messages)
    logger.info("Sent a list of 1000 messages")

def main():
    with open("azure-service-bus.yaml", 'r') as stream:
        config = yaml.safe_load(stream)
    
    logger.info("Start sending messages")
    connection_string = config['connection_string']
    queue_name = config['queue_name']

    queue = ServiceBusClient.from_connection_string(conn_str=connection_string, queue_name=queue_name)

    with queue:
        sender = queue.get_queue_sender(queue_name=queue_name)
        with sender:
            send_a_list_of_messages(sender)

    logger.info("Done sending messages")
    logger.info("-----------------------")

if __name__ == "__main__":
    main()