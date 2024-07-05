from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "_2_kills": "2_kills",
        "_3_kills": "3_kills",
        "_4_kills": "4_kills",
        "_5_kills": "5_kills",
    }
)
class ValorantTeamStreaks(BaseModel):
    """Streaks done by a team member (in a given round)

    :param _2_kills: Number of 2-player kill streaks
    :type _2_kills: int
    :param _3_kills: Number of 3-player kill streaks
    :type _3_kills: int
    :param _4_kills: Number of 4-player kill streaks
    :type _4_kills: int
    :param _5_kills: Number of 3-player kill streaks
    :type _5_kills: int
    """

    def __init__(self, _2_kills: int, _3_kills: int, _4_kills: int, _5_kills: int):
        self._2_kills = _2_kills
        self._3_kills = _3_kills
        self._4_kills = _4_kills
        self._5_kills = _5_kills
