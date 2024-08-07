from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class SearchOverKogTeams(BaseModel):
    """SearchOverKogTeams

    :param acronym: acronym, defaults to None
    :type acronym: str, optional
    :param location: The team's organization location, defaults to None
    :type location: str, optional
    :param name: The name of the team., defaults to None
    :type name: str, optional
    :param slug: slug, defaults to None
    :type slug: str, optional
    """

    def __init__(
        self,
        acronym: str = None,
        location: str = None,
        name: str = None,
        slug: str = None,
    ):
        if acronym is not None:
            self.acronym = acronym
        if location is not None:
            self.location = location
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
