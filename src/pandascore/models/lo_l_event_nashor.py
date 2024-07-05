from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_event_nashor_object import LoLEventNashorObject


class LoLEventNashorType(Enum):
    """An enumeration representing different categories.

    :cvar BARON_NASHOR: "baron_nashor"
    :vartype BARON_NASHOR: str
    """

    BARON_NASHOR = "baron_nashor"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLEventNashorType._member_map_.values()))


@JsonMap({"type_": "type"})
class LoLEventNashor(BaseModel):
    """LoLEventNashor

    :param object: object
    :type object: LoLEventNashorObject
    :param type_: type_
    :type type_: LoLEventNashorType
    """

    def __init__(self, object: LoLEventNashorObject, type_: LoLEventNashorType):
        self.object = self._define_object(object, LoLEventNashorObject)
        self.type_ = self._enum_matching(type_, LoLEventNashorType.list(), "type_")
