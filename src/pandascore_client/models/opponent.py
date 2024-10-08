# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .base_opponent import BaseOpponent, BaseOpponentGuard
from .base_player import BasePlayer
from .base_team import BaseTeam
from .opponent_type import OpponentType


@JsonMap({"type_": "type"})
class Opponent(BaseModel):
    """Opponent

    :param opponent: opponent
    :type opponent: BaseOpponent
    :param type_: type_
    :type type_: OpponentType
    """

    def __init__(self, opponent: BaseOpponent, type_: OpponentType):
        """Opponent

        :param opponent: opponent
        :type opponent: BaseOpponent
        :param type_: type_
        :type type_: OpponentType
        """
        self.opponent = BaseOpponentGuard.return_one_of(opponent)
        self.type_ = self._enum_matching(type_, OpponentType.list(), "type_")
