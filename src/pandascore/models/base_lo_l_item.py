from .utils.json_map import JsonMap
from .base import BaseModel


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
        self.id_ = id_
        self.image_url = image_url
        self.is_trinket = is_trinket
        self.name = name
