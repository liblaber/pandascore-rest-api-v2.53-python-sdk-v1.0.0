from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .player import Player
from .opponent_type_player import OpponentTypePlayer


@JsonMap({"type_": "type"})
class PlayerRosters(BaseModel):
    """Rosters for a series or a tournament with player participants

    :param rosters: rosters
    :type rosters: List[Player]
    :param type_: type_
    :type type_: OpponentTypePlayer
    """

    def __init__(self, rosters: List[Player], type_: OpponentTypePlayer):
        self.rosters = self._define_list(rosters, Player)
        self.type_ = self._enum_matching(type_, OpponentTypePlayer.list(), "type_")
