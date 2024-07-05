from typing import Union
from .base import OneOfBaseModel


class OwMapIdOrSlugGuard(OneOfBaseModel):
    class_list = {"int": int, "str": str}


OwMapIdOrSlug = Union[int, str]
