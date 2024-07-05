from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class SearchOverValorantAgents(BaseModel):
    """SearchOverValorantAgents

    :param name: Name of the agent, defaults to None
    :type name: str, optional
    """

    def __init__(self, name: str = None):
        if name is not None:
            self.name = name
