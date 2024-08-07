from enum import Enum


class CsgoEventType(Enum):
    """An enumeration representing different categories.

    :cvar KILL: "kill"
    :vartype KILL: str
    :cvar ROUND_END: "round_end"
    :vartype ROUND_END: str
    :cvar ROUND_START: "round_start"
    :vartype ROUND_START: str
    """

    KILL = "kill"
    ROUND_END = "round_end"
    ROUND_START = "round_start"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, CsgoEventType._member_map_.values()))
