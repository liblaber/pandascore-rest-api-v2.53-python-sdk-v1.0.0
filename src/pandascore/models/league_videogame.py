from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
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


class LeagueVideogameGuard(OneOfBaseModel):
    class_list = {
        "LeagueVideogameLoL": LeagueVideogameLoL,
        "LeagueVideogameCsgo": LeagueVideogameCsgo,
        "LeagueVideogameDota2": LeagueVideogameDota2,
        "LeagueVideogameOverwatch": LeagueVideogameOverwatch,
        "LeagueVideogamePubg": LeagueVideogamePubg,
        "LeagueVideogameRocketLeague": LeagueVideogameRocketLeague,
        "LeagueVideogameCodmw": LeagueVideogameCodmw,
        "LeagueVideogameR6siege": LeagueVideogameR6siege,
        "LeagueVideogameFifa": LeagueVideogameFifa,
        "LeagueVideogameValorant": LeagueVideogameValorant,
        "LeagueVideogameKog": LeagueVideogameKog,
        "LeagueVideogameLolWildRift": LeagueVideogameLolWildRift,
        "LeagueVideogameStarcraft2": LeagueVideogameStarcraft2,
        "LeagueVideogameStarcraftBroodWar": LeagueVideogameStarcraftBroodWar,
        "LeagueVideogameEBasketball": LeagueVideogameEBasketball,
        "LeagueVideogameECricket": LeagueVideogameECricket,
        "LeagueVideogameESoccer": LeagueVideogameESoccer,
    }


LeagueVideogame = Union[
    LeagueVideogameLoL,
    LeagueVideogameCsgo,
    LeagueVideogameDota2,
    LeagueVideogameOverwatch,
    LeagueVideogamePubg,
    LeagueVideogameRocketLeague,
    LeagueVideogameCodmw,
    LeagueVideogameR6siege,
    LeagueVideogameFifa,
    LeagueVideogameValorant,
    LeagueVideogameKog,
    LeagueVideogameLolWildRift,
    LeagueVideogameStarcraft2,
    LeagueVideogameStarcraftBroodWar,
    LeagueVideogameEBasketball,
    LeagueVideogameECricket,
    LeagueVideogameESoccer,
]
