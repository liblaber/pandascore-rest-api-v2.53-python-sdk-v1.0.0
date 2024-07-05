from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
from .csgo_round_start_event import CsgoRoundStartEvent
from .csgo_round_end_event import CsgoRoundEndEvent
from .csgo_kill_event import CsgoKillEvent


class CsgoEventGuard(OneOfBaseModel):
    class_list = {
        "CsgoRoundStartEvent": CsgoRoundStartEvent,
        "CsgoRoundEndEvent": CsgoRoundEndEvent,
        "CsgoKillEvent": CsgoKillEvent,
    }


CsgoEvent = Union[CsgoRoundStartEvent, CsgoRoundEndEvent, CsgoKillEvent]
