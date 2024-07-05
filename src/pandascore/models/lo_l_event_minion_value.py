from enum import Enum


class LoLEventMinionValue(Enum):
    """An enumeration representing different categories.

    :cvar MINION: "Minion"
    :vartype MINION: str
    """

    MINION = "Minion"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLEventMinionValue._member_map_.values()))
