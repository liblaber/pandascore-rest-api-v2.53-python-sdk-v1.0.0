from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .match_type import MatchType
from .match_status import MatchStatus
from .match_winner_type import MatchWinnerType


@JsonMap({})
class SearchOverRlMatches(BaseModel):
    """SearchOverRlMatches

    :param match_type: match_type, defaults to None
    :type match_type: MatchType, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param slug: slug, defaults to None
    :type slug: str, optional
    :param status: status, defaults to None
    :type status: MatchStatus, optional
    :param winner_type: winner_type, defaults to None
    :type winner_type: MatchWinnerType, optional
    """

    def __init__(
        self,
        match_type: MatchType = None,
        name: str = None,
        slug: str = None,
        status: MatchStatus = None,
        winner_type: MatchWinnerType = None,
    ):
        if match_type is not None:
            self.match_type = self._enum_matching(
                match_type, MatchType.list(), "match_type"
            )
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = self._pattern_matching(slug, "^[ a-zA-Z0-9_-]+$", "slug")
        if status is not None:
            self.status = self._enum_matching(status, MatchStatus.list(), "status")
        if winner_type is not None:
            self.winner_type = self._enum_matching(
                winner_type, MatchWinnerType.list(), "winner_type"
            )
