from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class BaseValorantAgent(BaseModel):
    """BaseValorantAgent

    :param id_: ID of the agent
    :type id_: int
    :param name: Name of the agent
    :type name: str
    :param portrait_url: URL to a portrait image of the agent
    :type portrait_url: str
    """

    def __init__(self, id_: int, name: str, portrait_url: str):
        self.id_ = id_
        self.name = name
        self.portrait_url = portrait_url
