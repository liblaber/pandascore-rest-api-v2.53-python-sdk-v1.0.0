from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_full_round_utility import CsgoFullRoundUtility


class Armor(Enum):
    """An enumeration representing different categories.

    :cvar KEVLAR: "kevlar"
    :vartype KEVLAR: str
    :cvar KEVLAR_AND_HELMET: "kevlar_and_helmet"
    :vartype KEVLAR_AND_HELMET: str
    """

    KEVLAR = "kevlar"
    KEVLAR_AND_HELMET = "kevlar_and_helmet"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Armor._member_map_.values()))


@JsonMap({"id_": "id"})
class PrimaryWeapon(BaseModel):
    """PrimaryWeapon

    :param id_: id_
    :type id_: int
    :param image_url: A URL to the image of the weapon.
    :type image_url: str
    :param name: name
    :type name: str
    :param slug: The slug of the weapon.
    :type slug: str
    """

    def __init__(self, id_: int, image_url: str, name: str, slug: str):
        self.id_ = id_
        self.image_url = image_url
        self.name = name
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")


@JsonMap({"id_": "id"})
class SecondaryWeapon(BaseModel):
    """SecondaryWeapon

    :param id_: id_
    :type id_: int
    :param image_url: A URL to the image of the weapon.
    :type image_url: str
    :param name: name
    :type name: str
    :param slug: The slug of the weapon.
    :type slug: str
    """

    def __init__(self, id_: int, image_url: str, name: str, slug: str):
        self.id_ = id_
        self.image_url = image_url
        self.name = name
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")


@JsonMap({})
class CsgoFullRoundPlayerEconomy(BaseModel):
    """CsgoFullRoundPlayerEconomy

    :param armor: armor
    :type armor: Armor
    :param defuse_kit: Whether the player carries a defuse kit, defaults to None
    :type defuse_kit: bool, optional
    :param economy: The in-game money that a player has.
    :type economy: int
    :param primary_weapon: primary_weapon
    :type primary_weapon: PrimaryWeapon
    :param secondary_weapon: secondary_weapon
    :type secondary_weapon: SecondaryWeapon
    :param utilities: utilities
    :type utilities: List[CsgoFullRoundUtility]
    """

    def __init__(
        self,
        armor: Armor,
        economy: int,
        primary_weapon: PrimaryWeapon,
        secondary_weapon: SecondaryWeapon,
        utilities: List[CsgoFullRoundUtility],
        defuse_kit: bool = None,
    ):
        self.armor = self._enum_matching(armor, Armor.list(), "armor")
        if defuse_kit is not None:
            self.defuse_kit = defuse_kit
        self.economy = economy
        self.primary_weapon = self._define_object(primary_weapon, PrimaryWeapon)
        self.secondary_weapon = self._define_object(secondary_weapon, SecondaryWeapon)
        self.utilities = self._define_list(utilities, CsgoFullRoundUtility)
