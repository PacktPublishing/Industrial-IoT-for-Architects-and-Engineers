import sys
import time
import traceback
import logging
import json

import awsiot.greengrasscoreipc
import awsiot.greengrasscoreipc.client as client
from awsiot.greengrasscoreipc.model import (
    IoTCoreMessage,
    QOS,
    PublishToIoTCoreRequest,
    SubscribeToTopicRequest,
    SubscriptionResponseMessage
)


# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

TIMEOUT = 10

ipc_client = awsiot.greengrasscoreipc.connect()
                    
class StreamHandler(client.SubscribeToTopicStreamHandler):
    def __init__(self):
        super().__init__()

    def on_stream_event(self, event: SubscriptionResponseMessage) -> None:
        try:
            message_string = str(event.binary_message.message, "utf-8")
            # Handle message.
            logger.debug("received message")
            logger.debug( message_string )

            #pubiotcore = PublishToIoTCoreRequest()
            #pubiotcore.topic_name = "modbus/response/conveyer/1"
            #pubiotcore.payload = event.binary_message.message    
            #pubiotcore.qos = QOS.AT_LEAST_ONCE
            #logger.debug("new publish to iot core")
            #operation = ipc_client.new_publish_to_iot_core()
            #logger.debug("activate")
            #operation.activate(pubiotcore)
            #future = operation.get_response()
            #logger.debug("waiting on future result")
            #future.result(TIMEOUT)
            #logger.debug("sent to IoT Core")
        except:
            traceback.print_exc()
            logger.debug("exception in handler receive")

    def on_stream_error(self, error: Exception) -> bool:
        # Handle error.
        logger.debug("handler error")
        logger.debug( Exception)
        return True  # Return True to close stream, False to keep stream open.

    def on_stream_closed(self) -> None:
        # Handle close.
        logger.debug("closing stream")
        pass


topic = "modbus/response/conveyer"

request = SubscribeToTopicRequest()
request.topic = topic
handler = StreamHandler()
operation = ipc_client.new_subscribe_to_topic(handler) 
future = operation.activate(request)
future.result(TIMEOUT)

# Keep the main thread alive, or the process will exit.
while True:
    time.sleep(10)
    
# To stop subscribing, close the operation stream.
operation.close()