from __future__ import annotations
from typing import Union
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .search_over_valorant_short_tournaments_tier_2 import (
    SearchOverValorantShortTournamentsTier2,
)
from .opponent_id import OpponentId, OpponentIdGuard
from .opponent_type import OpponentType


class FilterOverStarcraftBroodWarShortTournamentsVideogameTitleGuard(OneOfBaseModel):
    class_list = {"int": int, "str": str}


FilterOverStarcraftBroodWarShortTournamentsVideogameTitle = Union[int, str]


@JsonMap({"id_": "id"})
class FilterOverStarcraftBroodWarShortTournaments(BaseModel):
    """FilterOverStarcraftBroodWarShortTournaments

    :param begin_at: begin_at, defaults to None
    :type begin_at: List[str], optional
    :param detailed_stats: Whether the tournament is expected to have detailed statistics available, defaults to None
    :type detailed_stats: bool, optional
    :param end_at: end_at, defaults to None
    :type end_at: List[str], optional
    :param has_bracket: Whether the tournament has a bracket, defaults to None
    :type has_bracket: bool, optional
    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param live_supported: Whether live is supported, defaults to None
    :type live_supported: bool, optional
    :param modified_at: modified_at, defaults to None
    :type modified_at: List[str], optional
    :param name: name, defaults to None
    :type name: List[str], optional
    :param prizepool: prizepool, defaults to None
    :type prizepool: List[str], optional
    :param serie_id: serie_id, defaults to None
    :type serie_id: List[int], optional
    :param slug: slug, defaults to None
    :type slug: List[str], optional
    :param tier: tier, defaults to None
    :type tier: List[SearchOverValorantShortTournamentsTier2], optional
    :param videogame_title: A videogame title id or slug. <br/>Only for `/csgo/*`, `/codmw/*`, `/fifa/*` and `/ow/*` endpoints <br/>, defaults to None
    :type videogame_title: List[FilterOverStarcraftBroodWarShortTournamentsVideogameTitle], optional
    :param winner_id: winner_id, defaults to None
    :type winner_id: List[OpponentId], optional
    :param winner_type: winner_type, defaults to None
    :type winner_type: List[OpponentType], optional
    """

    def __init__(
        self,
        begin_at: List[str] = None,
        detailed_stats: bool = None,
        end_at: List[str] = None,
        has_bracket: bool = None,
        id_: List[int] = None,
        live_supported: bool = None,
        modified_at: List[str] = None,
        name: List[str] = None,
        prizepool: List[str] = None,
        serie_id: List[int] = None,
        slug: List[str] = None,
        tier: List[SearchOverValorantShortTournamentsTier2] = None,
        videogame_title: List[
            FilterOverStarcraftBroodWarShortTournamentsVideogameTitle
        ] = None,
        winner_id: List[OpponentId] = None,
        winner_type: List[OpponentType] = None,
    ):
        if begin_at is not None:
            self.begin_at = begin_at
        if detailed_stats is not None:
            self.detailed_stats = detailed_stats
        if end_at is not None:
            self.end_at = end_at
        if has_bracket is not None:
            self.has_bracket = has_bracket
        if id_ is not None:
            self.id_ = id_
        if live_supported is not None:
            self.live_supported = live_supported
        if modified_at is not None:
            self.modified_at = modified_at
        if name is not None:
            self.name = name
        if prizepool is not None:
            self.prizepool = prizepool
        if serie_id is not None:
            self.serie_id = serie_id
        if slug is not None:
            self.slug = slug
        if tier is not None:
            self.tier = self._define_list(tier, SearchOverValorantShortTournamentsTier2)
        if videogame_title is not None:
            self.videogame_title = self._define_list(
                videogame_title,
                FilterOverStarcraftBroodWarShortTournamentsVideogameTitle,
            )
        if winner_id is not None:
            self.winner_id = self._define_list(winner_id, OpponentId)
        if winner_type is not None:
            self.winner_type = self._define_list(winner_type, OpponentType)
