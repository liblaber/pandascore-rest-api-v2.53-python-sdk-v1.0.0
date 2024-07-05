from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_weapon_kind import CsgoWeaponKind


@JsonMap({"id_": "id"})
class CsgoWeapon(BaseModel):
    """CsgoWeapon

    :param ammo_clip_max: ammo_clip_max
    :type ammo_clip_max: int
    :param ammo_max: ammo_max
    :type ammo_max: int
    :param cost: cost
    :type cost: int
    :param id_: id_
    :type id_: int
    :param image_url: A URL to the image of the weapon.
    :type image_url: str
    :param kill_reward: kill_reward
    :type kill_reward: int
    :param kind: kind
    :type kind: CsgoWeaponKind
    :param name: name
    :type name: str
    :param slug: The slug of the weapon.
    :type slug: str
    """

    def __init__(
        self,
        ammo_clip_max: int,
        ammo_max: int,
        cost: int,
        id_: int,
        image_url: str,
        kill_reward: int,
        kind: CsgoWeaponKind,
        name: str,
        slug: str,
    ):
        self.ammo_clip_max = ammo_clip_max
        self.ammo_max = ammo_max
        self.cost = cost
        self.id_ = id_
        self.image_url = image_url
        self.kill_reward = kill_reward
        self.kind = self._enum_matching(kind, CsgoWeaponKind.list(), "kind")
        self.name = name
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
