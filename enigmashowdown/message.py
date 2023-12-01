# This file contains things relating to type hinting messages

from typing import TypedDict, Optional, List

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

class Vec2(TypedDict):
    x: float
    y: float

class EntityState(TypedDict):
    id: str
    position: Vec2
    entityType: str

class MapCoordinate(TypedDict):
    x: int
    y: int

class BarrierTile(TypedDict):
    coordinate: MapCoordinate
    barrierType: str #TODO define BarrierType

class GameStateView(Packet):
    tick: int

class LevelEndStatistics(TypedDict):
    playerId: str
    status: str
    tickEndedOn: int
    damageTaken: int
    damageGiven: int
    enemiesDefeated: int

class ConquestStateView(GameStateView):
    entries: List[EntityState]
    barriers: List[BarrierTile]
    levelEndStatistics: List[LevelEndStatistics]

class LevelStateBroadcast(BroadcastMessage):
    ticksUntilBegin: int
    levelId: str
    gameStateView: GameStateView
