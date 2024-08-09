# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class Dota2FrameHero(BaseModel):
    """Dota2FrameHero

    :param id_: id_
    :type id_: int
    :param localized_name: localized_name
    :type localized_name: str
    :param name: name
    :type name: str
    """

    def __init__(self, id_: int, localized_name: str, name: str):
        """Dota2FrameHero

        :param id_: id_
        :type id_: int
        :param localized_name: localized_name
        :type localized_name: str
        :param name: name
        :type name: str
        """
        self.id_ = self._define_number("id_", id_, ge=1)
        self.localized_name = localized_name
        self.name = self._define_str(
            "name", name, pattern="^[a-z0-9_-]+$", min_length=1
        )