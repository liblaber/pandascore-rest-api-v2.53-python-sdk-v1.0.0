# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .lo_l_event_minion_value import LoLEventMinionValue
from .lo_l_team_color import LoLTeamColor


@JsonMap({})
class LoLEventMinionObject(BaseModel):
    """LoLEventMinionObject

    :param name: name
    :type name: LoLEventMinionValue
    :param side: side
    :type side: LoLTeamColor
    """

    def __init__(self, name: LoLEventMinionValue, side: LoLTeamColor):
        """LoLEventMinionObject

        :param name: name
        :type name: LoLEventMinionValue
        :param side: side
        :type side: LoLTeamColor
        """
        self.name = self._enum_matching(name, LoLEventMinionValue.list(), "name")
        self.side = self._enum_matching(side, LoLTeamColor.list(), "side")
