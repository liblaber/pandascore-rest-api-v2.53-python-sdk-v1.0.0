from typing import Union
from .base import OneOfBaseModel


class IncidentIdGuard(OneOfBaseModel):
    class_list = {
        "int": int,
        "int": int,
        "int": int,
        "int": int,
        "int": int,
        "int": int,
    }


IncidentId = Union[int, int, int, int, int, int]
