from typing import Union
from .base import OneOfBaseModel


class MatchIdOrSlugGuard(OneOfBaseModel):
    class_list = {"int": int, "str": str}


MatchIdOrSlug = Union[int, str]
