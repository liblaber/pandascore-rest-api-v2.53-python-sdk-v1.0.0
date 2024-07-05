from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_event_minion_object import LoLEventMinionObject


class LoLEventMinionType(Enum):
    """An enumeration representing different categories.

    :cvar MINION: "minion"
    :vartype MINION: str
    """

    MINION = "minion"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLEventMinionType._member_map_.values()))


@JsonMap({"type_": "type"})
class LoLEventMinion(BaseModel):
    """LoLEventMinion

    :param object: object
    :type object: LoLEventMinionObject
    :param type_: type_
    :type type_: LoLEventMinionType
    """

    def __init__(self, object: LoLEventMinionObject, type_: LoLEventMinionType):
        self.object = self._define_object(object, LoLEventMinionObject)
        self.type_ = self._enum_matching(type_, LoLEventMinionType.list(), "type_")
