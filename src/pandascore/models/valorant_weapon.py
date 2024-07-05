from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class ValorantWeapon(BaseModel):
    """ValorantWeapon

    :param creds: Credit cost of the weapon
    :type creds: float
    :param id_: ID of the weapon
    :type id_: int
    :param image_url: URL to an image of the weapon
    :type image_url: str
    :param name: Name of the weapon
    :type name: str
    :param videogame_versions: Array of of video game versions (ie. patches) for this resource
    :type videogame_versions: List[str]
    """

    def __init__(
        self,
        creds: float,
        id_: int,
        image_url: str,
        name: str,
        videogame_versions: List[str],
    ):
        self.creds = creds
        self.id_ = id_
        self.image_url = image_url
        self.name = name
        self.videogame_versions = videogame_versions
