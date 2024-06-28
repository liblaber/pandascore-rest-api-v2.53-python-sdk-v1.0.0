# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import Union
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .base_league import BaseLeague
from .base_tournament import BaseTournament
from .videogame_id import VideogameId


@JsonMap({"id_": "id"})
class SerieVideogameTitle(BaseModel):
    """SerieVideogameTitle

    :param id_: id_
    :type id_: int
    :param name: name
    :type name: str
    :param slug: slug
    :type slug: str
    :param videogame_id: A videogame ID
    :type videogame_id: VideogameId
    """

    def __init__(self, id_: int, name: str, slug: str, videogame_id: VideogameId):
        self.id_ = id_
        self.name = name
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
        self.videogame_id = self._enum_matching(
            videogame_id, VideogameId.list(), "videogame_id"
        )


class SerieWinnerIdGuard(OneOfBaseModel):
    class_list = {"int": int, "int": int}


SerieWinnerId = Union[int, int]


class SerieWinnerType(Enum):
    """An enumeration representing different categories.

    :cvar PLAYER: "Player"
    :vartype PLAYER: str
    :cvar TEAM: "Team"
    :vartype TEAM: str
    """

    PLAYER = "Player"
    TEAM = "Team"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, SerieWinnerType._member_map_.values()))


@JsonMap({"id_": "id"})
class Serie(BaseModel):
    """A serie, an occurrence of a league event

    :param begin_at: begin_at
    :type begin_at: str
    :param end_at: end_at
    :type end_at: str
    :param full_name: full_name
    :type full_name: str
    :param id_: id_
    :type id_: int
    :param league: league
    :type league: BaseLeague
    :param league_id: league_id
    :type league_id: int
    :param modified_at: modified_at
    :type modified_at: str
    :param name: name
    :type name: str
    :param season: season
    :type season: str
    :param slug: slug
    :type slug: str
    :param tournaments: tournaments
    :type tournaments: List[BaseTournament]
    :param videogame: videogame
    :type videogame: dict
    :param videogame_title: videogame_title
    :type videogame_title: SerieVideogameTitle
    :param winner_id: winner_id
    :type winner_id: SerieWinnerId
    :param winner_type: winner_type
    :type winner_type: SerieWinnerType
    :param year: year
    :type year: int
    """

    def __init__(
        self,
        begin_at: str,
        end_at: str,
        full_name: str,
        id_: int,
        league: BaseLeague,
        league_id: int,
        modified_at: str,
        name: str,
        season: str,
        slug: str,
        tournaments: List[BaseTournament],
        videogame: dict,
        videogame_title: SerieVideogameTitle,
        winner_id: SerieWinnerId,
        winner_type: SerieWinnerType,
        year: int,
    ):
        self.begin_at = begin_at
        self.end_at = end_at
        self.full_name = full_name
        self.id_ = id_
        self.league = self._define_object(league, BaseLeague)
        self.league_id = league_id
        self.modified_at = modified_at
        self.name = name
        self.season = season
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
        self.tournaments = self._define_list(tournaments, BaseTournament)
        self.videogame = videogame
        self.videogame_title = self._define_object(videogame_title, SerieVideogameTitle)
        self.winner_id = SerieWinnerIdGuard.return_one_of(winner_id)
        self.winner_type = self._enum_matching(
            winner_type, SerieWinnerType.list(), "winner_type"
        )
        self.year = year
