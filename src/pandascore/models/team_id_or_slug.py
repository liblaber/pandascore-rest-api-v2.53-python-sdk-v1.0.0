from typing import Union
from .base import OneOfBaseModel


class TeamIdOrSlugGuard(OneOfBaseModel):
    class_list = {"int": int, "str": str}


TeamIdOrSlug = Union[int, str]
