from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class RangeOverKogTeams(BaseModel):
    """RangeOverKogTeams

    :param acronym: acronym, defaults to None
    :type acronym: List[str], optional
    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param location: location, defaults to None
    :type location: List[str], optional
    :param modified_at: modified_at, defaults to None
    :type modified_at: List[str], optional
    :param name: name, defaults to None
    :type name: List[str], optional
    :param slug: slug, defaults to None
    :type slug: List[str], optional
    """

    def __init__(
        self,
        acronym: List[str] = None,
        id_: List[int] = None,
        location: List[str] = None,
        modified_at: List[str] = None,
        name: List[str] = None,
        slug: List[str] = None,
    ):
        if acronym is not None:
            self.acronym = acronym
        if id_ is not None:
            self.id_ = id_
        if location is not None:
            self.location = location
        if modified_at is not None:
            self.modified_at = modified_at
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = slug
