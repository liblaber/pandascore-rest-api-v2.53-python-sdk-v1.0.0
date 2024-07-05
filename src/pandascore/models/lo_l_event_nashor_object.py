from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_event_nashor_value import LoLEventNashorValue


@JsonMap({})
class LoLEventNashorObject(BaseModel):
    """LoLEventNashorObject

    :param name: name
    :type name: LoLEventNashorValue
    """

    def __init__(self, name: LoLEventNashorValue):
        self.name = self._enum_matching(name, LoLEventNashorValue.list(), "name")
