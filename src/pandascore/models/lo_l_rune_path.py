from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_rune_path_runes_object import LoLRunePathRunesObject


@JsonMap({"id_": "id"})
class LoLRunePath(BaseModel):
    """LoLRunePath

    :param id_: ID of the rune path
    :type id_: int
    :param image_url: URL to an image of the rune path
    :type image_url: str
    :param name: Name of the rune
    :type name: str
    :param runes: runes
    :type runes: LoLRunePathRunesObject
    :param videogame_versions: Array of of video game versions (ie. patches) for this resource
    :type videogame_versions: List[str]
    """

    def __init__(
        self,
        id_: int,
        image_url: str,
        name: str,
        runes: LoLRunePathRunesObject,
        videogame_versions: List[str],
    ):
        self.id_ = id_
        self.image_url = image_url
        self.name = name
        self.runes = self._define_object(runes, LoLRunePathRunesObject)
        self.videogame_versions = videogame_versions
