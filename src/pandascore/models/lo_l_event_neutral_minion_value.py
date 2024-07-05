from enum import Enum


class LoLEventNeutralMinionValue(Enum):
    """An enumeration representing different categories.

    :cvar BIG_CORBIN: "Big Corbin"
    :vartype BIG_CORBIN: str
    :cvar BIG_GOLEM: "Big Golem"
    :vartype BIG_GOLEM: str
    :cvar BIG_WOLF: "Big Wolf"
    :vartype BIG_WOLF: str
    :cvar BLUE_BUFF: "Blue Buff"
    :vartype BLUE_BUFF: str
    :cvar GROMP: "Gromp"
    :vartype GROMP: str
    :cvar RED_BUFF: "Red Buff"
    :vartype RED_BUFF: str
    :cvar SMALL_CORBIN: "Small Corbin"
    :vartype SMALL_CORBIN: str
    :cvar SMALL_GOLEM: "Small Golem"
    :vartype SMALL_GOLEM: str
    :cvar SMALL_WOLF: "Small Wolf"
    :vartype SMALL_WOLF: str
    """

    BIG_CORBIN = "Big Corbin"
    BIG_GOLEM = "Big Golem"
    BIG_WOLF = "Big Wolf"
    BLUE_BUFF = "Blue Buff"
    GROMP = "Gromp"
    RED_BUFF = "Red Buff"
    SMALL_CORBIN = "Small Corbin"
    SMALL_GOLEM = "Small Golem"
    SMALL_WOLF = "Small Wolf"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, LoLEventNeutralMinionValue._member_map_.values())
        )
