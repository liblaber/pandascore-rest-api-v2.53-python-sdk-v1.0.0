from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class Dota2Item(BaseModel):
    """Dota2Item

    :param id_: id_
    :type id_: int
    :param image_url: image_url
    :type image_url: str
    :param name: name
    :type name: str
    """

    def __init__(self, id_: int, image_url: str, name: str):
        self.id_ = id_
        self.image_url = image_url
        self.name = self._pattern_matching(name, "^[a-z0-9_-]+$", "name")
