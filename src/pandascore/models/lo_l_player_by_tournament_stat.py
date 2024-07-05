from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_player_averages import LoLPlayerAverages
from .lo_l_player_stats_totals import LoLPlayerStatsTotals
from .tournament import Tournament


@JsonMap({})
class LoLPlayerByTournamentStat(BaseModel):
    """Player's statistics for a tournament

    :param averages: averages
    :type averages: LoLPlayerAverages
    :param games_count: Number of games
    :type games_count: int
    :param totals: totals
    :type totals: LoLPlayerStatsTotals
    :param tournament: tournament
    :type tournament: Tournament
    """

    def __init__(
        self,
        averages: LoLPlayerAverages,
        games_count: int,
        totals: LoLPlayerStatsTotals,
        tournament: Tournament,
    ):
        self.averages = self._define_object(averages, LoLPlayerAverages)
        self.games_count = games_count
        self.totals = self._define_object(totals, LoLPlayerStatsTotals)
        self.tournament = self._define_object(tournament, Tournament)
