from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_stats_counts_for_match import CsgoStatsCountsForMatch
from .csgo_team_map_stats import CsgoTeamMapStats
from .match import Match
from .csgo_team_stats_game_averages import CsgoTeamStatsGameAverages
from .csgo_stats_round_averages import CsgoStatsRoundAverages


@JsonMap({})
class CsgoTeamStatsByMatch(BaseModel):
    """Statistics for a match

    :param counts: counts
    :type counts: CsgoStatsCountsForMatch
    :param maps: maps
    :type maps: List[CsgoTeamMapStats]
    :param match: match
    :type match: Match
    :param per_game_averages: per_game_averages
    :type per_game_averages: CsgoTeamStatsGameAverages
    :param per_round_averages: per_round_averages
    :type per_round_averages: CsgoStatsRoundAverages
    """

    def __init__(
        self,
        counts: CsgoStatsCountsForMatch,
        maps: List[CsgoTeamMapStats],
        match: Match,
        per_game_averages: CsgoTeamStatsGameAverages,
        per_round_averages: CsgoStatsRoundAverages,
    ):
        self.counts = self._define_object(counts, CsgoStatsCountsForMatch)
        self.maps = self._define_list(maps, CsgoTeamMapStats)
        self.match = self._define_object(match, Match)
        self.per_game_averages = self._define_object(
            per_game_averages, CsgoTeamStatsGameAverages
        )
        self.per_round_averages = self._define_object(
            per_round_averages, CsgoStatsRoundAverages
        )
