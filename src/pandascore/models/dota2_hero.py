from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class Dota2Hero(BaseModel):
    """Dota2Hero

    :param id_: id_
    :type id_: int
    :param image_url: image_url
    :type image_url: str
    :param localized_name: localized_name
    :type localized_name: str
    :param name: name
    :type name: str
    """

    def __init__(self, id_: int, image_url: str, localized_name: str, name: str):
        self.id_ = id_
        self.image_url = image_url
        self.localized_name = localized_name
        self.name = self._pattern_matching(name, "^[a-z0-9_-]+$", "name")
