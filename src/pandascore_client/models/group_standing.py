# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
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
        self.losses = self._define_number("losses", losses, ge=0)
        self.rank = self._define_number("rank", rank, ge=0)
        self.team = self._define_object(team, BaseTeam)
        if ties is not None:
            self.ties = self._define_number("ties", ties, ge=1)
        self.total = self._define_number("total", total, ge=0)
        self.wins = self._define_number("wins", wins, ge=0)
