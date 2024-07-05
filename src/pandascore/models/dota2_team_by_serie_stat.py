from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .dota2_team_averages import Dota2TeamAverages
from .serie import Serie
from .dota2_team_stats_totals import Dota2TeamStatsTotals


@JsonMap({})
class Dota2TeamBySerieStat(BaseModel):
    """Team's statistics for a serie

    :param averages: averages
    :type averages: Dota2TeamAverages
    :param games_count: Number of games
    :type games_count: int
    :param serie: A serie, an occurrence of a league event
    :type serie: Serie
    :param totals: totals
    :type totals: Dota2TeamStatsTotals
    """

    def __init__(
        self,
        averages: Dota2TeamAverages,
        games_count: int,
        serie: Serie,
        totals: Dota2TeamStatsTotals,
    ):
        self.averages = self._define_object(averages, Dota2TeamAverages)
        self.games_count = games_count
        self.serie = self._define_object(serie, Serie)
        self.totals = self._define_object(totals, Dota2TeamStatsTotals)
