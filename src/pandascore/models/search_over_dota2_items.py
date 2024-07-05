from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class SearchOverDota2Items(BaseModel):
    """SearchOverDota2Items

    :param name: name, defaults to None
    :type name: str, optional
    """

    def __init__(self, name: str = None):
        if name is not None:
            self.name = self._pattern_matching(name, "^[a-z0-9_-]+$", "name")
