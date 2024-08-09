# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class SearchOverStarcraft2Leagues(BaseModel):
    """SearchOverStarcraft2Leagues

    :param name: name, defaults to None
    :type name: str, optional
    :param slug: slug, defaults to None
    :type slug: str, optional
    :param url: url, defaults to None
    :type url: str, optional
    """

    def __init__(self, name: str = None, slug: str = None, url: str = None):
        """SearchOverStarcraft2Leagues

        :param name: name, defaults to None
        :type name: str, optional
        :param slug: slug, defaults to None
        :type slug: str, optional
        :param url: url, defaults to None
        :type url: str, optional
        """
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = self._define_str(
                "slug", slug, pattern="^[a-z0-9:_-]+$", min_length=1
            )
        if url is not None:
            self.url = url