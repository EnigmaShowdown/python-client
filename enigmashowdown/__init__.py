# This is the main file for the python client

import zmq

"""
Common classes to look at (for now):

    ServerTest - class to run to test python client
    ZeroMqServerManager - contains server logic for creating REP socket (reply)
    EnigmaShowdownConstants - contains port nums
    ClientCommunicationTest - Kotlin equivalent of python client file
    ZeroMqRequestClient - should eventually write in python (end goal); allows for easy communication with server
    ConnectRequest - class that is able to be serialized into json

"""

def main():
    request_json = """
{
    "type": "connect-request",
    "clientType": "PLAYER"
}
"""

    context = zmq.Context()

    #  Socket to talk to server
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:31877")

    for _ in range(10):
        socket.send(request_json.encode('utf-8'))

        #  Get the reply.
        message = socket.recv().decode('utf-8')
        print(message)

    return

if __name__=="__main__":
    main()