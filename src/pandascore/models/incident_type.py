from enum import Enum


class IncidentType(Enum):
    """An enumeration representing different categories.

    :cvar LEAGUE: "league"
    :vartype LEAGUE: str
    :cvar MATCH: "match"
    :vartype MATCH: str
    :cvar PLAYER: "player"
    :vartype PLAYER: str
    :cvar SERIE: "serie"
    :vartype SERIE: str
    :cvar TEAM: "team"
    :vartype TEAM: str
    :cvar TOURNAMENT: "tournament"
    :vartype TOURNAMENT: str
    """

    LEAGUE = "league"
    MATCH = "match"
    PLAYER = "player"
    SERIE = "serie"
    TEAM = "team"
    TOURNAMENT = "tournament"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, IncidentType._member_map_.values()))
