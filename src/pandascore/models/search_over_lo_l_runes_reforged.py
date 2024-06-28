# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class SearchOverLoLRunesReforged(BaseModel):
    """SearchOverLoLRunesReforged

    :param name: Name of the rune path, defaults to None
    :type name: str, optional
    """

    def __init__(self, name: str = None):
        if name is not None:
            self.name = name