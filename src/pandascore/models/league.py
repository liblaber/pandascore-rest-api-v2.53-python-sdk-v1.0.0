from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .base_serie import BaseSerie
from .league_videogame import LeagueVideogame, LeagueVideogameGuard
from .league_videogame_lo_l import LeagueVideogameLoL
from .league_videogame_csgo import LeagueVideogameCsgo
from .league_videogame_dota2 import LeagueVideogameDota2
from .league_videogame_overwatch import LeagueVideogameOverwatch
from .league_videogame_pubg import LeagueVideogamePubg
from .league_videogame_rocket_league import LeagueVideogameRocketLeague
from .league_videogame_codmw import LeagueVideogameCodmw
from .league_videogame_r6siege import LeagueVideogameR6siege
from .league_videogame_fifa import LeagueVideogameFifa
from .league_videogame_valorant import LeagueVideogameValorant
from .league_videogame_kog import LeagueVideogameKog
from .league_videogame_lol_wild_rift import LeagueVideogameLolWildRift
from .league_videogame_starcraft2 import LeagueVideogameStarcraft2
from .league_videogame_starcraft_brood_war import LeagueVideogameStarcraftBroodWar
from .league_videogame_e_basketball import LeagueVideogameEBasketball
from .league_videogame_e_cricket import LeagueVideogameECricket
from .league_videogame_e_soccer import LeagueVideogameESoccer


@JsonMap({"id_": "id"})
class League(BaseModel):
    """League

    :param id_: id_
    :type id_: int
    :param image_url: image_url
    :type image_url: str
    :param modified_at: modified_at
    :type modified_at: str
    :param name: name
    :type name: str
    :param series: series
    :type series: List[BaseSerie]
    :param slug: slug
    :type slug: str
    :param url: url
    :type url: str
    :param videogame: videogame
    :type videogame: LeagueVideogame
    """

    def __init__(
        self,
        id_: int,
        image_url: str,
        modified_at: str,
        name: str,
        series: List[BaseSerie],
        slug: str,
        url: str,
        videogame: LeagueVideogame,
    ):
        self.id_ = id_
        self.image_url = image_url
        self.modified_at = modified_at
        self.name = name
        self.series = self._define_list(series, BaseSerie)
        self.slug = self._pattern_matching(slug, "^[a-z0-9:_-]+$", "slug")
        self.url = url
        self.videogame = LeagueVideogameGuard.return_one_of(videogame)
