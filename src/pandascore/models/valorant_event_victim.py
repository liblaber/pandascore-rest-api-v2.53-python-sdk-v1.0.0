from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .base_valorant_agent import BaseValorantAgent
from .valorant_team_side import ValorantTeamSide


@JsonMap({"id_": "id"})
class ValorantEventVictim(BaseModel):
    """ValorantEventVictim

    :param agent: agent
    :type agent: BaseValorantAgent
    :param id_: ID of the player
    :type id_: int
    :param name: Professional name of the player
    :type name: str
    :param team_side: Team side in the round
    :type team_side: ValorantTeamSide
    """

    def __init__(
        self, agent: BaseValorantAgent, id_: int, name: str, team_side: ValorantTeamSide
    ):
        self.agent = self._define_object(agent, BaseValorantAgent)
        self.id_ = id_
        self.name = name
        self.team_side = self._enum_matching(
            team_side, ValorantTeamSide.list(), "team_side"
        )
