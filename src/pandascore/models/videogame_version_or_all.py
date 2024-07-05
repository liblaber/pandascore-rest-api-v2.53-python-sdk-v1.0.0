from typing import Union
from .base import OneOfBaseModel


class VideogameVersionOrAllGuard(OneOfBaseModel):
    class_list = {"str": str, "any": any, "any": any}


VideogameVersionOrAll = Union[str, any, any]
