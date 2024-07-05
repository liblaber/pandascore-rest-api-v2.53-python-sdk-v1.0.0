from enum import Enum


class OwHeroRole(Enum):
    """An enumeration representing different categories.

    :cvar DAMAGE: "damage"
    :vartype DAMAGE: str
    :cvar DEFENSE: "defense"
    :vartype DEFENSE: str
    :cvar OFFENSE: "offense"
    :vartype OFFENSE: str
    :cvar SUPPORT: "support"
    :vartype SUPPORT: str
    :cvar TANK: "tank"
    :vartype TANK: str
    """

    DAMAGE = "damage"
    DEFENSE = "defense"
    OFFENSE = "offense"
    SUPPORT = "support"
    TANK = "tank"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, OwHeroRole._member_map_.values()))
