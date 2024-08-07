from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class LoLUsedItem(BaseModel):
    """An item used by a champion

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
        self.name = name
