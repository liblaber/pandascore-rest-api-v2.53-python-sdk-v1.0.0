from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class CsgoFullRoundMap(BaseModel):
    """The location selected during the picks and bans phase for the game.

    :param id_: The ID of the map.
    :type id_: int
    :param image_url: A URL to the image of the map.
    :type image_url: str
    :param name: The name of the map.
    :type name: str
    """

    def __init__(self, id_: int, image_url: str, name: str):
        self.id_ = id_
        self.image_url = image_url
        self.name = name
