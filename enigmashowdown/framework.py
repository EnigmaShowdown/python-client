from typing import Callable
from enigmashowdown import ZeroMqRequestClient
from enigmashowdown.message import ConnectResponse, LevelStateBroadcast

StateListener = Callable[[str, LevelStateBroadcast, ZeroMqRequestClient], None]

# check that response type is a ConnectResponse type


class ClientFramework:
    def start():
        # TODO: see below
        # also note: whenever you see something like response.type, you actually have to write response["type"]
        # init context
        # init ZeroMqRequestClient as client
        response = None # somethinng here - call client.send
        # confirm response.type is "connect-response"
        connect_response: ConnectResponse = response # this is a sort of "cast"
        # init ZeroMqBroadcastReceiver with data from connect_response
        # enter while true loop
        #   Call self.state_listener here
