# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class LoLPlayerTotalKillCounters(BaseModel):
    """LoLPlayerTotalKillCounters

    :param inhibitors: Number of inhibitors killed by the player
    :type inhibitors: int
    :param turrets: Number of turrets killed
    :type turrets: int
    :param wards: Number of wards killed by the player
    :type wards: int
    """

    def __init__(self, inhibitors: int, turrets: int, wards: int):
        """LoLPlayerTotalKillCounters

        :param inhibitors: Number of inhibitors killed by the player
        :type inhibitors: int
        :param turrets: Number of turrets killed
        :type turrets: int
        :param wards: Number of wards killed by the player
        :type wards: int
        """
        self.inhibitors = self._define_number(
            "inhibitors", inhibitors, nullable=True, ge=0
        )
        self.turrets = self._define_number("turrets", turrets, nullable=True, ge=0)
        self.wards = self._define_number("wards", wards, nullable=True, ge=0)
