from typing import Union
from .base import OneOfBaseModel


class Dota2HeroIdOrSlugGuard(OneOfBaseModel):
    class_list = {"int": int, "str": str}


Dota2HeroIdOrSlug = Union[int, str]
