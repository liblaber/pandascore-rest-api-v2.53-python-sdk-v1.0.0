from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .dota2_player_averages import Dota2PlayerAverages
from .dota2_player_stats_totals import Dota2PlayerStatsTotals
from .tournament import Tournament


@JsonMap({})
class Dota2PlayerByTournamentStat(BaseModel):
    """Player's statistics for a tournament

    :param averages: averages
    :type averages: Dota2PlayerAverages
    :param games_count: Number of games
    :type games_count: int
    :param totals: totals
    :type totals: Dota2PlayerStatsTotals
    :param tournament: tournament
    :type tournament: Tournament
    """

    def __init__(
        self,
        averages: Dota2PlayerAverages,
        games_count: int,
        totals: Dota2PlayerStatsTotals,
        tournament: Tournament,
    ):
        self.averages = self._define_object(averages, Dota2PlayerAverages)
        self.games_count = games_count
        self.totals = self._define_object(totals, Dota2PlayerStatsTotals)
        self.tournament = self._define_object(tournament, Tournament)
