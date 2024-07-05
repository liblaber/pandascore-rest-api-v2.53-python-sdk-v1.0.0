from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
from .match_team_opponents_object import MatchTeamOpponentsObject
from .match_player_opponents_object import MatchPlayerOpponentsObject


class MatchOpponentsObjectGuard(OneOfBaseModel):
    class_list = {
        "MatchTeamOpponentsObject": MatchTeamOpponentsObject,
        "MatchPlayerOpponentsObject": MatchPlayerOpponentsObject,
    }


MatchOpponentsObject = Union[MatchTeamOpponentsObject, MatchPlayerOpponentsObject]
