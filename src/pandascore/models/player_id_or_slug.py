from typing import Union
from .base import OneOfBaseModel


class PlayerIdOrSlugGuard(OneOfBaseModel):
    class_list = {"int": int, "str": str}


PlayerIdOrSlug = Union[int, str]
