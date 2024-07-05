from .utils.json_map import JsonMap
from .base import BaseModel


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
        self.inhibitors = inhibitors
        self.turrets = turrets
        self.wards = wards
