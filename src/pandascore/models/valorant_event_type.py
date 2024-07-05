from enum import Enum


class ValorantEventType(Enum):
    """An enumeration representing different categories.

    :cvar KILL: "kill"
    :vartype KILL: str
    :cvar SPIKE_DEFUSED: "spike_defused"
    :vartype SPIKE_DEFUSED: str
    :cvar SPIKE_PLANTED: "spike_planted"
    :vartype SPIKE_PLANTED: str
    """

    KILL = "kill"
    SPIKE_DEFUSED = "spike_defused"
    SPIKE_PLANTED = "spike_planted"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ValorantEventType._member_map_.values()))
