from typing import Union
from .base import OneOfBaseModel


class VideogameTitleIdOrSlugGuard(OneOfBaseModel):
    class_list = {"int": int, "str": str}


VideogameTitleIdOrSlug = Union[int, str]
