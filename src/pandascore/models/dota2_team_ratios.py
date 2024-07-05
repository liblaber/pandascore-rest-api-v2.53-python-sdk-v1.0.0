from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class Dota2TeamRatios(BaseModel):
    """Dota2TeamRatios

    :param first_blood: first_blood
    :type first_blood: float
    :param win: win
    :type win: float
    """

    def __init__(self, first_blood: float, win: float):
        self.first_blood = first_blood
        self.win = win
