from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_full_round_player_economy import CsgoFullRoundPlayerEconomy


@JsonMap({"id_": "id"})
class CsgoFullRoundTeamPlayer(BaseModel):
    """CsgoFullRoundTeamPlayer

    :param assists: Player's number of kill assists for a game
    :type assists: int
    :param freeze_time_economy: freeze_time_economy
    :type freeze_time_economy: CsgoFullRoundPlayerEconomy
    :param id_: ID of the player
    :type id_: int
    :param is_alive: Whether the player is alive or not
    :type is_alive: bool
    :param kills: Player's number of kills
    :type kills: int
    :param name: Professional name of the player
    :type name: str
    :param remaining_hp: Number of health points at the end of the round
    :type remaining_hp: int
    :param round_start_economy: round_start_economy
    :type round_start_economy: CsgoFullRoundPlayerEconomy
    """

    def __init__(
        self,
        assists: int,
        freeze_time_economy: CsgoFullRoundPlayerEconomy,
        id_: int,
        is_alive: bool,
        kills: int,
        name: str,
        remaining_hp: int,
        round_start_economy: CsgoFullRoundPlayerEconomy,
    ):
        self.assists = assists
        self.freeze_time_economy = self._define_object(
            freeze_time_economy, CsgoFullRoundPlayerEconomy
        )
        self.id_ = id_
        self.is_alive = is_alive
        self.kills = kills
        self.name = name
        self.remaining_hp = remaining_hp
        self.round_start_economy = self._define_object(
            round_start_economy, CsgoFullRoundPlayerEconomy
        )
