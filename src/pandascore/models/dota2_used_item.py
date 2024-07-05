from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class Dota2UsedItem(BaseModel):
    """An item used by a hero

    :param count: count
    :type count: int
    :param id_: id_
    :type id_: int
    :param name: name
    :type name: str
    """

    def __init__(self, count: int, id_: int, name: str):
        self.count = count
        self.id_ = id_
        self.name = self._pattern_matching(name, "^[a-z0-9_-]+$", "name")
