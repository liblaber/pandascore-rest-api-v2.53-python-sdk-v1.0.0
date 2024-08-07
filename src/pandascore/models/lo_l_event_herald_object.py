from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_event_herald_value import LoLEventHeraldValue


@JsonMap({})
class LoLEventHeraldObject(BaseModel):
    """LoLEventHeraldObject

    :param name: name
    :type name: LoLEventHeraldValue
    """

    def __init__(self, name: LoLEventHeraldValue):
        self.name = self._enum_matching(name, LoLEventHeraldValue.list(), "name")
