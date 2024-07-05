from enum import Enum


class LoLEventType(Enum):
    """An enumeration representing different categories.

    :cvar BARON_NASHOR_KILL: "baron_nashor_kill"
    :vartype BARON_NASHOR_KILL: str
    :cvar DRAKE_KILL: "drake_kill"
    :vartype DRAKE_KILL: str
    :cvar INHIBITOR_KILL: "inhibitor_kill"
    :vartype INHIBITOR_KILL: str
    :cvar OTHER: "other"
    :vartype OTHER: str
    :cvar PLAYER_KILL: "player_kill"
    :vartype PLAYER_KILL: str
    :cvar RIFT_HERALD_KILL: "rift_herald_kill"
    :vartype RIFT_HERALD_KILL: str
    :cvar SUICIDE: "suicide"
    :vartype SUICIDE: str
    :cvar TOWER_KILL: "tower_kill"
    :vartype TOWER_KILL: str
    :cvar VOIDGRUB_KILL: "voidgrub_kill"
    :vartype VOIDGRUB_KILL: str
    """

    BARON_NASHOR_KILL = "baron_nashor_kill"
    DRAKE_KILL = "drake_kill"
    INHIBITOR_KILL = "inhibitor_kill"
    OTHER = "other"
    PLAYER_KILL = "player_kill"
    RIFT_HERALD_KILL = "rift_herald_kill"
    SUICIDE = "suicide"
    TOWER_KILL = "tower_kill"
    VOIDGRUB_KILL = "voidgrub_kill"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLEventType._member_map_.values()))
