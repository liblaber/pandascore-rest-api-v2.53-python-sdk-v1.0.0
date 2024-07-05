from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_weapon_kind import CsgoWeaponKind


@JsonMap({})
class SearchOverCsgoWeapons(BaseModel):
    """SearchOverCsgoWeapons

    :param kind: kind, defaults to None
    :type kind: CsgoWeaponKind, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param slug: The slug of the weapon., defaults to None
    :type slug: str, optional
    """

    def __init__(self, kind: CsgoWeaponKind = None, name: str = None, slug: str = None):
        if kind is not None:
            self.kind = self._enum_matching(kind, CsgoWeaponKind.list(), "kind")
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
