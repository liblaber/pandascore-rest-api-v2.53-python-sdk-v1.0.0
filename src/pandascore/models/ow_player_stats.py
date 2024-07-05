from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .ow_player_averages import OwPlayerAverages
from .ow_player10_min_averages import OwPlayer10MinAverages
from .ow_player_game_averages import OwPlayerGameAverages
from .ow_player_totals import OwPlayerTotals


@JsonMap({})
class OwPlayerStats(BaseModel):
    """Player's statistics

    :param averages: averages
    :type averages: OwPlayerAverages
    :param games_count: Number of games
    :type games_count: int
    :param per_10_minutes_averages: per_10_minutes_averages
    :type per_10_minutes_averages: OwPlayer10MinAverages
    :param per_game_averages: per_game_averages
    :type per_game_averages: OwPlayerGameAverages
    :param totals: totals
    :type totals: OwPlayerTotals
    """

    def __init__(
        self,
        averages: OwPlayerAverages,
        games_count: int,
        per_10_minutes_averages: OwPlayer10MinAverages,
        per_game_averages: OwPlayerGameAverages,
        totals: OwPlayerTotals,
    ):
        self.averages = self._define_object(averages, OwPlayerAverages)
        self.games_count = games_count
        self.per_10_minutes_averages = self._define_object(
            per_10_minutes_averages, OwPlayer10MinAverages
        )
        self.per_game_averages = self._define_object(
            per_game_averages, OwPlayerGameAverages
        )
        self.totals = self._define_object(totals, OwPlayerTotals)
