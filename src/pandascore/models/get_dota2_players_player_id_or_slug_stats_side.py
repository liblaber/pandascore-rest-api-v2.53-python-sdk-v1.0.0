from enum import Enum


class GetDota2PlayersPlayerIdOrSlugStatsSide(Enum):
    """An enumeration representing different categories.

    :cvar RADIANT: "radiant"
    :vartype RADIANT: str
    :cvar DIRE: "dire"
    :vartype DIRE: str
    """

    RADIANT = "radiant"
    DIRE = "dire"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                GetDota2PlayersPlayerIdOrSlugStatsSide._member_map_.values(),
            )
        )
