# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
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
        self.avg_time_to_charge_ultimate = self._define_number(
            "avg_time_to_charge_ultimate",
            avg_time_to_charge_ultimate,
            nullable=True,
            ge=0,
        )
        self.deaths = self._define_number("deaths", deaths, nullable=True, ge=0)
        self.destructions = self._define_number(
            "destructions", destructions, nullable=True, ge=0
        )
        self.difficulty = self._define_number("difficulty", difficulty, ge=1)
        self.id_ = self._define_number("id_", id_, ge=1)
        self.image_url = image_url
        self.kills = self._define_number("kills", kills, nullable=True, ge=0)
        self.name = name
        self.portrait_url = portrait_url
        self.real_name = real_name
        self.resurrections = self._define_number(
            "resurrections", resurrections, nullable=True, ge=0
        )
        self.role = self._enum_matching(role, OwHeroRole.list(), "role")
        self.slug = self._define_str(
            "slug", slug, pattern="^[a-z0-9_-]+$", min_length=1
        )
        self.time_played = self._define_number(
            "time_played", time_played, nullable=True, ge=0
        )
        self.time_with_ult_up = self._define_number(
            "time_with_ult_up", time_with_ult_up, nullable=True, ge=0
        )
        self.ultimates = self._define_number(
            "ultimates", ultimates, nullable=True, ge=0
        )
