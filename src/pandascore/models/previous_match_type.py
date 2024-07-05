from enum import Enum


class PreviousMatchType(Enum):
    """An enumeration representing different categories.

    :cvar LOSER: "loser"
    :vartype LOSER: str
    :cvar WINNER: "winner"
    :vartype WINNER: str
    """

    LOSER = "loser"
    WINNER = "winner"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, PreviousMatchType._member_map_.values()))
