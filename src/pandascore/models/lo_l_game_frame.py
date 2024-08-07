from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_frame_team import LoLFrameTeam


@JsonMap({})
class LoLGameFrame(BaseModel):
    """LoLGameFrame

    :param blue: blue
    :type blue: LoLFrameTeam
    :param current_timestamp: current_timestamp
    :type current_timestamp: int
    :param game_id: LoL game ID
    :type game_id: int
    :param match_id: match_id
    :type match_id: int
    :param red: red
    :type red: LoLFrameTeam
    :param tournament_id: tournament_id
    :type tournament_id: int
    """

    def __init__(
        self,
        blue: LoLFrameTeam,
        current_timestamp: int,
        game_id: int,
        match_id: int,
        red: LoLFrameTeam,
        tournament_id: int,
    ):
        self.blue = self._define_object(blue, LoLFrameTeam)
        self.current_timestamp = current_timestamp
        self.game_id = game_id
        self.match_id = match_id
        self.red = self._define_object(red, LoLFrameTeam)
        self.tournament_id = tournament_id
