from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_rune_reforged_type import LoLRuneReforgedType


@JsonMap({"id_": "id", "type_": "type"})
class LoLRuneReforged(BaseModel):
    """LoLRuneReforged

    :param id_: ID of the rune
    :type id_: int
    :param image_url: URL to an image of the rune
    :type image_url: str
    :param name: Name of the rune path
    :type name: str
    :param type_: type_
    :type type_: LoLRuneReforgedType
    """

    def __init__(self, id_: int, image_url: str, name: str, type_: LoLRuneReforgedType):
        self.id_ = id_
        self.image_url = image_url
        self.name = name
        self.type_ = self._enum_matching(type_, LoLRuneReforgedType.list(), "type_")
