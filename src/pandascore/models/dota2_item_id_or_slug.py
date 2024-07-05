from typing import Union
from .base import OneOfBaseModel


class Dota2ItemIdOrSlugGuard(OneOfBaseModel):
    class_list = {"int": int, "str": str}


Dota2ItemIdOrSlug = Union[int, str]
