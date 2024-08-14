# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
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
        self.begin_at = self._define_str(
            "begin_at", begin_at, nullable=True, min_length=1
        )
        self.expected_begin_at = self._define_str(
            "expected_begin_at", expected_begin_at, nullable=True, min_length=1
        )
        self.last_active = self._define_number(
            "last_active", last_active, nullable=True, ge=0
        )
        self.match_id = self._define_number("match_id", match_id, ge=1)
        self.open = open
        self.type_ = self._enum_matching(type_, LiveType.list(), "type_")
        self.url = url
