from enum import Enum


class MatchStatus(Enum):
    """An enumeration representing different categories.

    :cvar CANCELED: "canceled"
    :vartype CANCELED: str
    :cvar FINISHED: "finished"
    :vartype FINISHED: str
    :cvar NOT_STARTED: "not_started"
    :vartype NOT_STARTED: str
    :cvar POSTPONED: "postponed"
    :vartype POSTPONED: str
    :cvar RUNNING: "running"
    :vartype RUNNING: str
    """

    CANCELED = "canceled"
    FINISHED = "finished"
    NOT_STARTED = "not_started"
    POSTPONED = "postponed"
    RUNNING = "running"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, MatchStatus._member_map_.values()))
