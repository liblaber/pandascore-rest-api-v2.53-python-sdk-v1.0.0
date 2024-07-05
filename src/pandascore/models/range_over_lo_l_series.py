from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .opponent_id import OpponentId, OpponentIdGuard
from .opponent_type import OpponentType


@JsonMap({"id_": "id"})
class RangeOverLoLSeries(BaseModel):
    """RangeOverLoLSeries

    :param begin_at: begin_at, defaults to None
    :type begin_at: List[str], optional
    :param end_at: end_at, defaults to None
    :type end_at: List[str], optional
    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param league_id: league_id, defaults to None
    :type league_id: List[int], optional
    :param modified_at: modified_at, defaults to None
    :type modified_at: List[str], optional
    :param name: name, defaults to None
    :type name: List[str], optional
    :param season: season, defaults to None
    :type season: List[str], optional
    :param slug: slug, defaults to None
    :type slug: List[str], optional
    :param winner_id: winner_id, defaults to None
    :type winner_id: List[OpponentId], optional
    :param winner_type: winner_type, defaults to None
    :type winner_type: List[OpponentType], optional
    :param year: year, defaults to None
    :type year: List[int], optional
    """

    def __init__(
        self,
        begin_at: List[str] = None,
        end_at: List[str] = None,
        id_: List[int] = None,
        league_id: List[int] = None,
        modified_at: List[str] = None,
        name: List[str] = None,
        season: List[str] = None,
        slug: List[str] = None,
        winner_id: List[OpponentId] = None,
        winner_type: List[OpponentType] = None,
        year: List[int] = None,
    ):
        if begin_at is not None:
            self.begin_at = begin_at
        if end_at is not None:
            self.end_at = end_at
        if id_ is not None:
            self.id_ = id_
        if league_id is not None:
            self.league_id = league_id
        if modified_at is not None:
            self.modified_at = modified_at
        if name is not None:
            self.name = name
        if season is not None:
            self.season = season
        if slug is not None:
            self.slug = slug
        if winner_id is not None:
            self.winner_id = self._define_list(winner_id, OpponentId)
        if winner_type is not None:
            self.winner_type = self._define_list(winner_type, OpponentType)
        if year is not None:
            self.year = year
