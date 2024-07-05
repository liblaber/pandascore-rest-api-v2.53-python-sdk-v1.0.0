from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_event_drake_object import LoLEventDrakeObject


class LoLEventDrakeType(Enum):
    """An enumeration representing different categories.

    :cvar DRAKE: "drake"
    :vartype DRAKE: str
    """

    DRAKE = "drake"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLEventDrakeType._member_map_.values()))


@JsonMap({"type_": "type"})
class LoLEventDrake(BaseModel):
    """LoLEventDrake

    :param object: object
    :type object: LoLEventDrakeObject
    :param type_: type_
    :type type_: LoLEventDrakeType
    """

    def __init__(self, object: LoLEventDrakeObject, type_: LoLEventDrakeType):
        self.object = self._define_object(object, LoLEventDrakeObject)
        self.type_ = self._enum_matching(type_, LoLEventDrakeType.list(), "type_")
