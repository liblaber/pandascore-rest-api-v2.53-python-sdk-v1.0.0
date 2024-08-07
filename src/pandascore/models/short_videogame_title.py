from .utils.json_map import JsonMap
from .base import BaseModel


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
        self.id_ = id_
        self.name = name
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
