from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class Dota2BannedHero(BaseModel):
    """Dota2BannedHero

    :param count: count
    :type count: int
    :param name: name
    :type name: str
    """

    def __init__(self, count: int, name: str):
        self.count = count
        self.name = self._pattern_matching(name, "^[a-z0-9_-]+$", "name")
