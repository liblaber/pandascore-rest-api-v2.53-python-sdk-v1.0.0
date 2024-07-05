from typing import Union
from .base import OneOfBaseModel


class CsgoWeaponIdOrSlugGuard(OneOfBaseModel):
    class_list = {"int": int, "str": str}


CsgoWeaponIdOrSlug = Union[int, str]
