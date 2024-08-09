# This file was generated by liblab | https://liblab.com/

from enum import Enum


class LoLEventHeraldValue(Enum):
    """An enumeration representing different categories.

    :cvar RIFTHERALD: "Rift Herald"
    :vartype RIFTHERALD: str
    :cvar RIFTHERALD: "riftherald"
    :vartype RIFTHERALD: str
    """

    RIFTHERALD = "Rift Herald"
    RIFTHERALD = "riftherald"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLEventHeraldValue._member_map_.values()))