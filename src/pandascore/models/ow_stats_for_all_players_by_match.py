from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .ow_team_for_all_stats_players import OwTeamForAllStatsPlayers


@JsonMap({})
class OwStatsForAllPlayersByMatch(BaseModel):
    """OwStatsForAllPlayersByMatch

    :param teams: teams
    :type teams: List[OwTeamForAllStatsPlayers]
    """

    def __init__(self, teams: List[OwTeamForAllStatsPlayers]):
        self.teams = self._define_list(teams, OwTeamForAllStatsPlayers)
