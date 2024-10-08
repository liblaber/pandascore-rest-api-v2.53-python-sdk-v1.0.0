# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .ow_game_round_team import OwGameRoundTeam


@JsonMap({})
class OwGameRound(BaseModel):
    """OwGameRound

    :param round: round
    :type round: int
    :param teams: teams
    :type teams: List[OwGameRoundTeam]
    """

    def __init__(self, round: int, teams: List[OwGameRoundTeam]):
        """OwGameRound

        :param round: round
        :type round: int
        :param teams: teams
        :type teams: List[OwGameRoundTeam]
        """
        self.round = self._define_number("round", round, ge=1)
        self.teams = self._define_list(teams, OwGameRoundTeam)
