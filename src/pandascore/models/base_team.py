from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class BaseTeam(BaseModel):
    """BaseTeam

    :param acronym: acronym
    :type acronym: str
    :param id_: id_
    :type id_: int
    :param image_url: URL of the team logo
    :type image_url: str
    :param location: The team's organization location
    :type location: str
    :param modified_at: modified_at
    :type modified_at: str
    :param name: The name of the team.
    :type name: str
    :param slug: slug
    :type slug: str
    """

    def __init__(
        self,
        acronym: str,
        id_: int,
        image_url: str,
        location: str,
        modified_at: str,
        name: str,
        slug: str,
    ):
        self.acronym = acronym
        self.id_ = id_
        self.image_url = image_url
        self.location = location
        self.modified_at = modified_at
        self.name = name
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
