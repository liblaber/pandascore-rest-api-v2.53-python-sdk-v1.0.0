from enum import Enum


class GameStatus(Enum):
    """An enumeration representing different categories.

    :cvar FINISHED: "finished"
    :vartype FINISHED: str
    :cvar NOT_PLAYED: "not_played"
    :vartype NOT_PLAYED: str
    :cvar NOT_STARTED: "not_started"
    :vartype NOT_STARTED: str
    :cvar RUNNING: "running"
    :vartype RUNNING: str
    """

    FINISHED = "finished"
    NOT_PLAYED = "not_played"
    NOT_STARTED = "not_started"
    RUNNING = "running"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, GameStatus._member_map_.values()))
