from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_players_role import LoLPlayersRole


@JsonMap({"id_": "id"})
class LoLFrameTeam(BaseModel):
    """LoLFrameTeam

    :param acronym: acronym
    :type acronym: str
    :param drakes: drakes
    :type drakes: int
    :param gold: gold
    :type gold: int
    :param id_: id_
    :type id_: int
    :param inhibitors: Number of inhibitors killed by the player
    :type inhibitors: int
    :param kills: kills
    :type kills: int
    :param name: The name of the team.
    :type name: str
    :param nashors: nashors
    :type nashors: int
    :param players: players
    :type players: LoLPlayersRole
    :param score: score
    :type score: int
    :param towers: towers
    :type towers: int
    :param voidgrubs: The number of voidgrubs killed by a team.
    :type voidgrubs: int
    """

    def __init__(
        self,
        acronym: str,
        drakes: int,
        gold: int,
        id_: int,
        inhibitors: int,
        kills: int,
        name: str,
        nashors: int,
        players: LoLPlayersRole,
        score: int,
        towers: int,
        voidgrubs: int,
    ):
        self.acronym = acronym
        self.drakes = drakes
        self.gold = gold
        self.id_ = id_
        self.inhibitors = inhibitors
        self.kills = kills
        self.name = name
        self.nashors = nashors
        self.players = self._define_object(players, LoLPlayersRole)
        self.score = score
        self.towers = towers
        self.voidgrubs = voidgrubs
