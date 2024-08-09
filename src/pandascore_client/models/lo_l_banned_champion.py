# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class LoLBannedChampion(BaseModel):
    """A team's banned champion

    :param count: count
    :type count: int
    :param name: name
    :type name: str
    """

    def __init__(self, count: int, name: str):
        """A team's banned champion

        :param count: count
        :type count: int
        :param name: name
        :type name: str
        """
        self.count = self._define_number("count", count, ge=0)
        self.name = name