# This is the main file for the python client

import zmq
import json
from enigmashowdown.message import (
    RequestMessage,
    ResponseMessage,
    ConnectRequest,
    ConnectResponse,
    BroadcastMessage,
)


class ZeroMqBroadcastReceiver:
    def __init__(
        self, context: zmq.Context, host: str, port: int, subscribe_topic: str
    ) -> None:
        self.context = context
        self.host = host
        self.port = port
        self.subscribe_topic = subscribe_topic
        self.socket = self.context.socket(zmq.SUB)

    def start(self):
        #  Socket to talk to server
        self.socket.connect(f"tcp://{self.host}:{self.port}")
        self.socket.subscribe("")

    def take_message(self) -> BroadcastMessage:
        response_json: str = self.socket.recv().decode("utf-8")

        return json.loads(response_json)


class ZeroMqRequestClient:
    def __init__(self, context: zmq.Context, host: str, port: int) -> None:
        self.context = context
        self.host = host
        self.port = port

    def send(self, request: RequestMessage) -> ResponseMessage:
        with self.context.socket(zmq.REQ) as socket:
            socket.connect(f"tcp://{self.host}:{self.port}")

            request_json = json.dumps(request)

            socket.send(request_json.encode("utf-8"))

            response_json: str = socket.recv().decode("utf-8")

            return json.loads(response_json)


def client_test():
    client = ZeroMqRequestClient(zmq.Context(), "localhost", 31877)

    connect_request: ConnectRequest = {
        "type": "connect-request",
        "clientType": "PLAYER",
    }

    for _ in range(10):
        connect_response: ConnectResponse = client.send(connect_request)

        print(connect_response)

    return


def broadcast_test():
    broadcast_receiver = ZeroMqBroadcastReceiver(zmq.Context(), "localhost", 31878, "")
    broadcast_receiver.start()

    for _ in range(20):
        message = broadcast_receiver.take_message()
        print(message)

    return


if __name__ == "__main__":
    # client_test()
    broadcast_test()
