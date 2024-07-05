from typing import Union
from .base import OneOfBaseModel


class LeagueIdOrSlugGuard(OneOfBaseModel):
    class_list = {"int": int, "str": str}


LeagueIdOrSlug = Union[int, str]
