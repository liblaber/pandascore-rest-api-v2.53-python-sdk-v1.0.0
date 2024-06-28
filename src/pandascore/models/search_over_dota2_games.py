# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .game_status import GameStatus
from .opponent_type import OpponentType


@JsonMap({})
class SearchOverDota2Games(BaseModel):
    """SearchOverDota2Games

    :param status: The game status, defaults to None
    :type status: GameStatus, optional
    :param winner_type: winner_type, defaults to None
    :type winner_type: OpponentType, optional
    """

    def __init__(self, status: GameStatus = None, winner_type: OpponentType = None):
        if status is not None:
            self.status = self._enum_matching(status, GameStatus.list(), "status")
        if winner_type is not None:
            self.winner_type = self._enum_matching(
                winner_type, OpponentType.list(), "winner_type"
            )
