from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .base_player import BasePlayer


@JsonMap({"id_": "id"})
class Team(BaseModel):
    """Team

    :param acronym: acronym
    :type acronym: str
    :param current_videogame: current_videogame
    :type current_videogame: dict
    :param id_: id_
    :type id_: int
    :param image_url: URL of the team logo
    :type image_url: str
    :param location: The team's organization location
    :type location: str
    :param modified_at: modified_at
    :type modified_at: str
    :param name: The name of the team.
    :type name: str
    :param players: players
    :type players: List[BasePlayer]
    :param slug: slug
    :type slug: str
    """

    def __init__(
        self,
        acronym: str,
        current_videogame: dict,
        id_: int,
        image_url: str,
        location: str,
        modified_at: str,
        name: str,
        players: List[BasePlayer],
        slug: str,
    ):
        self.acronym = acronym
        self.current_videogame = current_videogame
        self.id_ = id_
        self.image_url = image_url
        self.location = location
        self.modified_at = modified_at
        self.name = name
        self.players = self._define_list(players, BasePlayer)
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
