from enum import Enum


class Dota2Faction(Enum):
    """An enumeration representing different categories.

    :cvar DIRE: "dire"
    :vartype DIRE: str
    :cvar RADIANT: "radiant"
    :vartype RADIANT: str
    """

    DIRE = "dire"
    RADIANT = "radiant"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Dota2Faction._member_map_.values()))
