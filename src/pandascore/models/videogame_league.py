from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .base_serie import BaseSerie


@JsonMap({"id_": "id"})
class VideogameLeague(BaseModel):
    """VideogameLeague

    :param id_: id_
    :type id_: int
    :param image_url: image_url
    :type image_url: str
    :param modified_at: modified_at
    :type modified_at: str
    :param name: name
    :type name: str
    :param series: series
    :type series: List[BaseSerie]
    :param slug: slug
    :type slug: str
    :param url: url
    :type url: str
    """

    def __init__(
        self,
        id_: int,
        image_url: str,
        modified_at: str,
        name: str,
        series: List[BaseSerie],
        slug: str,
        url: str,
    ):
        self.id_ = id_
        self.image_url = image_url
        self.modified_at = modified_at
        self.name = name
        self.series = self._define_list(series, BaseSerie)
        self.slug = self._pattern_matching(slug, "^[a-z0-9:_-]+$", "slug")
        self.url = url
