from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_event_champion import LoLEventChampion
from .lo_l_team_color import LoLTeamColor


@JsonMap({})
class LoLEventPlayerObject(BaseModel):
    """LoLEventPlayerObject

    :param champion: champion
    :type champion: LoLEventChampion
    :param player_id: ID of the player
    :type player_id: int
    :param player_name: Professional name of the player
    :type player_name: str
    :param side: side
    :type side: LoLTeamColor
    """

    def __init__(
        self,
        champion: LoLEventChampion,
        player_id: int,
        player_name: str,
        side: LoLTeamColor,
    ):
        self.champion = self._define_object(champion, LoLEventChampion)
        self.player_id = player_id
        self.player_name = player_name
        self.side = self._enum_matching(side, LoLTeamColor.list(), "side")
