from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .base_valorant_agent import BaseValorantAgent


@JsonMap({"id_": "id"})
class ValorantEventPlayer(BaseModel):
    """ValorantEventPlayer

    :param agent: agent
    :type agent: BaseValorantAgent
    :param id_: ID of the player
    :type id_: int
    :param name: Professional name of the player
    :type name: str
    """

    def __init__(self, agent: BaseValorantAgent, id_: int, name: str):
        self.agent = self._define_object(agent, BaseValorantAgent)
        self.id_ = id_
        self.name = name
