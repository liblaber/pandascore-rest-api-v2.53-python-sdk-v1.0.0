from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_event_inhibitor_value import LoLEventInhibitorValue
from .lo_l_team_color import LoLTeamColor


@JsonMap({})
class LoLEventInhibitorObject(BaseModel):
    """LoLEventInhibitorObject

    :param name: name
    :type name: LoLEventInhibitorValue
    :param side: side
    :type side: LoLTeamColor
    """

    def __init__(self, name: LoLEventInhibitorValue, side: LoLTeamColor):
        self.name = self._enum_matching(name, LoLEventInhibitorValue.list(), "name")
        self.side = self._enum_matching(side, LoLTeamColor.list(), "side")
