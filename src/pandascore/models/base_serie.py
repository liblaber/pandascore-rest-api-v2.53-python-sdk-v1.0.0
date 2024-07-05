from enum import Enum
from typing import Union
from .utils.json_map import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel


class BaseSerieWinnerIdGuard(OneOfBaseModel):
    class_list = {"int": int, "int": int}


BaseSerieWinnerId = Union[int, int]


class BaseSerieWinnerType(Enum):
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
        return list(map(lambda x: x.value, BaseSerieWinnerType._member_map_.values()))


@JsonMap({"id_": "id"})
class BaseSerie(BaseModel):
    """BaseSerie

    :param begin_at: begin_at
    :type begin_at: str
    :param end_at: end_at
    :type end_at: str
    :param full_name: full_name
    :type full_name: str
    :param id_: id_
    :type id_: int
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
    :param winner_id: winner_id
    :type winner_id: BaseSerieWinnerId
    :param winner_type: winner_type
    :type winner_type: BaseSerieWinnerType
    :param year: year
    :type year: int
    """

    def __init__(
        self,
        begin_at: str,
        end_at: str,
        full_name: str,
        id_: int,
        league_id: int,
        modified_at: str,
        name: str,
        season: str,
        slug: str,
        winner_id: BaseSerieWinnerId,
        winner_type: BaseSerieWinnerType,
        year: int,
    ):
        self.begin_at = begin_at
        self.end_at = end_at
        self.full_name = full_name
        self.id_ = id_
        self.league_id = league_id
        self.modified_at = modified_at
        self.name = name
        self.season = season
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
        self.winner_id = BaseSerieWinnerIdGuard.return_one_of(winner_id)
        self.winner_type = self._enum_matching(
            winner_type, BaseSerieWinnerType.list(), "winner_type"
        )
        self.year = year
