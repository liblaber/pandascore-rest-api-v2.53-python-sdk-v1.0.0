# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .search_over_valorant_short_tournaments_tier_2 import (
    SearchOverValorantShortTournamentsTier2,
)
from .opponent_type import OpponentType


@JsonMap({})
class SearchOverValorantShortTournaments(BaseModel):
    """SearchOverValorantShortTournaments

    :param name: name, defaults to None
    :type name: str, optional
    :param prizepool: prizepool, defaults to None
    :type prizepool: str, optional
    :param slug: slug, defaults to None
    :type slug: str, optional
    :param tier: The tier of the tournament, ranging from 'S' to 'Unranked'. Ranking 'S' > 'A' > 'B' > 'C' > 'D' > 'Unranked', defaults to None
    :type tier: SearchOverValorantShortTournamentsTier2, optional
    :param winner_type: winner_type, defaults to None
    :type winner_type: OpponentType, optional
    """

    def __init__(
        self,
        name: str = None,
        prizepool: str = None,
        slug: str = None,
        tier: SearchOverValorantShortTournamentsTier2 = None,
        winner_type: OpponentType = None,
    ):
        if name is not None:
            self.name = name
        if prizepool is not None:
            self.prizepool = prizepool
        if slug is not None:
            self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
        if tier is not None:
            self.tier = self._enum_matching(
                tier, SearchOverValorantShortTournamentsTier2.list(), "tier"
            )
        if winner_type is not None:
            self.winner_type = self._enum_matching(
                winner_type, OpponentType.list(), "winner_type"
            )
