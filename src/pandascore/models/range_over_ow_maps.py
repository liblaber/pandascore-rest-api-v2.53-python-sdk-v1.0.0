from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .ow_map_game_mode import OwMapGameMode


@JsonMap({"id_": "id"})
class RangeOverOwMaps(BaseModel):
    """RangeOverOwMaps

    :param game_mode: game_mode, defaults to None
    :type game_mode: List[OwMapGameMode], optional
    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param name: name, defaults to None
    :type name: List[str], optional
    :param slug: slug, defaults to None
    :type slug: List[str], optional
    """

    def __init__(
        self,
        game_mode: List[OwMapGameMode] = None,
        id_: List[int] = None,
        name: List[str] = None,
        slug: List[str] = None,
    ):
        if game_mode is not None:
            self.game_mode = self._define_list(game_mode, OwMapGameMode)
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = slug
