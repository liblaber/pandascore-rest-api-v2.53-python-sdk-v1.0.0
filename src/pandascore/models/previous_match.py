from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .previous_match_type import PreviousMatchType


@JsonMap({"type_": "type"})
class PreviousMatch(BaseModel):
    """PreviousMatch

    :param match_id: match_id
    :type match_id: int
    :param type_: type_
    :type type_: PreviousMatchType
    """

    def __init__(self, match_id: int, type_: PreviousMatchType):
        self.match_id = match_id
        self.type_ = self._enum_matching(type_, PreviousMatchType.list(), "type_")
