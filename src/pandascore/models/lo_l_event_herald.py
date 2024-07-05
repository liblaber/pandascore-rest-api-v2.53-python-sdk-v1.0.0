from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_event_herald_object import LoLEventHeraldObject


class LoLEventHeraldType(Enum):
    """An enumeration representing different categories.

    :cvar HERALD: "herald"
    :vartype HERALD: str
    :cvar RIFT_HERALD: "rift_herald"
    :vartype RIFT_HERALD: str
    """

    HERALD = "herald"
    RIFT_HERALD = "rift_herald"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLEventHeraldType._member_map_.values()))


@JsonMap({"type_": "type"})
class LoLEventHerald(BaseModel):
    """LoLEventHerald

    :param object: object
    :type object: LoLEventHeraldObject
    :param type_: type_
    :type type_: LoLEventHeraldType
    """

    def __init__(self, object: LoLEventHeraldObject, type_: LoLEventHeraldType):
        self.object = self._define_object(object, LoLEventHeraldObject)
        self.type_ = self._enum_matching(type_, LoLEventHeraldType.list(), "type_")
