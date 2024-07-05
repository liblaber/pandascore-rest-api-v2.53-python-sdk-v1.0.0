from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .dota2_team_averages import Dota2TeamAverages
from .dota2_team_stats_totals import Dota2TeamStatsTotals


@JsonMap({})
class Dota2TotalTeamStat(BaseModel):
    """Total Team's statistics

    :param averages: averages
    :type averages: Dota2TeamAverages
    :param games_count: Number of games
    :type games_count: int
    :param totals: totals
    :type totals: Dota2TeamStatsTotals
    """

    def __init__(
        self,
        averages: Dota2TeamAverages,
        games_count: int,
        totals: Dota2TeamStatsTotals,
    ):
        self.averages = self._define_object(averages, Dota2TeamAverages)
        self.games_count = games_count
        self.totals = self._define_object(totals, Dota2TeamStatsTotals)
