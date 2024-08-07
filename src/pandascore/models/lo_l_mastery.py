from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class LoLMastery(BaseModel):
    """LoLMastery

    :param id_: id_
    :type id_: int
    :param name: name
    :type name: str
    """

    def __init__(self, id_: int, name: str):
        self.id_ = id_
        self.name = name
