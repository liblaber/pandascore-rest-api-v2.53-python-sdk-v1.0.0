from typing import Union
from .base import OneOfBaseModel


class GameIdGuard(OneOfBaseModel):
    class_list = {
        "int": int,
        "int": int,
        "int": int,
        "int": int,
        "int": int,
        "int": int,
    }


GameId = Union[int, int, int, int, int, int]
