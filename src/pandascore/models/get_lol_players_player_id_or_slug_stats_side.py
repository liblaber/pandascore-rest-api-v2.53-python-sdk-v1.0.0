from enum import Enum


class GetLolPlayersPlayerIdOrSlugStatsSide(Enum):
    """An enumeration representing different categories.

    :cvar BLUE: "blue"
    :vartype BLUE: str
    :cvar RED: "red"
    :vartype RED: str
    """

    BLUE = "blue"
    RED = "red"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                GetLolPlayersPlayerIdOrSlugStatsSide._member_map_.values(),
            )
        )
