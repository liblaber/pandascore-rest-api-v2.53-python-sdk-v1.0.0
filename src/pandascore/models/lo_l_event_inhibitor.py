from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_event_inhibitor_object import LoLEventInhibitorObject


class LoLEventInhibitorType(Enum):
    """An enumeration representing different categories.

    :cvar INHIBITOR: "inhibitor"
    :vartype INHIBITOR: str
    """

    INHIBITOR = "inhibitor"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLEventInhibitorType._member_map_.values()))


@JsonMap({"type_": "type"})
class LoLEventInhibitor(BaseModel):
    """LoLEventInhibitor

    :param object: object
    :type object: LoLEventInhibitorObject
    :param type_: type_
    :type type_: LoLEventInhibitorType
    """

    def __init__(self, object: LoLEventInhibitorObject, type_: LoLEventInhibitorType):
        self.object = self._define_object(object, LoLEventInhibitorObject)
        self.type_ = self._enum_matching(type_, LoLEventInhibitorType.list(), "type_")
