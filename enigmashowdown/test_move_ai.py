from enigmashowdown.framework import ClientFramework, StateListener
from enigmashowdown.message import LevelStateBroadcast, ConquestStateView
from enigmashowdown import ZeroMqRequestClient
from enigmashowdown.constants import PORT_SERVER
import math


class MinimalMoveAI(StateListener):
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
                        "directionRadians": math.radians(30.0),
                        "speed": 5.0,
                    },
                },
            }
        )


if __name__ == "__main__":
    ClientFramework("localhost", PORT_SERVER, MinimalMoveAI()).start()
