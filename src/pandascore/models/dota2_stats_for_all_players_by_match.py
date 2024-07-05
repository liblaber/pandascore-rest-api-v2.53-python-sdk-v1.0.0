from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .dota2_team_for_all_stats_players import Dota2TeamForAllStatsPlayers


@JsonMap({})
class Dota2StatsForAllPlayersByMatch(BaseModel):
    """Dota2StatsForAllPlayersByMatch

    :param teams: teams
    :type teams: List[Dota2TeamForAllStatsPlayers]
    """

    def __init__(self, teams: List[Dota2TeamForAllStatsPlayers]):
        self.teams = self._define_list(teams, Dota2TeamForAllStatsPlayers)
