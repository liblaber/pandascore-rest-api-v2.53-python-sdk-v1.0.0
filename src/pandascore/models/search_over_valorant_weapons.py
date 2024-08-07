from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class SearchOverValorantWeapons(BaseModel):
    """SearchOverValorantWeapons

    :param name: Name of the weapon, defaults to None
    :type name: str, optional
    """

    def __init__(self, name: str = None):
        if name is not None:
            self.name = name
