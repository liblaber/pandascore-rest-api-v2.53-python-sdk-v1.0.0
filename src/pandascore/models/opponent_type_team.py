from enum import Enum


class OpponentTypeTeam(Enum):
    """An enumeration representing different categories.

    :cvar TEAM: "Team"
    :vartype TEAM: str
    """

    TEAM = "Team"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, OpponentTypeTeam._member_map_.values()))
