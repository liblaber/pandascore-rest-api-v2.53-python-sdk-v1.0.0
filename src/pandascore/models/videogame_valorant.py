from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .videogame_league import VideogameLeague


@JsonMap({"id_": "id"})
class VideogameValorant(BaseModel):
    """VideogameValorant

    :param current_version: current_version
    :type current_version: str
    :param id_: id_
    :type id_: any
    :param leagues: leagues
    :type leagues: List[VideogameLeague]
    :param name: name
    :type name: any
    :param slug: slug
    :type slug: any
    """

    def __init__(
        self,
        current_version: str,
        id_: any,
        leagues: List[VideogameLeague],
        name: any,
        slug: any,
    ):
        self.current_version = self._pattern_matching(
            current_version, "^[0-9]+\.[0-9]+(\.[0-9]+)?$", "current_version"
        )
        self.id_ = id_
        self.leagues = self._define_list(leagues, VideogameLeague)
        self.name = name
        self.slug = slug
