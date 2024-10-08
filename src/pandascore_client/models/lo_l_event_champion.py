# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class LoLEventChampion(BaseModel):
    """LoLEventChampion

    :param id_: id_
    :type id_: int
    :param name: name
    :type name: str
    """

    def __init__(self, id_: int, name: str):
        """LoLEventChampion

        :param id_: id_
        :type id_: int
        :param name: name
        :type name: str
        """
        self.id_ = self._define_number("id_", id_, ge=1)
        self.name = name
