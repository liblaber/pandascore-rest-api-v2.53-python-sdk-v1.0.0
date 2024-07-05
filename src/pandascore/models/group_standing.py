from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .base_team import BaseTeam


@JsonMap({})
class GroupStanding(BaseModel):
    """GroupStanding

    :param losses: losses
    :type losses: int
    :param rank: rank
    :type rank: int
    :param team: team
    :type team: BaseTeam
    :param ties: Only present if ties occured during the tournament, defaults to None
    :type ties: int, optional
    :param total: total
    :type total: int
    :param wins: wins
    :type wins: int
    """

    def __init__(
        self,
        losses: int,
        rank: int,
        team: BaseTeam,
        total: int,
        wins: int,
        ties: int = None,
    ):
        self.losses = losses
        self.rank = rank
        self.team = self._define_object(team, BaseTeam)
        if ties is not None:
            self.ties = ties
        self.total = total
        self.wins = wins
