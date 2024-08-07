from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .dota2_player_averages import Dota2PlayerAverages
from .serie import Serie
from .dota2_player_stats_totals import Dota2PlayerStatsTotals


@JsonMap({})
class Dota2PlayerBySerieStat(BaseModel):
    """Player's statistics for a serie

    :param averages: averages
    :type averages: Dota2PlayerAverages
    :param games_count: Number of games
    :type games_count: int
    :param serie: A serie, an occurrence of a league event
    :type serie: Serie
    :param totals: totals
    :type totals: Dota2PlayerStatsTotals
    """

    def __init__(
        self,
        averages: Dota2PlayerAverages,
        games_count: int,
        serie: Serie,
        totals: Dota2PlayerStatsTotals,
    ):
        self.averages = self._define_object(averages, Dota2PlayerAverages)
        self.games_count = games_count
        self.serie = self._define_object(serie, Serie)
        self.totals = self._define_object(totals, Dota2PlayerStatsTotals)
