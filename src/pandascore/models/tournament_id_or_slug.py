# This file was generated by liblab | https://liblab.com/

from typing import Union
from .base import OneOfBaseModel


class TournamentIdOrSlugGuard(OneOfBaseModel):
    class_list = {"int": int, "str": str}


TournamentIdOrSlug = Union[int, str]