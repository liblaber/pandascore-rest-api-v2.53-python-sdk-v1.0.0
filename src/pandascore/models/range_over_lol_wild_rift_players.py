from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class RangeOverLolWildRiftPlayers(BaseModel):
    """RangeOverLolWildRiftPlayers

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
    """

    def __init__(
        self,
        birthday: List[str] = None,
        first_name: List[str] = None,
        id_: List[int] = None,
        last_name: List[str] = None,
        modified_at: List[str] = None,
        name: List[str] = None,
        nationality: List[str] = None,
        role: List[str] = None,
        slug: List[str] = None,
    ):
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
