from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class RangeOverValorantWeapons(BaseModel):
    """RangeOverValorantWeapons

    :param creds: creds, defaults to None
    :type creds: List[float], optional
    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param name: name, defaults to None
    :type name: List[str], optional
    """

    def __init__(
        self, creds: List[float] = None, id_: List[int] = None, name: List[str] = None
    ):
        if creds is not None:
            self.creds = creds
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
