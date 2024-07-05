from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_team_averages import LoLTeamAverages
from .serie import Serie
from .lo_l_team_stats_totals import LoLTeamStatsTotals


@JsonMap({})
class LoLTeamBySerieStat(BaseModel):
    """Team's statistics for a serie

    :param averages: averages
    :type averages: LoLTeamAverages
    :param games_count: Number of games
    :type games_count: int
    :param serie: A serie, an occurrence of a league event
    :type serie: Serie
    :param totals: totals
    :type totals: LoLTeamStatsTotals
    """

    def __init__(
        self,
        averages: LoLTeamAverages,
        games_count: int,
        serie: Serie,
        totals: LoLTeamStatsTotals,
    ):
        self.averages = self._define_object(averages, LoLTeamAverages)
        self.games_count = games_count
        self.serie = self._define_object(serie, Serie)
        self.totals = self._define_object(totals, LoLTeamStatsTotals)
