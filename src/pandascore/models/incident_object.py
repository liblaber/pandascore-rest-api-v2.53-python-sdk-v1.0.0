from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
from .league import League
from .serie import Serie
from .tournament import Tournament
from .match import Match
from .player import Player
from .team import Team


class IncidentObjectGuard(OneOfBaseModel):
    class_list = {
        "League": League,
        "Serie": Serie,
        "Tournament": Tournament,
        "Match": Match,
        "Player": Player,
        "Team": Team,
    }


IncidentObject = Union[League, Serie, Tournament, Match, Player, Team]
