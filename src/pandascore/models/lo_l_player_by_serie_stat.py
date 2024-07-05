from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_player_averages import LoLPlayerAverages
from .serie import Serie
from .lo_l_player_stats_totals import LoLPlayerStatsTotals


@JsonMap({})
class LoLPlayerBySerieStat(BaseModel):
    """Player's statistics for a serie

    :param averages: averages
    :type averages: LoLPlayerAverages
    :param games_count: Number of games
    :type games_count: int
    :param serie: A serie, an occurrence of a league event
    :type serie: Serie
    :param totals: totals
    :type totals: LoLPlayerStatsTotals
    """

    def __init__(
        self,
        averages: LoLPlayerAverages,
        games_count: int,
        serie: Serie,
        totals: LoLPlayerStatsTotals,
    ):
        self.averages = self._define_object(averages, LoLPlayerAverages)
        self.games_count = games_count
        self.serie = self._define_object(serie, Serie)
        self.totals = self._define_object(totals, LoLPlayerStatsTotals)
