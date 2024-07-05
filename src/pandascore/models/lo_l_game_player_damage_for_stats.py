from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class LoLGamePlayerDamageForStats(BaseModel):
    """LoLGamePlayerDamageForStats

    :param dealt: dealt
    :type dealt: int
    :param dealt_to_champions: dealt_to_champions
    :type dealt_to_champions: int
    :param taken: taken
    :type taken: int
    """

    def __init__(self, dealt: int, dealt_to_champions: int, taken: int):
        self.dealt = dealt
        self.dealt_to_champions = dealt_to_champions
        self.taken = taken
