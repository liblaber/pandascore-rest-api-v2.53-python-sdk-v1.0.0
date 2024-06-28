# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_stats_counts_for_match import CsgoStatsCountsForMatch
from .match import Match
from .csgo_player_stats_game_averages import CsgoPlayerStatsGameAverages
from .csgo_stats_round_averages import CsgoStatsRoundAverages


@JsonMap({})
class CsgoPlayerStatsByMatch(BaseModel):
    """Statistics for a match

    :param counts: counts
    :type counts: CsgoStatsCountsForMatch
    :param match: match
    :type match: Match
    :param per_game_averages: per_game_averages
    :type per_game_averages: CsgoPlayerStatsGameAverages
    :param per_round_averages: per_round_averages
    :type per_round_averages: CsgoStatsRoundAverages
    """

    def __init__(
        self,
        counts: CsgoStatsCountsForMatch,
        match: Match,
        per_game_averages: CsgoPlayerStatsGameAverages,
        per_round_averages: CsgoStatsRoundAverages,
    ):
        self.counts = self._define_object(counts, CsgoStatsCountsForMatch)
        self.match = self._define_object(match, Match)
        self.per_game_averages = self._define_object(
            per_game_averages, CsgoPlayerStatsGameAverages
        )
        self.per_round_averages = self._define_object(
            per_round_averages, CsgoStatsRoundAverages
        )
