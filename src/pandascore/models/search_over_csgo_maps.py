from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class SearchOverCsgoMaps(BaseModel):
    """SearchOverCsgoMaps

    :param name: The name of the map., defaults to None
    :type name: str, optional
    :param slug: Human-readable identifier of the map, defaults to None
    :type slug: str, optional
    """

    def __init__(self, name: str = None, slug: str = None):
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
