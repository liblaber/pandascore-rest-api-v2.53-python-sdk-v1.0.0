from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .live_endpoint import LiveEndpoint
from .match import Match


@JsonMap({})
class Live(BaseModel):
    """Live

    :param endpoints: endpoints
    :type endpoints: List[LiveEndpoint]
    :param match: match
    :type match: Match
    """

    def __init__(self, endpoints: List[LiveEndpoint], match: Match):
        self.endpoints = self._define_list(endpoints, LiveEndpoint)
        self.match = self._define_object(match, Match)
