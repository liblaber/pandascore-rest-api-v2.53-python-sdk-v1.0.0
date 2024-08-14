# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


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
        """The location selected during the picks and bans phase for the game.

        :param id_: The ID of the map.
        :type id_: int
        :param image_url: A URL to the image of the map.
        :type image_url: str
        :param name: The name of the map.
        :type name: str
        """
        self.id_ = self._define_number("id_", id_, ge=1)
        self.image_url = self._define_str("image_url", image_url, nullable=True)
        self.name = name
