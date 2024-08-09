# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .ow_map_game_mode import OwMapGameMode


@JsonMap({})
class SearchOverOwMaps(BaseModel):
    """SearchOverOwMaps

    :param game_mode: game_mode, defaults to None
    :type game_mode: OwMapGameMode, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param slug: slug, defaults to None
    :type slug: str, optional
    """

    def __init__(
        self, game_mode: OwMapGameMode = None, name: str = None, slug: str = None
    ):
        """SearchOverOwMaps

        :param game_mode: game_mode, defaults to None
        :type game_mode: OwMapGameMode, optional
        :param name: name, defaults to None
        :type name: str, optional
        :param slug: slug, defaults to None
        :type slug: str, optional
        """
        if game_mode is not None:
            self.game_mode = self._enum_matching(
                game_mode, OwMapGameMode.list(), "game_mode"
            )
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = self._define_str(
                "slug", slug, pattern="^[a-z0-9_-]+$", min_length=1
            )