# This file was generated by liblab | https://liblab.com/

from typing import Union
from .utils.one_of_base_model import OneOfBaseModel


class TeamIdOrSlugGuard(OneOfBaseModel):
    class_list = {"int": int, "str": str}


TeamIdOrSlug = Union[int, str]