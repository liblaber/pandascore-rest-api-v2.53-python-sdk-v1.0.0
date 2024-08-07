from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class SearchOverOwLeagues(BaseModel):
    """SearchOverOwLeagues

    :param name: name, defaults to None
    :type name: str, optional
    :param slug: slug, defaults to None
    :type slug: str, optional
    :param url: url, defaults to None
    :type url: str, optional
    """

    def __init__(self, name: str = None, slug: str = None, url: str = None):
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = self._pattern_matching(slug, "^[a-z0-9:_-]+$", "slug")
        if url is not None:
            self.url = url
