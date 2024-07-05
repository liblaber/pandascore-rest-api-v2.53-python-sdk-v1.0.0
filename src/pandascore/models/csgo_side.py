from enum import Enum


class CsgoSide(Enum):
    """An enumeration representing different categories.

    :cvar CT: "ct"
    :vartype CT: str
    :cvar TERRORISTS: "terrorists"
    :vartype TERRORISTS: str
    """

    CT = "ct"
    TERRORISTS = "terrorists"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, CsgoSide._member_map_.values()))
