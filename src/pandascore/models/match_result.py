from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
from .match_team_result import MatchTeamResult
from .match_player_result import MatchPlayerResult


class MatchResultGuard(OneOfBaseModel):
    class_list = {
        "MatchTeamResult": MatchTeamResult,
        "MatchPlayerResult": MatchPlayerResult,
    }


MatchResult = Union[MatchTeamResult, MatchPlayerResult]
