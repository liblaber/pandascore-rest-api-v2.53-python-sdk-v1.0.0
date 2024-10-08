# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
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
        self.acronym = self._define_str("acronym", acronym, nullable=True)
        self.id_ = self._define_number("id_", id_, ge=1)
        self.image_url = self._define_str("image_url", image_url, nullable=True)
        self.location = self._define_str("location", location, nullable=True)
        self.name = name
        self.players = self._define_list(players, ValorantGamePlayer)
        self.score = self._define_number("score", score, ge=0)
        self.slug = self._define_str(
            "slug", slug, nullable=True, pattern="^[a-z0-9_-]+$", min_length=1
        )
