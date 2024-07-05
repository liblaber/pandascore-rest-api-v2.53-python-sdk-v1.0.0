from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .dota2_frame_team import Dota2FrameTeam


@JsonMap({})
class Dota2Frame(BaseModel):
    """Dota2Frame

    :param current_timestamp: Time elapsed since the beginning of the game, in seconds
    :type current_timestamp: int
    :param dire_team: dire_team
    :type dire_team: Dota2FrameTeam
    :param radiant_team: radiant_team
    :type radiant_team: Dota2FrameTeam
    """

    def __init__(
        self,
        current_timestamp: int,
        dire_team: Dota2FrameTeam,
        radiant_team: Dota2FrameTeam,
    ):
        self.current_timestamp = current_timestamp
        self.dire_team = self._define_object(dire_team, Dota2FrameTeam)
        self.radiant_team = self._define_object(radiant_team, Dota2FrameTeam)
