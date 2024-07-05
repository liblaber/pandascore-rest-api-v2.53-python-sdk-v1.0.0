from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
from .base_player import BasePlayer
from .base_team import BaseTeam


class BaseOpponentGuard(OneOfBaseModel):
    class_list = {"BasePlayer": BasePlayer, "BaseTeam": BaseTeam}


BaseOpponent = Union[BasePlayer, BaseTeam]
