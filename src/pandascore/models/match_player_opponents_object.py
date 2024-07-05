from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .opponent_type_player import OpponentTypePlayer
from .match_opponent_base_player import MatchOpponentBasePlayer


@JsonMap({})
class MatchPlayerOpponentsObject(BaseModel):
    """MatchPlayerOpponentsObject

    :param opponent_type: opponent_type
    :type opponent_type: OpponentTypePlayer
    :param opponents: A list of players
    :type opponents: List[MatchOpponentBasePlayer]
    """

    def __init__(
        self,
        opponent_type: OpponentTypePlayer,
        opponents: List[MatchOpponentBasePlayer],
    ):
        self.opponent_type = self._enum_matching(
            opponent_type, OpponentTypePlayer.list(), "opponent_type"
        )
        self.opponents = self._define_list(opponents, MatchOpponentBasePlayer)
