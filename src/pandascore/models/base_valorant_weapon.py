# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class BaseValorantWeapon(BaseModel):
    """BaseValorantWeapon

    :param id_: ID of the weapon
    :type id_: int
    :param image_url: URL to an image of the weapon
    :type image_url: str
    :param name: Name of the weapon
    :type name: str
    """

    def __init__(self, id_: int, image_url: str, name: str):
        self.id_ = id_
        self.image_url = image_url
        self.name = name