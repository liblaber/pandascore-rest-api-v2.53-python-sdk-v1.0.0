from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class AbilityType(Enum):
    """An enumeration representing different categories.

    :cvar ABILITY_ONE: "ability_one"
    :vartype ABILITY_ONE: str
    :cvar ABILITY_TWO: "ability_two"
    :vartype ABILITY_TWO: str
    :cvar GRENADE_ABILITY: "grenade_ability"
    :vartype GRENADE_ABILITY: str
    :cvar ULTIMATE_ABILITY: "ultimate_ability"
    :vartype ULTIMATE_ABILITY: str
    """

    ABILITY_ONE = "ability_one"
    ABILITY_TWO = "ability_two"
    GRENADE_ABILITY = "grenade_ability"
    ULTIMATE_ABILITY = "ultimate_ability"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, AbilityType._member_map_.values()))


@JsonMap({"id_": "id"})
class ValorantAbility(BaseModel):
    """ValorantAbility

    :param ability_type: Ability type
    :type ability_type: AbilityType
    :param creds: Credit cost of the ability
    :type creds: float
    :param id_: ID of the ability
    :type id_: int
    :param image_url: URL to an image of the ability
    :type image_url: str
    :param name: Name of the ability
    :type name: str
    :param videogame_versions: Array of of video game versions (ie. patches) for this resource
    :type videogame_versions: List[str]
    """

    def __init__(
        self,
        ability_type: AbilityType,
        creds: float,
        id_: int,
        image_url: str,
        name: str,
        videogame_versions: List[str],
    ):
        self.ability_type = self._enum_matching(
            ability_type, AbilityType.list(), "ability_type"
        )
        self.creds = creds
        self.id_ = id_
        self.image_url = image_url
        self.name = name
        self.videogame_versions = videogame_versions
