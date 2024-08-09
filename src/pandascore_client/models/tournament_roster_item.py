# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .base_player import BasePlayer
from .base_team import BaseTeam


@JsonMap({})
class TournamentRosterItem(BaseModel):
    """TournamentRosterItem

    :param players: players
    :type players: List[BasePlayer]
    :param team: team
    :type team: BaseTeam
    """

    def __init__(self, players: List[BasePlayer], team: BaseTeam):
        """TournamentRosterItem

        :param players: players
        :type players: List[BasePlayer]
        :param team: team
        :type team: BaseTeam
        """
        self.players = self._define_list(players, BasePlayer)
        self.team = self._define_object(team, BaseTeam)