# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


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
        self.id_ = self._define_number("id_", id_, ge=1)
        self.image_url = self._define_str("image_url", image_url, nullable=True)
        self.localized_name = localized_name
        self.name = self._define_str(
            "name", name, pattern="^[a-z0-9_-]+$", min_length=1
        )
