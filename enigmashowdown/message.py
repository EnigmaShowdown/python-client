# This file contains things relating to type hinting messages

from typing import TypedDict, Optional

class Packet(TypedDict):
    type: str

class RequestMessage(Packet):
    pass

class ResponseMessage(Packet):
    pass

class BroadcastMessage(Packet):
    pass

class PlayerAction(Packet):
    pass

class MoveAction(TypedDict):
    directionRadians: float
    speed: float

class ConquestAction(PlayerAction):
    moveAction: Optional[MoveAction]

class PlayerActionRequest(RequestMessage):
    playerId: str
    levelTick: int
    playerAction: PlayerAction

class KeepAliveRequest(RequestMessage):
    clientId: str

class ConnectRequest(RequestMessage):
    clientType: str

class ConnectResponse(ResponseMessage):
    uuid: str
    broadcastPort: int
    subscribeTopic: str

