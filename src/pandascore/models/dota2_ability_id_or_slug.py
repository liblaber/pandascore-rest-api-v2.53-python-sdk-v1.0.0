from typing import Union
from .base import OneOfBaseModel


class Dota2AbilityIdOrSlugGuard(OneOfBaseModel):
    class_list = {"int": int, "str": str}


Dota2AbilityIdOrSlug = Union[int, str]
