from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .ow_hero_role import OwHeroRole


@JsonMap({"id_": "id"})
class OwHero(BaseModel):
    """OwHero

    :param difficulty: difficulty
    :type difficulty: int
    :param id_: id_
    :type id_: int
    :param image_url: image_url
    :type image_url: str
    :param name: name
    :type name: str
    :param portrait_url: portrait_url
    :type portrait_url: str
    :param real_name: real_name
    :type real_name: str
    :param role: role
    :type role: OwHeroRole
    :param slug: slug
    :type slug: str
    """

    def __init__(
        self,
        difficulty: int,
        id_: int,
        image_url: str,
        name: str,
        portrait_url: str,
        real_name: str,
        role: OwHeroRole,
        slug: str,
    ):
        self.difficulty = difficulty
        self.id_ = id_
        self.image_url = image_url
        self.name = name
        self.portrait_url = portrait_url
        self.real_name = real_name
        self.role = self._enum_matching(role, OwHeroRole.list(), "role")
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
