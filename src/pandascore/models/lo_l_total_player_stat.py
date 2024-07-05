from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_player_averages import LoLPlayerAverages
from .lo_l_player_stats_totals import LoLPlayerStatsTotals


@JsonMap({})
class LoLTotalPlayerStat(BaseModel):
    """Total Player's statistics

    :param averages: averages
    :type averages: LoLPlayerAverages
    :param games_count: Number of games
    :type games_count: int
    :param totals: totals
    :type totals: LoLPlayerStatsTotals
    """

    def __init__(
        self,
        averages: LoLPlayerAverages,
        games_count: int,
        totals: LoLPlayerStatsTotals,
    ):
        self.averages = self._define_object(averages, LoLPlayerAverages)
        self.games_count = games_count
        self.totals = self._define_object(totals, LoLPlayerStatsTotals)
