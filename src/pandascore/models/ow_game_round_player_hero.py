from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .ow_hero_role import OwHeroRole


@JsonMap({"id_": "id"})
class OwGameRoundPlayerHero(BaseModel):
    """OwGameRoundPlayerHero

    :param avg_time_to_charge_ultimate: avg_time_to_charge_ultimate
    :type avg_time_to_charge_ultimate: int
    :param deaths: deaths
    :type deaths: int
    :param destructions: destructions
    :type destructions: int
    :param difficulty: difficulty
    :type difficulty: int
    :param id_: id_
    :type id_: int
    :param image_url: image_url
    :type image_url: str
    :param kills: kills
    :type kills: int
    :param name: name
    :type name: str
    :param portrait_url: portrait_url
    :type portrait_url: str
    :param real_name: real_name
    :type real_name: str
    :param resurrections: resurrections
    :type resurrections: int
    :param role: role
    :type role: OwHeroRole
    :param slug: slug
    :type slug: str
    :param time_played: time_played
    :type time_played: int
    :param time_with_ult_up: time_with_ult_up
    :type time_with_ult_up: int
    :param ultimates: ultimates
    :type ultimates: int
    """

    def __init__(
        self,
        avg_time_to_charge_ultimate: int,
        deaths: int,
        destructions: int,
        difficulty: int,
        id_: int,
        image_url: str,
        kills: int,
        name: str,
        portrait_url: str,
        real_name: str,
        resurrections: int,
        role: OwHeroRole,
        slug: str,
        time_played: int,
        time_with_ult_up: int,
        ultimates: int,
    ):
        self.avg_time_to_charge_ultimate = avg_time_to_charge_ultimate
        self.deaths = deaths
        self.destructions = destructions
        self.difficulty = difficulty
        self.id_ = id_
        self.image_url = image_url
        self.kills = kills
        self.name = name
        self.portrait_url = portrait_url
        self.real_name = real_name
        self.resurrections = resurrections
        self.role = self._enum_matching(role, OwHeroRole.list(), "role")
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
        self.time_played = time_played
        self.time_with_ult_up = time_with_ult_up
        self.ultimates = ultimates
