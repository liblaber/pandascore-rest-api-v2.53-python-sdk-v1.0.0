from enum import Enum


class ValorantPlayerShield(Enum):
    """An enumeration representing different categories.

    :cvar HEAVY_SHIELD: "heavy_shield"
    :vartype HEAVY_SHIELD: str
    :cvar LIGHT_SHIELD: "light_shield"
    :vartype LIGHT_SHIELD: str
    :cvar NO_SHIELD: "no_shield"
    :vartype NO_SHIELD: str
    """

    HEAVY_SHIELD = "heavy_shield"
    LIGHT_SHIELD = "light_shield"
    NO_SHIELD = "no_shield"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ValorantPlayerShield._member_map_.values()))
