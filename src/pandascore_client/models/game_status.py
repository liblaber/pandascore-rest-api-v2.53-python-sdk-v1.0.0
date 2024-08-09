# This file was generated by liblab | https://liblab.com/

from enum import Enum


class GameStatus(Enum):
    """An enumeration representing different categories.

    :cvar FINISHED: "finished"
    :vartype FINISHED: str
    :cvar NOTPLAYED: "not_played"
    :vartype NOTPLAYED: str
    :cvar NOTSTARTED: "not_started"
    :vartype NOTSTARTED: str
    :cvar RUNNING: "running"
    :vartype RUNNING: str
    """

    FINISHED = "finished"
    NOTPLAYED = "not_played"
    NOTSTARTED = "not_started"
    RUNNING = "running"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, GameStatus._member_map_.values()))