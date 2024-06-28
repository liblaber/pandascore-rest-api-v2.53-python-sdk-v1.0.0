# This file was generated by liblab | https://liblab.com/

from typing import Union
from .utils.json_map import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel


@JsonMap({})
class Page2(BaseModel):
    """Page2

    :param number: number, defaults to None
    :type number: int, optional
    :param size: size, defaults to None
    :type size: int, optional
    """

    def __init__(self, number: int = None, size: int = None):
        if number is not None:
            self.number = number
        if size is not None:
            self.size = size


class GetDota2MatchesUpcomingPageGuard(OneOfBaseModel):
    class_list = {"int": int, "Page2": Page2}


GetDota2MatchesUpcomingPage = Union[int, Page2]
