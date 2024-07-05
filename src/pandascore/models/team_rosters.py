from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .team import Team
from .opponent_type_team import OpponentTypeTeam


@JsonMap({"type_": "type"})
class TeamRosters(BaseModel):
    """Rosters for a a series or a tournament with team participants

    :param rosters: A list of teams
    :type rosters: List[Team]
    :param type_: type_
    :type type_: OpponentTypeTeam
    """

    def __init__(self, rosters: List[Team], type_: OpponentTypeTeam):
        self.rosters = self._define_list(rosters, Team)
        self.type_ = self._enum_matching(type_, OpponentTypeTeam.list(), "type_")
