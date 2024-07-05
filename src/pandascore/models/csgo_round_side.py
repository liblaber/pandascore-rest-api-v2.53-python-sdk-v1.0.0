from enum import Enum


class CsgoRoundSide(Enum):
    """An enumeration representing different categories.

    :cvar COUNTER_TERRORISTS: "counter_terrorists"
    :vartype COUNTER_TERRORISTS: str
    :cvar TERRORISTS: "terrorists"
    :vartype TERRORISTS: str
    """

    COUNTER_TERRORISTS = "counter_terrorists"
    TERRORISTS = "terrorists"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, CsgoRoundSide._member_map_.values()))
