from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class LeagueVideogameR6siege(BaseModel):
    """LeagueVideogameR6siege

    :param current_version: current_version
    :type current_version: str
    :param id_: id_
    :type id_: any
    :param name: name
    :type name: any
    :param slug: slug
    :type slug: any
    """

    def __init__(self, current_version: str, id_: any, name: any, slug: any):
        self.current_version = self._pattern_matching(
            current_version, "^[0-9]+\.[0-9]+(\.[0-9]+)?$", "current_version"
        )
        self.id_ = id_
        self.name = name
        self.slug = slug
