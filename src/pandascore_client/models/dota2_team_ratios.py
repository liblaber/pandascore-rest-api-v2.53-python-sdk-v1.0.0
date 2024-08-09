# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class Dota2TeamRatios(BaseModel):
    """Dota2TeamRatios

    :param first_blood: first_blood
    :type first_blood: float
    :param win: win
    :type win: float
    """

    def __init__(self, first_blood: float, win: float):
        """Dota2TeamRatios

        :param first_blood: first_blood
        :type first_blood: float
        :param win: win
        :type win: float
        """
        self.first_blood = self._define_number(
            "first_blood", first_blood, nullable=True, ge=0, le=1
        )
        self.win = self._define_number("win", win, nullable=True, ge=0, le=1)