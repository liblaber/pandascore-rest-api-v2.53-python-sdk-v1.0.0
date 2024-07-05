from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_stats_counts import CsgoStatsCounts
from .csgo_team_map_stats import CsgoTeamMapStats
from .csgo_team_stats_game_averages import CsgoTeamStatsGameAverages
from .csgo_stats_round_averages import CsgoStatsRoundAverages


@JsonMap({})
class CsgoTeamStats(BaseModel):
    """Statistics for all matches

    :param counts: counts
    :type counts: CsgoStatsCounts
    :param maps: maps
    :type maps: List[CsgoTeamMapStats]
    :param per_game_averages: per_game_averages
    :type per_game_averages: CsgoTeamStatsGameAverages
    :param per_round_averages: per_round_averages
    :type per_round_averages: CsgoStatsRoundAverages
    """

    def __init__(
        self,
        counts: CsgoStatsCounts,
        maps: List[CsgoTeamMapStats],
        per_game_averages: CsgoTeamStatsGameAverages,
        per_round_averages: CsgoStatsRoundAverages,
    ):
        self.counts = self._define_object(counts, CsgoStatsCounts)
        self.maps = self._define_list(maps, CsgoTeamMapStats)
        self.per_game_averages = self._define_object(
            per_game_averages, CsgoTeamStatsGameAverages
        )
        self.per_round_averages = self._define_object(
            per_round_averages, CsgoStatsRoundAverages
        )
