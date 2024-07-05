from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_event_tower_value import LoLEventTowerValue
from .lo_l_team_color import LoLTeamColor


@JsonMap({})
class LoLEventTowerObject(BaseModel):
    """LoLEventTowerObject

    :param name: name
    :type name: LoLEventTowerValue
    :param side: side
    :type side: LoLTeamColor
    """

    def __init__(self, name: LoLEventTowerValue, side: LoLTeamColor):
        self.name = self._enum_matching(name, LoLEventTowerValue.list(), "name")
        self.side = self._enum_matching(side, LoLTeamColor.list(), "side")
