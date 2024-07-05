from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_event_voidgrub_object import LoLEventVoidgrubObject


class LoLEventVoidgrubType(Enum):
    """An enumeration representing different categories.

    :cvar VOIDGRUB: "voidgrub"
    :vartype VOIDGRUB: str
    """

    VOIDGRUB = "voidgrub"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLEventVoidgrubType._member_map_.values()))


@JsonMap({"type_": "type"})
class LoLEventVoidgrub(BaseModel):
    """LoLEventVoidgrub

    :param object: object
    :type object: LoLEventVoidgrubObject
    :param type_: type_
    :type type_: LoLEventVoidgrubType
    """

    def __init__(self, object: LoLEventVoidgrubObject, type_: LoLEventVoidgrubType):
        self.object = self._define_object(object, LoLEventVoidgrubObject)
        self.type_ = self._enum_matching(type_, LoLEventVoidgrubType.list(), "type_")
