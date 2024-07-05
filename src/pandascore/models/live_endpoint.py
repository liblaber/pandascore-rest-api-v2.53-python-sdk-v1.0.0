from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .live_type import LiveType


@JsonMap({"type_": "type"})
class LiveEndpoint(BaseModel):
    """LiveEndpoint

    :param begin_at: begin_at
    :type begin_at: str
    :param expected_begin_at: expected_begin_at
    :type expected_begin_at: str
    :param last_active: Timestamp in milliseconds (since January 1, 1970 00:00:00 UTC)
    :type last_active: int
    :param match_id: match_id
    :type match_id: int
    :param open: Whether live is open
    :type open: bool
    :param type_: type_
    :type type_: LiveType
    :param url: url
    :type url: str
    """

    def __init__(
        self,
        begin_at: str,
        expected_begin_at: str,
        last_active: int,
        match_id: int,
        open: bool,
        type_: LiveType,
        url: str,
    ):
        self.begin_at = begin_at
        self.expected_begin_at = expected_begin_at
        self.last_active = last_active
        self.match_id = match_id
        self.open = open
        self.type_ = self._enum_matching(type_, LiveType.list(), "type_")
        self.url = url
