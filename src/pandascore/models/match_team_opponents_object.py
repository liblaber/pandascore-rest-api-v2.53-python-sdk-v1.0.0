from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .opponent_type_team import OpponentTypeTeam
from .team import Team


@JsonMap({})
class MatchTeamOpponentsObject(BaseModel):
    """MatchTeamOpponentsObject

    :param opponent_type: opponent_type
    :type opponent_type: OpponentTypeTeam
    :param opponents: A list of teams
    :type opponents: List[Team]
    """

    def __init__(self, opponent_type: OpponentTypeTeam, opponents: List[Team]):
        self.opponent_type = self._enum_matching(
            opponent_type, OpponentTypeTeam.list(), "opponent_type"
        )
        self.opponents = self._define_list(opponents, Team)
