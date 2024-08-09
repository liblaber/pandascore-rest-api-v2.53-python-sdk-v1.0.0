# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class BaseLoLItem(BaseModel):
    """BaseLoLItem

    :param id_: id_
    :type id_: int
    :param image_url: image_url
    :type image_url: str
    :param is_trinket: Whether item is a trinket
    :type is_trinket: bool
    :param name: name
    :type name: str
    """

    def __init__(self, id_: int, image_url: str, is_trinket: bool, name: str):
        """BaseLoLItem

        :param id_: id_
        :type id_: int
        :param image_url: image_url
        :type image_url: str
        :param is_trinket: Whether item is a trinket
        :type is_trinket: bool
        :param name: name
        :type name: str
        """
        self.id_ = self._define_number("id_", id_, ge=1)
        self.image_url = self._define_str("image_url", image_url, nullable=True)
        self.is_trinket = is_trinket
        self.name = name
