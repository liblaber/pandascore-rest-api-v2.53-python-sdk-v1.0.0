from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .base_match import BaseMatch
from .base_team import BaseTeam


@JsonMap({})
class BracketStanding(BaseModel):
    """BracketStanding

    :param last_match: last_match
    :type last_match: BaseMatch
    :param rank: rank
    :type rank: int
    :param team: team
    :type team: BaseTeam
    """

    def __init__(self, last_match: BaseMatch, rank: int, team: BaseTeam):
        self.last_match = self._define_object(last_match, BaseMatch)
        self.rank = rank
        self.team = self._define_object(team, BaseTeam)
