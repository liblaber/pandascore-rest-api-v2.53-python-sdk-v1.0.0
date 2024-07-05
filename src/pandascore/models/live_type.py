from enum import Enum


class LiveType(Enum):
    """An enumeration representing different categories.

    :cvar EVENTS: "events"
    :vartype EVENTS: str
    :cvar FRAMES: "frames"
    :vartype FRAMES: str
    """

    EVENTS = "events"
    FRAMES = "frames"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LiveType._member_map_.values()))
