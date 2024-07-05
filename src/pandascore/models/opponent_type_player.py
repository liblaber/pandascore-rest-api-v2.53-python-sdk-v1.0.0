from enum import Enum


class OpponentTypePlayer(Enum):
    """An enumeration representing different categories.

    :cvar PLAYER: "Player"
    :vartype PLAYER: str
    """

    PLAYER = "Player"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, OpponentTypePlayer._member_map_.values()))
