import zmq
from enigmashowdown.constants import TICKS_PER_SECOND
from typing import Callable
from enigmashowdown import ZeroMqBroadcastReceiver, ZeroMqRequestClient
from enigmashowdown.message import (
    RequestMessage,
    ResponseMessage,
    ConnectRequest,
    ConnectResponse,
    BroadcastMessage,
    LevelStateBroadcast,
    KeepAliveRequest,
)

StateListener = Callable[[str, LevelStateBroadcast, ZeroMqRequestClient], None]

# check that response type is a ConnectResponse type


class ClientFramework:
    def __init__(self, host: str, server_port: int, state_listener: StateListener):
        self.host = host
        self.server_port = server_port
        self.state_listener = state_listener

    def start(self):
        # TODO: see below
        # note: whenever you see something like response.type, you actually have to write response["type"]
        # init context
        context = zmq.Context()

        # init ZeroMqRequestClient as client
        client: ZeroMqRequestClient = ZeroMqRequestClient(
            context, self.host, self.server_port
        )
        connect_request: ConnectRequest = {
            "type": "connect-request",
            "clientType": "PLAYER",
        }
        response: ResponseMessage = client.send(
            connect_request
        )  # somethinng here - call client.send

        # confirm response.type is "connect-response"
        if response["type"] != "connect-response":
            raise ValueError(f"Bad response: {response['type']}")

        connect_response: ConnectResponse = response  # this is a sort of "cast"

        player_id = connect_response["uuid"]

        # init ZeroMqBroadcastReceiver with data from connect_response
        broadcast_receiver: ZeroMqBroadcastReceiver = ZeroMqBroadcastReceiver(
            context,
            self.host,
            connect_response["broadcastPort"],
            connect_response["subscribeTopic"],
        )
        broadcast_receiver.start()
        print(f"Connected to server... player_id: {player_id}")
        # enter while true loop
        while True:
            message: BroadcastMessage = broadcast_receiver.take_message()
            if message["type"] == "level-state-broadcast":
                level_state_broadcast: LevelStateBroadcast = message
                if (
                    level_state_broadcast["ticksUntilBegin"] > 0
                    and level_state_broadcast["ticksUntilBegin"] % TICKS_PER_SECOND == 0
                ):
                    client.send({"type": "keep-alive-request", "clientId": player_id})
                # Call self.state_listener here
                self.state_listener(player_id, level_state_broadcast, client)
