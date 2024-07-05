from enum import Enum


class MatchType(Enum):
    """An enumeration representing different categories.

    :cvar ALL_GAMES_PLAYED: "all_games_played"
    :vartype ALL_GAMES_PLAYED: str
    :cvar BEST_OF: "best_of"
    :vartype BEST_OF: str
    :cvar CUSTOM: "custom"
    :vartype CUSTOM: str
    :cvar FIRST_TO: "first_to"
    :vartype FIRST_TO: str
    :cvar OW_BEST_OF: "ow_best_of"
    :vartype OW_BEST_OF: str
    :cvar RED_BULL_HOME_GROUND: "red_bull_home_ground"
    :vartype RED_BULL_HOME_GROUND: str
    """

    ALL_GAMES_PLAYED = "all_games_played"
    BEST_OF = "best_of"
    CUSTOM = "custom"
    FIRST_TO = "first_to"
    OW_BEST_OF = "ow_best_of"
    RED_BULL_HOME_GROUND = "red_bull_home_ground"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, MatchType._member_map_.values()))
