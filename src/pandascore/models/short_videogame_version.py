from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class ShortVideogameVersion(BaseModel):
    """ShortVideogameVersion

    :param current: Whether this videogame version is current
    :type current: bool
    :param name: name
    :type name: str
    """

    def __init__(self, current: bool, name: str):
        self.current = current
        self.name = self._pattern_matching(name, "^[0-9]+\.[0-9]+(\.[0-9]+)?$", "name")
