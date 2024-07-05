from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_team_for_all_stats_players import CsgoTeamForAllStatsPlayers


@JsonMap({})
class CsgoStatsForAllPlayersByMatch(BaseModel):
    """CsgoStatsForAllPlayersByMatch

    :param teams: teams
    :type teams: List[CsgoTeamForAllStatsPlayers]
    """

    def __init__(self, teams: List[CsgoTeamForAllStatsPlayers]):
        self.teams = self._define_list(teams, CsgoTeamForAllStatsPlayers)
