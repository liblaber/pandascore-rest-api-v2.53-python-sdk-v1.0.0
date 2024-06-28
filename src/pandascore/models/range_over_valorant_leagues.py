# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class RangeOverValorantLeagues(BaseModel):
    """RangeOverValorantLeagues

    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param modified_at: modified_at, defaults to None
    :type modified_at: List[str], optional
    :param name: name, defaults to None
    :type name: List[str], optional
    :param slug: slug, defaults to None
    :type slug: List[str], optional
    :param url: url, defaults to None
    :type url: List[str], optional
    """

    def __init__(
        self,
        id_: List[int] = None,
        modified_at: List[str] = None,
        name: List[str] = None,
        slug: List[str] = None,
        url: List[str] = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if modified_at is not None:
            self.modified_at = modified_at
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = slug
        if url is not None:
            self.url = url
