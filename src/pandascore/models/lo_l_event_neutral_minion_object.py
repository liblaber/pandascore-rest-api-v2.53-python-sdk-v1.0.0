from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_event_neutral_minion_value import LoLEventNeutralMinionValue


@JsonMap({})
class LoLEventNeutralMinionObject(BaseModel):
    """LoLEventNeutralMinionObject

    :param name: name
    :type name: LoLEventNeutralMinionValue
    """

    def __init__(self, name: LoLEventNeutralMinionValue):
        self.name = self._enum_matching(name, LoLEventNeutralMinionValue.list(), "name")
