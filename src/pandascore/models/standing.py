from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
from .bracket_standing import BracketStanding
from .group_standing import GroupStanding


class StandingGuard(OneOfBaseModel):
    class_list = {"BracketStanding": BracketStanding, "GroupStanding": GroupStanding}


Standing = Union[BracketStanding, GroupStanding]
