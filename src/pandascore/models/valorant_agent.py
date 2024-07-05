from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class ValorantAgent(BaseModel):
    """ValorantAgent

    :param id_: ID of the agent
    :type id_: int
    :param name: Name of the agent
    :type name: str
    :param portrait_url: URL to a portrait image of the agent
    :type portrait_url: str
    :param videogame_versions: Array of of video game versions (ie. patches) for this resource
    :type videogame_versions: List[str]
    """

    def __init__(
        self, id_: int, name: str, portrait_url: str, videogame_versions: List[str]
    ):
        self.id_ = id_
        self.name = name
        self.portrait_url = portrait_url
        self.videogame_versions = videogame_versions
