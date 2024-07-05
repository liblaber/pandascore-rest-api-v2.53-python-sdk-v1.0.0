from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_stats_counts import CsgoStatsCounts
from .csgo_player_stats_game_averages import CsgoPlayerStatsGameAverages
from .csgo_stats_round_averages import CsgoStatsRoundAverages
from .serie import Serie


@JsonMap({})
class CsgoPlayerStatsBySerie(BaseModel):
    """Statistics for a serie

    :param counts: counts
    :type counts: CsgoStatsCounts
    :param per_game_averages: per_game_averages
    :type per_game_averages: CsgoPlayerStatsGameAverages
    :param per_round_averages: per_round_averages
    :type per_round_averages: CsgoStatsRoundAverages
    :param serie: A serie, an occurrence of a league event
    :type serie: Serie
    """

    def __init__(
        self,
        counts: CsgoStatsCounts,
        per_game_averages: CsgoPlayerStatsGameAverages,
        per_round_averages: CsgoStatsRoundAverages,
        serie: Serie,
    ):
        self.counts = self._define_object(counts, CsgoStatsCounts)
        self.per_game_averages = self._define_object(
            per_game_averages, CsgoPlayerStatsGameAverages
        )
        self.per_round_averages = self._define_object(
            per_round_averages, CsgoStatsRoundAverages
        )
        self.serie = self._define_object(serie, Serie)
