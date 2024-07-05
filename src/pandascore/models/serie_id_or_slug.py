from typing import Union
from .base import OneOfBaseModel


class SerieIdOrSlugGuard(OneOfBaseModel):
    class_list = {"int": int, "str": str}


SerieIdOrSlug = Union[int, str]
