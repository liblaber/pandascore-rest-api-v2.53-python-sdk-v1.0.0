from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
from .videogame_id import VideogameId
from .videogame_slug import VideogameSlug


class VideogameIdOrSlugGuard(OneOfBaseModel):
    class_list = {"VideogameIdEnum": int, "VideogameSlugEnum": str}


VideogameIdOrSlug = Union[int, str]
