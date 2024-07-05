from typing import Union
from .base import OneOfBaseModel


class OpponentIdGuard(OneOfBaseModel):
    class_list = {"int": int, "int": int}


OpponentId = Union[int, int]
