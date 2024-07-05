from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_drake_name import LoLDrakeName
from .lo_l_drake_type import LoLDrakeType


@JsonMap({"type_": "type"})
class LoLEventDrakeObject(BaseModel):
    """LoLEventDrakeObject

    :param name: name
    :type name: LoLDrakeName
    :param type_: type_
    :type type_: LoLDrakeType
    """

    def __init__(self, name: LoLDrakeName, type_: LoLDrakeType):
        self.name = self._enum_matching(name, LoLDrakeName.list(), "name")
        self.type_ = self._enum_matching(type_, LoLDrakeType.list(), "type_")
