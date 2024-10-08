# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .videogame_id import VideogameId


@JsonMap({"id_": "id"})
class FilterOverOwPlayers(BaseModel):
    """FilterOverOwPlayers

    :param active: Whether player is active, defaults to None
    :type active: bool, optional
    :param birthday: birthday, defaults to None
    :type birthday: List[str], optional
    :param first_name: first_name, defaults to None
    :type first_name: List[str], optional
    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param last_name: last_name, defaults to None
    :type last_name: List[str], optional
    :param modified_at: modified_at, defaults to None
    :type modified_at: List[str], optional
    :param name: name, defaults to None
    :type name: List[str], optional
    :param nationality: nationality, defaults to None
    :type nationality: List[str], optional
    :param role: role, defaults to None
    :type role: List[str], optional
    :param slug: slug, defaults to None
    :type slug: List[str], optional
    :param team_id: team_id, defaults to None
    :type team_id: List[int], optional
    :param videogame_id: videogame_id, defaults to None
    :type videogame_id: List[VideogameId], optional
    """

    def __init__(
        self,
        active: bool = None,
        birthday: List[str] = None,
        first_name: List[str] = None,
        id_: List[int] = None,
        last_name: List[str] = None,
        modified_at: List[str] = None,
        name: List[str] = None,
        nationality: List[str] = None,
        role: List[str] = None,
        slug: List[str] = None,
        team_id: List[int] = None,
        videogame_id: List[VideogameId] = None,
    ):
        """FilterOverOwPlayers

        :param active: Whether player is active, defaults to None
        :type active: bool, optional
        :param birthday: birthday, defaults to None
        :type birthday: List[str], optional
        :param first_name: first_name, defaults to None
        :type first_name: List[str], optional
        :param id_: id_, defaults to None
        :type id_: List[int], optional
        :param last_name: last_name, defaults to None
        :type last_name: List[str], optional
        :param modified_at: modified_at, defaults to None
        :type modified_at: List[str], optional
        :param name: name, defaults to None
        :type name: List[str], optional
        :param nationality: nationality, defaults to None
        :type nationality: List[str], optional
        :param role: role, defaults to None
        :type role: List[str], optional
        :param slug: slug, defaults to None
        :type slug: List[str], optional
        :param team_id: team_id, defaults to None
        :type team_id: List[int], optional
        :param videogame_id: videogame_id, defaults to None
        :type videogame_id: List[VideogameId], optional
        """
        if active is not None:
            self.active = active
        if birthday is not None:
            self.birthday = birthday
        if first_name is not None:
            self.first_name = first_name
        if id_ is not None:
            self.id_ = id_
        if last_name is not None:
            self.last_name = last_name
        if modified_at is not None:
            self.modified_at = modified_at
        if name is not None:
            self.name = name
        if nationality is not None:
            self.nationality = nationality
        if role is not None:
            self.role = role
        if slug is not None:
            self.slug = slug
        if team_id is not None:
            self.team_id = team_id
        if videogame_id is not None:
            self.videogame_id = self._define_list(videogame_id, VideogameId)
