# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
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
        """PreviousMatch

        :param match_id: match_id
        :type match_id: int
        :param type_: type_
        :type type_: PreviousMatchType
        """
        self.match_id = self._define_number("match_id", match_id, ge=1)
        self.type_ = self._enum_matching(type_, PreviousMatchType.list(), "type_")
