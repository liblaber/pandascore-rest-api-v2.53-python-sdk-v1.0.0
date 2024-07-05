from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
from .videogame_lo_l import VideogameLoL
from .videogame_csgo import VideogameCsgo
from .videogame_dota2 import VideogameDota2
from .videogame_overwatch import VideogameOverwatch
from .videogame_pubg import VideogamePubg
from .videogame_rocket_league import VideogameRocketLeague
from .videogame_codmw import VideogameCodmw
from .videogame_r6siege import VideogameR6siege
from .videogame_fifa import VideogameFifa
from .videogame_valorant import VideogameValorant
from .videogame_kog import VideogameKog
from .videogame_lol_wild_rift import VideogameLolWildRift
from .videogame_starcraft2 import VideogameStarcraft2
from .videogame_starcraft_brood_war import VideogameStarcraftBroodWar
from .videogame_e_soccer import VideogameESoccer
from .videogame_e_basketball import VideogameEBasketball
from .videogame_e_cricket import VideogameECricket


class VideogameGuard(OneOfBaseModel):
    class_list = {
        "VideogameLoL": VideogameLoL,
        "VideogameCsgo": VideogameCsgo,
        "VideogameDota2": VideogameDota2,
        "VideogameOverwatch": VideogameOverwatch,
        "VideogamePubg": VideogamePubg,
        "VideogameRocketLeague": VideogameRocketLeague,
        "VideogameCodmw": VideogameCodmw,
        "VideogameR6siege": VideogameR6siege,
        "VideogameFifa": VideogameFifa,
        "VideogameValorant": VideogameValorant,
        "VideogameKog": VideogameKog,
        "VideogameLolWildRift": VideogameLolWildRift,
        "VideogameStarcraft2": VideogameStarcraft2,
        "VideogameStarcraftBroodWar": VideogameStarcraftBroodWar,
        "VideogameESoccer": VideogameESoccer,
        "VideogameEBasketball": VideogameEBasketball,
        "VideogameECricket": VideogameECricket,
    }


Videogame = Union[
    VideogameLoL,
    VideogameCsgo,
    VideogameDota2,
    VideogameOverwatch,
    VideogamePubg,
    VideogameRocketLeague,
    VideogameCodmw,
    VideogameR6siege,
    VideogameFifa,
    VideogameValorant,
    VideogameKog,
    VideogameLolWildRift,
    VideogameStarcraft2,
    VideogameStarcraftBroodWar,
    VideogameESoccer,
    VideogameEBasketball,
    VideogameECricket,
]
