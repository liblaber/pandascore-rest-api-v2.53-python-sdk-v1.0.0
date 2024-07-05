from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .videogame_id import VideogameId


@JsonMap({"id_": "id"})
class FilterOverStarcraft2Teams(BaseModel):
    """FilterOverStarcraft2Teams

    :param acronym: acronym, defaults to None
    :type acronym: List[str], optional
    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param location: location, defaults to None
    :type location: List[str], optional
    :param modified_at: modified_at, defaults to None
    :type modified_at: List[str], optional
    :param name: name, defaults to None
    :type name: List[str], optional
    :param slug: slug, defaults to None
    :type slug: List[str], optional
    :param videogame_id: videogame_id, defaults to None
    :type videogame_id: List[VideogameId], optional
    """

    def __init__(
        self,
        acronym: List[str] = None,
        id_: List[int] = None,
        location: List[str] = None,
        modified_at: List[str] = None,
        name: List[str] = None,
        slug: List[str] = None,
        videogame_id: List[VideogameId] = None,
    ):
        if acronym is not None:
            self.acronym = acronym
        if id_ is not None:
            self.id_ = id_
        if location is not None:
            self.location = location
        if modified_at is not None:
            self.modified_at = modified_at
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = slug
        if videogame_id is not None:
            self.videogame_id = self._define_list(videogame_id, VideogameId)
