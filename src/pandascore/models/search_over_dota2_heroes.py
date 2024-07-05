from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class SearchOverDota2Heroes(BaseModel):
    """SearchOverDota2Heroes

    :param localized_name: localized_name, defaults to None
    :type localized_name: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    """

    def __init__(self, localized_name: str = None, name: str = None):
        if localized_name is not None:
            self.localized_name = localized_name
        if name is not None:
            self.name = self._pattern_matching(name, "^[a-z0-9_-]+$", "name")
