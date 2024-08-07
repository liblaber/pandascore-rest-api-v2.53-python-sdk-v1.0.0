from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .ow_hero_role import OwHeroRole


@JsonMap({})
class SearchOverOwHeroes(BaseModel):
    """SearchOverOwHeroes

    :param name: name, defaults to None
    :type name: str, optional
    :param real_name: real_name, defaults to None
    :type real_name: str, optional
    :param role: role, defaults to None
    :type role: OwHeroRole, optional
    :param slug: slug, defaults to None
    :type slug: str, optional
    """

    def __init__(
        self,
        name: str = None,
        real_name: str = None,
        role: OwHeroRole = None,
        slug: str = None,
    ):
        if name is not None:
            self.name = name
        if real_name is not None:
            self.real_name = real_name
        if role is not None:
            self.role = self._enum_matching(role, OwHeroRole.list(), "role")
        if slug is not None:
            self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
