from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_weapon_kind import CsgoWeaponKind


@JsonMap({"id_": "id"})
class FilterOverCsgoWeapons(BaseModel):
    """FilterOverCsgoWeapons

    :param ammo_clip_max: ammo_clip_max, defaults to None
    :type ammo_clip_max: List[int], optional
    :param ammo_max: ammo_max, defaults to None
    :type ammo_max: List[int], optional
    :param cost: cost, defaults to None
    :type cost: List[int], optional
    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param kill_reward: kill_reward, defaults to None
    :type kill_reward: List[int], optional
    :param kind: kind, defaults to None
    :type kind: List[CsgoWeaponKind], optional
    :param name: name, defaults to None
    :type name: List[str], optional
    :param slug: slug, defaults to None
    :type slug: List[str], optional
    """

    def __init__(
        self,
        ammo_clip_max: List[int] = None,
        ammo_max: List[int] = None,
        cost: List[int] = None,
        id_: List[int] = None,
        kill_reward: List[int] = None,
        kind: List[CsgoWeaponKind] = None,
        name: List[str] = None,
        slug: List[str] = None,
    ):
        if ammo_clip_max is not None:
            self.ammo_clip_max = ammo_clip_max
        if ammo_max is not None:
            self.ammo_max = ammo_max
        if cost is not None:
            self.cost = cost
        if id_ is not None:
            self.id_ = id_
        if kill_reward is not None:
            self.kill_reward = kill_reward
        if kind is not None:
            self.kind = self._define_list(kind, CsgoWeaponKind)
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = slug
