# This file was generated by liblab | https://liblab.com/

from enum import Enum


class CsgoWeaponKind(Enum):
    """An enumeration representing different categories.

    :cvar GRENADE: "grenade"
    :vartype GRENADE: str
    :cvar KNIFE: "knife"
    :vartype KNIFE: str
    :cvar PRIMARY: "primary"
    :vartype PRIMARY: str
    :cvar SECONDARY: "secondary"
    :vartype SECONDARY: str
    :cvar TASER: "taser"
    :vartype TASER: str
    """

    GRENADE = "grenade"
    KNIFE = "knife"
    PRIMARY = "primary"
    SECONDARY = "secondary"
    TASER = "taser"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, CsgoWeaponKind._member_map_.values()))
