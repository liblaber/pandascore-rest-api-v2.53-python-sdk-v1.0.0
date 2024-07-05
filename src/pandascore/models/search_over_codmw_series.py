from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .opponent_type import OpponentType


@JsonMap({})
class SearchOverCodmwSeries(BaseModel):
    """SearchOverCodmwSeries

    :param name: name, defaults to None
    :type name: str, optional
    :param season: season, defaults to None
    :type season: str, optional
    :param slug: slug, defaults to None
    :type slug: str, optional
    :param winner_type: winner_type, defaults to None
    :type winner_type: OpponentType, optional
    """

    def __init__(
        self,
        name: str = None,
        season: str = None,
        slug: str = None,
        winner_type: OpponentType = None,
    ):
        if name is not None:
            self.name = name
        if season is not None:
            self.season = season
        if slug is not None:
            self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
        if winner_type is not None:
            self.winner_type = self._enum_matching(
                winner_type, OpponentType.list(), "winner_type"
            )
