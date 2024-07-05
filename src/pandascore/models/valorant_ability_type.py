from enum import Enum


class ValorantAbilityType(Enum):
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
        return list(map(lambda x: x.value, ValorantAbilityType._member_map_.values()))
