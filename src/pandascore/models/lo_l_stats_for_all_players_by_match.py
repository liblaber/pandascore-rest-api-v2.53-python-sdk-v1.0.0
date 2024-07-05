from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_team_for_all_stats_players import LoLTeamForAllStatsPlayers


@JsonMap({})
class LoLStatsForAllPlayersByMatch(BaseModel):
    """LoLStatsForAllPlayersByMatch

    :param teams: teams
    :type teams: List[LoLTeamForAllStatsPlayers]
    """

    def __init__(self, teams: List[LoLTeamForAllStatsPlayers]):
        self.teams = self._define_list(teams, LoLTeamForAllStatsPlayers)
