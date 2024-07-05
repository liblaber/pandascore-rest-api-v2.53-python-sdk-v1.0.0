from enum import Enum


class LoLEventHeraldValue(Enum):
    """An enumeration representing different categories.

    :cvar RIFT_HERALD: "Rift Herald"
    :vartype RIFT_HERALD: str
    :cvar RIFTHERALD: "riftherald"
    :vartype RIFTHERALD: str
    """

    RIFT_HERALD = "Rift Herald"
    RIFTHERALD = "riftherald"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLEventHeraldValue._member_map_.values()))
