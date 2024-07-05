from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .ow_map_game_mode import OwMapGameMode


@JsonMap({"id_": "id"})
class OwMap(BaseModel):
    """OwMap

    :param game_mode: game_mode
    :type game_mode: OwMapGameMode
    :param id_: id_
    :type id_: int
    :param image_url: image_url
    :type image_url: str
    :param name: name
    :type name: str
    :param slug: slug
    :type slug: str
    :param thumbnail_url: thumbnail_url
    :type thumbnail_url: str
    """

    def __init__(
        self,
        game_mode: OwMapGameMode,
        id_: int,
        image_url: str,
        name: str,
        slug: str,
        thumbnail_url: str,
    ):
        self.game_mode = self._enum_matching(
            game_mode, OwMapGameMode.list(), "game_mode"
        )
        self.id_ = id_
        self.image_url = image_url
        self.name = name
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
        self.thumbnail_url = thumbnail_url
