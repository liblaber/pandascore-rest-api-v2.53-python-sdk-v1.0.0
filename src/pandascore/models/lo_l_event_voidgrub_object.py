from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_event_voidgrub_value import LoLEventVoidgrubValue


@JsonMap({})
class LoLEventVoidgrubObject(BaseModel):
    """LoLEventVoidgrubObject

    :param name: name
    :type name: LoLEventVoidgrubValue
    """

    def __init__(self, name: LoLEventVoidgrubValue):
        self.name = self._enum_matching(name, LoLEventVoidgrubValue.list(), "name")
