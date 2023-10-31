# This is the main file for the python client

import zmq
import json
from message import RequestMessage, ResponseMessage, ConnectRequest, ConnectResponse


class ZeroMqBroadcastReceiver:
    def __init__(self, context: zmq.Context, host: str, port: int) -> None:
        self.context = context
        self.host = host
        self.port = port


class ZeroMqRequestClient:
    def __init__(self, context: zmq.Context, host: str, port: int) -> None:
        self.context = context
        self.host = host
        self.port = port
        
    def send(self, request: RequestMessage) -> ResponseMessage:
        with self.context.socket(zmq.REQ) as socket:
            socket.connect(f"tcp://{self.host}:{self.port}")

            request_json = json.dumps(request)

            socket.send(request_json.encode('utf-8'))

            response_json: str = socket.recv().decode('utf-8')
            
            return json.loads(response_json)


def client_test():
    """
    Common classes to look at (for now):

        ServerTest - class to run to test python client
        ZeroMqServerManager - contains server logic for creating REP socket (reply)
        EnigmaShowdownConstants - contains port nums
        ClientCommunicationTest - Kotlin equivalent of this function
        ZeroMqRequestClient - should eventually write in python (end goal); allows for easy communication with server
        ConnectRequest - class that is able to be serialized into json

    """

    request_json = """
{
    "type": "connect-request",
    "clientType": "PLAYER"
}
"""

    client = ZeroMqRequestClient(zmq.Context(), "localhost", 31877)

    connect_request: ConnectRequest = {"type": "connect-request", "clientType": "PLAYER"}

    for _ in range(10):
        connect_response: ConnectResponse = client.send(connect_request)

        print(connect_response)

    # for _ in range(10):
    #     socket.send(request_json.encode('utf-8'))

    #     #  Get the reply
    #     message = socket.recv().decode('utf-8')
    #     print(message)
    
    return


def broadcast_test():
    """
    Common classes to reference:
        BroadcastServerTest - class to run that python broadcast client will comm with
        ZeroMqBroadcastManager - contains server logic for creating PUB socket (publish)
        ClientBroadcastListenTest - Kotlin equivalent of this function
        TODO: implement ZeroMqBroadcastReceiver function in ClientBroadcastReceiver
            has logic for creating SUB (subscribe) socket
    """

    context = zmq.Context()

    #  Socket to talk to server
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:31878")

    socket.subscribe("")

    for _ in range(10):
        message = socket.recv().decode('utf-8')
        print(message)

    return

if __name__=="__main__":
    client_test()
    # broadcast_test()