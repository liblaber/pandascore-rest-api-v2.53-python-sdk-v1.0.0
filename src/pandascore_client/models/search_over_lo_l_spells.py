# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class SearchOverLoLSpells(BaseModel):
    """SearchOverLoLSpells

    :param name: name, defaults to None
    :type name: str, optional
    """

    def __init__(self, name: str = None):
        """SearchOverLoLSpells

        :param name: name, defaults to None
        :type name: str, optional
        """
        if name is not None:
            self.name = name