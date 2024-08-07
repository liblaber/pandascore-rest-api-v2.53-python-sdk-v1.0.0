from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class LoLBannedChampion(BaseModel):
    """A team's banned champion

    :param count: count
    :type count: int
    :param name: name
    :type name: str
    """

    def __init__(self, count: int, name: str):
        self.count = count
        self.name = name
