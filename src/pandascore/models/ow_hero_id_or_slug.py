# This file was generated by liblab | https://liblab.com/

from typing import Union
from .base import OneOfBaseModel


class OwHeroIdOrSlugGuard(OneOfBaseModel):
    class_list = {"int": int, "str": str}


OwHeroIdOrSlug = Union[int, str]
