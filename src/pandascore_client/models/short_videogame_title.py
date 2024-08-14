# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class ShortVideogameTitle(BaseModel):
    """ShortVideogameTitle

    :param id_: id_
    :type id_: int
    :param name: name
    :type name: str
    :param slug: slug
    :type slug: str
    """

    def __init__(self, id_: int, name: str, slug: str):
        """ShortVideogameTitle

        :param id_: id_
        :type id_: int
        :param name: name
        :type name: str
        :param slug: slug
        :type slug: str
        """
        self.id_ = self._define_number("id_", id_, ge=1)
        self.name = name
        self.slug = self._define_str(
            "slug", slug, pattern="^[a-z0-9_-]+$", min_length=1
        )
