# This file was generated by liblab | https://liblab.com/

from enum import Enum


class OwMapGameMode(Enum):
    """An enumeration representing different categories.

    :cvar ASSAULT: "Assault"
    :vartype ASSAULT: str
    :cvar CONTROL: "Control"
    :vartype CONTROL: str
    :cvar ESCORT: "Escort"
    :vartype ESCORT: str
    :cvar HYBRID: "Hybrid"
    :vartype HYBRID: str
    :cvar PUSH: "Push"
    :vartype PUSH: str
    """

    ASSAULT = "Assault"
    CONTROL = "Control"
    ESCORT = "Escort"
    HYBRID = "Hybrid"
    PUSH = "Push"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, OwMapGameMode._member_map_.values()))
