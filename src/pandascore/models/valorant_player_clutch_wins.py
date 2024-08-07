from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class ValorantPlayerClutchWins(BaseModel):
    """Round wins when the player was the last team member alive

    :param versus_1: Number of clutch wins versus 1 player
    :type versus_1: int
    :param versus_2: Number of clutch wins versus 2 players
    :type versus_2: int
    :param versus_3: Number of clutch wins versus 3 players
    :type versus_3: float
    :param versus_4: Number of clutch wins versus 4 players
    :type versus_4: int
    :param versus_5: Number of clutch wins versus 5 players
    :type versus_5: int
    """

    def __init__(
        self,
        versus_1: int,
        versus_2: int,
        versus_3: float,
        versus_4: int,
        versus_5: int,
    ):
        self.versus_1 = versus_1
        self.versus_2 = versus_2
        self.versus_3 = versus_3
        self.versus_4 = versus_4
        self.versus_5 = versus_5
