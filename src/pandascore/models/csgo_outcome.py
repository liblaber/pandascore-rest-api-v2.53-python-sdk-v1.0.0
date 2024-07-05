from enum import Enum


class CsgoOutcome(Enum):
    """An enumeration representing different categories.

    :cvar DEFUSED: "defused"
    :vartype DEFUSED: str
    :cvar ELIMINATED: "eliminated"
    :vartype ELIMINATED: str
    :cvar EXPLODED: "exploded"
    :vartype EXPLODED: str
    :cvar PLANTED_ELIMINATED: "planted_eliminated"
    :vartype PLANTED_ELIMINATED: str
    :cvar TIMEOUT: "timeout"
    :vartype TIMEOUT: str
    """

    DEFUSED = "defused"
    ELIMINATED = "eliminated"
    EXPLODED = "exploded"
    PLANTED_ELIMINATED = "planted_eliminated"
    TIMEOUT = "timeout"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, CsgoOutcome._member_map_.values()))
