from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
from .team_rosters import TeamRosters
from .player_rosters import PlayerRosters


class TournamentRostersGuard(OneOfBaseModel):
    class_list = {"TeamRosters": TeamRosters, "PlayerRosters": PlayerRosters}


TournamentRosters = Union[TeamRosters, PlayerRosters]
