import sys
import datetime
import time
import logging

import awsiot.greengrasscoreipc
from awsiot.greengrasscoreipc.model import (
    PublishToTopicRequest,
    PublishMessage,
    BinaryMessage
)

# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

FUTURE_WAIT_TIME = 10
SLEEP_TIME = 60

ipc_client = awsiot.greengrasscoreipc.connect()
                    
topic = "modbus/request/conveyer"
#message = '{"request": { "operation": "ReadCoilsRequest","device": 1,"address": 1,"count": 1 }, "id": "1" }' # used for modbus-rtu component
#message = '{ "id": "TestRequest", "function": "ReadCoils", "address": 00001, "quantity": 10 }'   
#message = '{ "id": "ReadVoltage", "function": "ReadHoldingRegisters", "address": 40, "quantity": 3 }'
message = '{ "id": "00824502", "function": "ReadInputRegisters", "address": 11, "quantity": 1 }'

logger.debug("topic: " + topic)
logger.debug("message: " + message)

request = PublishToTopicRequest()
request.topic = topic

publish_message = PublishMessage()
publish_message.binary_message = BinaryMessage()
publish_message.binary_message.message = bytes(message, "utf-8")
request.publish_message = publish_message

while True:

    operation = ipc_client.new_publish_to_topic()
    operation.activate(request)
    future = operation.get_response()
    future.result(FUTURE_WAIT_TIME)
    
    # Append the message to the log file.
    logger.info(message)
    
    logger.debug("going to sleep")
    time.sleep(SLEEP_TIME)

