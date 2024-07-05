from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class ValorantMap(BaseModel):
    """An object that represents a Valorant map

    :param id_: ID of the map
    :type id_: int
    :param image_url: URL to an image of the map
    :type image_url: str
    :param name: Name of the map
    :type name: str
    :param slug: Human-readable identifier of the map
    :type slug: str
    :param videogame_versions: Array of of video game versions (ie. patches) for this resource
    :type videogame_versions: List[str]
    """

    def __init__(
        self,
        id_: int,
        image_url: str,
        name: str,
        slug: str,
        videogame_versions: List[str],
    ):
        self.id_ = id_
        self.image_url = image_url
        self.name = name
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
        self.videogame_versions = videogame_versions
