# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_event_player_object import LoLEventPlayerObject


class LoLEventPlayerType(Enum):
    """An enumeration representing different categories.

    :cvar PLAYER: "player"
    :vartype PLAYER: str
    """

    PLAYER = "player"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLEventPlayerType._member_map_.values()))


@JsonMap({"type_": "type"})
class LoLEventPlayer(BaseModel):
    """LoLEventPlayer

    :param object: object
    :type object: LoLEventPlayerObject
    :param type_: type_
    :type type_: LoLEventPlayerType
    """

    def __init__(self, object: LoLEventPlayerObject, type_: LoLEventPlayerType):
        self.object = self._define_object(object, LoLEventPlayerObject)
        self.type_ = self._enum_matching(type_, LoLEventPlayerType.list(), "type_")