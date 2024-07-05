from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .valorant_game_player import ValorantGamePlayer


@JsonMap({"id_": "id"})
class ValorantGameTeam(BaseModel):
    """ValorantGameTeam

    :param acronym: acronym
    :type acronym: str
    :param id_: id_
    :type id_: int
    :param image_url: URL of the team logo
    :type image_url: str
    :param location: The team's organization location
    :type location: str
    :param name: The name of the team.
    :type name: str
    :param players: players
    :type players: List[ValorantGamePlayer]
    :param score: Number of rounds won by the team
    :type score: int
    :param slug: slug
    :type slug: str
    """

    def __init__(
        self,
        acronym: str,
        id_: int,
        image_url: str,
        location: str,
        name: str,
        players: List[ValorantGamePlayer],
        score: int,
        slug: str,
    ):
        self.acronym = acronym
        self.id_ = id_
        self.image_url = image_url
        self.location = location
        self.name = name
        self.players = self._define_list(players, ValorantGamePlayer)
        self.score = score
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
