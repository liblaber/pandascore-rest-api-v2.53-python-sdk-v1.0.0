from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .dota2_player_averages import Dota2PlayerAverages
from .dota2_player_stats_totals import Dota2PlayerStatsTotals


@JsonMap({})
class Dota2TotalPlayerStat(BaseModel):
    """Total Player's statistics

    :param averages: averages
    :type averages: Dota2PlayerAverages
    :param games_count: Number of games
    :type games_count: int
    :param totals: totals
    :type totals: Dota2PlayerStatsTotals
    """

    def __init__(
        self,
        averages: Dota2PlayerAverages,
        games_count: int,
        totals: Dota2PlayerStatsTotals,
    ):
        self.averages = self._define_object(averages, Dota2PlayerAverages)
        self.games_count = games_count
        self.totals = self._define_object(totals, Dota2PlayerStatsTotals)
