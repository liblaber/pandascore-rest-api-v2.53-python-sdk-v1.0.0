from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .match import Match
from .valorant_player_match_stats import ValorantPlayerMatchStats


@JsonMap({})
class ValorantStatsForPlayersByMatch(BaseModel):
    """ValorantStatsForPlayersByMatch

    :param match: match
    :type match: Match
    :param stats: stats
    :type stats: List[ValorantPlayerMatchStats]
    """

    def __init__(self, match: Match, stats: List[ValorantPlayerMatchStats]):
        self.match = self._define_object(match, Match)
        self.stats = self._define_list(stats, ValorantPlayerMatchStats)
