# This file was generated by liblab | https://liblab.com/

from enum import Enum


class ValorantTeamSide(Enum):
    """An enumeration representing different categories.

    :cvar ATTACKERS: "attackers"
    :vartype ATTACKERS: str
    :cvar DEFENDERS: "defenders"
    :vartype DEFENDERS: str
    """

    ATTACKERS = "attackers"
    DEFENDERS = "defenders"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ValorantTeamSide._member_map_.values()))
