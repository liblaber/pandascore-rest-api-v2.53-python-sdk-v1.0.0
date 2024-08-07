from enum import Enum


class ValorantGameRoundOutcome(Enum):
    """An enumeration representing different categories.

    :cvar ATTACK_TIMEOUT: "attack_timeout"
    :vartype ATTACK_TIMEOUT: str
    :cvar ATTACKERS_ELIMINATED: "attackers_eliminated"
    :vartype ATTACKERS_ELIMINATED: str
    :cvar DEFENDERS_ELIMINATED: "defenders_eliminated"
    :vartype DEFENDERS_ELIMINATED: str
    :cvar SPIKE_DEFUSED: "spike_defused"
    :vartype SPIKE_DEFUSED: str
    :cvar SPIKE_EXPLODED: "spike_exploded"
    :vartype SPIKE_EXPLODED: str
    """

    ATTACK_TIMEOUT = "attack_timeout"
    ATTACKERS_ELIMINATED = "attackers_eliminated"
    DEFENDERS_ELIMINATED = "defenders_eliminated"
    SPIKE_DEFUSED = "spike_defused"
    SPIKE_EXPLODED = "spike_exploded"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, ValorantGameRoundOutcome._member_map_.values())
        )
