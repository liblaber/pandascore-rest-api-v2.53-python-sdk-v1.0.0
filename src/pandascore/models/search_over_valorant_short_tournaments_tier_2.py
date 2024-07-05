from enum import Enum


class SearchOverValorantShortTournamentsTier2(Enum):
    """An enumeration representing different categories.

    :cvar A: "a"
    :vartype A: str
    :cvar B: "b"
    :vartype B: str
    :cvar C: "c"
    :vartype C: str
    :cvar D: "d"
    :vartype D: str
    :cvar S: "s"
    :vartype S: str
    :cvar UNRANKED: "unranked"
    :vartype UNRANKED: str
    """

    A = "a"
    B = "b"
    C = "c"
    D = "d"
    S = "s"
    UNRANKED = "unranked"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                SearchOverValorantShortTournamentsTier2._member_map_.values(),
            )
        )
