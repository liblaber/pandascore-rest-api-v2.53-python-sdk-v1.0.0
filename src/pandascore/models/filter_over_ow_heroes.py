from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .ow_hero_role import OwHeroRole


@JsonMap({"id_": "id"})
class FilterOverOwHeroes(BaseModel):
    """FilterOverOwHeroes

    :param difficulty: difficulty, defaults to None
    :type difficulty: List[int], optional
    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param name: name, defaults to None
    :type name: List[str], optional
    :param real_name: real_name, defaults to None
    :type real_name: List[str], optional
    :param role: role, defaults to None
    :type role: List[OwHeroRole], optional
    :param slug: slug, defaults to None
    :type slug: List[str], optional
    """

    def __init__(
        self,
        difficulty: List[int] = None,
        id_: List[int] = None,
        name: List[str] = None,
        real_name: List[str] = None,
        role: List[OwHeroRole] = None,
        slug: List[str] = None,
    ):
        if difficulty is not None:
            self.difficulty = difficulty
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if real_name is not None:
            self.real_name = real_name
        if role is not None:
            self.role = self._define_list(role, OwHeroRole)
        if slug is not None:
            self.slug = slug
