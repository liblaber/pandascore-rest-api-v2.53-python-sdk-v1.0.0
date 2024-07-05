from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class FilterOverLoLMasteries(BaseModel):
    """FilterOverLoLMasteries

    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param name: name, defaults to None
    :type name: List[str], optional
    """

    def __init__(self, id_: List[int] = None, name: List[str] = None):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
