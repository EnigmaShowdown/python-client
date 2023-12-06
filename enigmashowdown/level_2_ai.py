from enigmashowdown.framework import ClientFramework, StateListener
from enigmashowdown.message import LevelStateBroadcast, ConquestStateView
from enigmashowdown import ZeroMqRequestClient
from enigmashowdown.constants import PORT_SERVER
import math


class LevelOneAi(StateListener):
    def __call__(
        self,
        player_id: str,
        level_state_broadcast: LevelStateBroadcast,
        client: ZeroMqRequestClient,
    ):
        state: ConquestStateView = level_state_broadcast["gameStateView"]
        
        client.send(
            {
                "type": "player-action-request",
                "playerId": player_id,
                "levelTick": state["tick"],
                "playerAction": {
                    "type": "conquest-action",
                    "moveAction": {
                        "directionRadians": math.radians(0.0),
                        "speed": 5.0,
                    },
                },
            }
        )

        if state["tick"] > 32.0:
            client.send(
                {
                    "type": "player-action-request",
                    "playerId": player_id,
                    "levelTick": state["tick"],
                    "playerAction": {
                        "type": "conquest-action",
                        "moveAction": {
                            "directionRadians": math.radians(90.0),
                            "speed": 10.0,
                        },
                    },
                }
            )
        
        if state["tick"] > 40.0:
            client.send(
                {
                    "type": "player-action-request",
                    "playerId": player_id,
                    "levelTick": state["tick"],
                    "playerAction": {
                        "type": "conquest-action",
                        "moveAction": {
                            "directionRadians": math.radians(180.0),
                            "speed": 10.0,
                        },
                    },
                }
            )

        if state["tick"] > 55.0:
            client.send(
                {
                    "type": "player-action-request",
                    "playerId": player_id,
                    "levelTick": state["tick"],
                    "playerAction": {
                        "type": "conquest-action",
                        "moveAction": {
                            "directionRadians": math.radians(90.0),
                            "speed": 10.0,
                        },
                    },
                }
            )
        
        if state["tick"] > 65.0:
            client.send(
                {
                    "type": "player-action-request",
                    "playerId": player_id,
                    "levelTick": state["tick"],
                    "playerAction": {
                        "type": "conquest-action",
                        "moveAction": {
                            "directionRadians": math.radians(0.0),
                            "speed": 10.0,
                        },
                    },
                }
            )
        
        if state["tick"] > 75.0:
            client.send(
                {
                    "type": "player-action-request",
                    "playerId": player_id,
                    "levelTick": state["tick"],
                    "playerAction": {
                        "type": "conquest-action",
                        "moveAction": {
                            "directionRadians": math.radians(90.0),
                            "speed": 10.0,
                        },
                    },
                }
            )
        
        if state["tick"] > 83.0:
            client.send(
                {
                    "type": "player-action-request",
                    "playerId": player_id,
                    "levelTick": state["tick"],
                    "playerAction": {
                        "type": "conquest-action",
                        "moveAction": {
                            "directionRadians": math.radians(0.0),
                            "speed": 10.0,
                        },
                    },
                }
            )


if __name__ == "__main__":
    ClientFramework("localhost", PORT_SERVER, LevelOneAi()).start()
