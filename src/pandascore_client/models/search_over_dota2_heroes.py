# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class SearchOverDota2Heroes(BaseModel):
    """SearchOverDota2Heroes

    :param localized_name: localized_name, defaults to None
    :type localized_name: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    """

    def __init__(self, localized_name: str = None, name: str = None):
        """SearchOverDota2Heroes

        :param localized_name: localized_name, defaults to None
        :type localized_name: str, optional
        :param name: name, defaults to None
        :type name: str, optional
        """
        if localized_name is not None:
            self.localized_name = localized_name
        if name is not None:
            self.name = self._define_str(
                "name", name, pattern="^[a-z0-9_-]+$", min_length=1
            )