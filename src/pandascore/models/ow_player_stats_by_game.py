from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .ow_player_averages import OwPlayerAverages
from .ow_game_stats_game import OwGameStatsGame
from .ow_player10_min_averages import OwPlayer10MinAverages
from .ow_player_game_averages import OwPlayerGameAverages
from .ow_player_game_totals_for_game import OwPlayerGameTotalsForGame


@JsonMap({})
class OwPlayerStatsByGame(BaseModel):
    """Player's statistics for a game

    :param averages: averages
    :type averages: OwPlayerAverages
    :param game: A game
    :type game: OwGameStatsGame
    :param game_id: game_id
    :type game_id: int
    :param games_count: Number of games
    :type games_count: int
    :param per_10_minutes_averages: per_10_minutes_averages
    :type per_10_minutes_averages: OwPlayer10MinAverages
    :param per_game_averages: per_game_averages
    :type per_game_averages: OwPlayerGameAverages
    :param totals: totals
    :type totals: OwPlayerGameTotalsForGame
    """

    def __init__(
        self,
        averages: OwPlayerAverages,
        game: OwGameStatsGame,
        game_id: int,
        games_count: int,
        per_10_minutes_averages: OwPlayer10MinAverages,
        per_game_averages: OwPlayerGameAverages,
        totals: OwPlayerGameTotalsForGame,
    ):
        self.averages = self._define_object(averages, OwPlayerAverages)
        self.game = self._define_object(game, OwGameStatsGame)
        self.game_id = game_id
        self.games_count = games_count
        self.per_10_minutes_averages = self._define_object(
            per_10_minutes_averages, OwPlayer10MinAverages
        )
        self.per_game_averages = self._define_object(
            per_game_averages, OwPlayerGameAverages
        )
        self.totals = self._define_object(totals, OwPlayerGameTotalsForGame)
