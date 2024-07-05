from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
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
        self.round = round
        self.teams = self._define_list(teams, OwGameRoundTeam)
