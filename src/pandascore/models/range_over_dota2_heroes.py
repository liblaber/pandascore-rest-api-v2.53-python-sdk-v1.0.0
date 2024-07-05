from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class RangeOverDota2Heroes(BaseModel):
    """RangeOverDota2Heroes

    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param localized_name: localized_name, defaults to None
    :type localized_name: List[str], optional
    :param name: name, defaults to None
    :type name: List[str], optional
    """

    def __init__(
        self,
        id_: List[int] = None,
        localized_name: List[str] = None,
        name: List[str] = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if localized_name is not None:
            self.localized_name = localized_name
        if name is not None:
            self.name = name
