from enum import Enum


class LoLEventNashorValue(Enum):
    """An enumeration representing different categories.

    :cvar BARON_NASHOR: "Baron Nashor"
    :vartype BARON_NASHOR: str
    """

    BARON_NASHOR = "Baron Nashor"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLEventNashorValue._member_map_.values()))
