from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_team_averages import LoLTeamAverages
from .lo_l_team_stats_totals import LoLTeamStatsTotals
from .tournament import Tournament


@JsonMap({})
class LoLTeamByTournamentStat(BaseModel):
    """Team's statistics for a tournament

    :param averages: averages
    :type averages: LoLTeamAverages
    :param games_count: Number of games
    :type games_count: int
    :param totals: totals
    :type totals: LoLTeamStatsTotals
    :param tournament: tournament
    :type tournament: Tournament
    """

    def __init__(
        self,
        averages: LoLTeamAverages,
        games_count: int,
        totals: LoLTeamStatsTotals,
        tournament: Tournament,
    ):
        self.averages = self._define_object(averages, LoLTeamAverages)
        self.games_count = games_count
        self.totals = self._define_object(totals, LoLTeamStatsTotals)
        self.tournament = self._define_object(tournament, Tournament)
