from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_flags import LoLFlags
from .lo_l_kill_counters import LoLKillCounters
from .lo_l_kills_series import LoLKillsSeries


class LoLMatchGamePlayerRole(Enum):
    """An enumeration representing different categories.

    :cvar ADC: "adc"
    :vartype ADC: str
    :cvar JUN: "jun"
    :vartype JUN: str
    :cvar MID: "mid"
    :vartype MID: str
    :cvar SUP: "sup"
    :vartype SUP: str
    :cvar TOP: "top"
    :vartype TOP: str
    """

    ADC = "adc"
    JUN = "jun"
    MID = "mid"
    SUP = "sup"
    TOP = "top"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, LoLMatchGamePlayerRole._member_map_.values())
        )


@JsonMap({})
class LoLMatchGamePlayer(BaseModel):
    """Player's data for a Game in a LoL Match

    :param assists: assists
    :type assists: int
    :param deaths: deaths
    :type deaths: int
    :param flags: flags
    :type flags: LoLFlags
    :param kills: kills
    :type kills: int
    :param kills_counters: kills_counters
    :type kills_counters: LoLKillCounters
    :param kills_series: kills_series
    :type kills_series: LoLKillsSeries
    :param largest_critical_strike: largest_critical_strike
    :type largest_critical_strike: int
    :param largest_killing_spree: largest_killing_spree
    :type largest_killing_spree: int
    :param largest_multi_kill: largest_multi_kill
    :type largest_multi_kill: int
    :param player_id: ID of the player
    :type player_id: int
    :param role: role
    :type role: LoLMatchGamePlayerRole
    """

    def __init__(
        self,
        assists: int,
        deaths: int,
        flags: LoLFlags,
        kills: int,
        kills_counters: LoLKillCounters,
        kills_series: LoLKillsSeries,
        largest_critical_strike: int,
        largest_killing_spree: int,
        largest_multi_kill: int,
        player_id: int,
        role: LoLMatchGamePlayerRole,
    ):
        self.assists = assists
        self.deaths = deaths
        self.flags = self._define_object(flags, LoLFlags)
        self.kills = kills
        self.kills_counters = self._define_object(kills_counters, LoLKillCounters)
        self.kills_series = self._define_object(kills_series, LoLKillsSeries)
        self.largest_critical_strike = largest_critical_strike
        self.largest_killing_spree = largest_killing_spree
        self.largest_multi_kill = largest_multi_kill
        self.player_id = player_id
        self.role = self._enum_matching(role, LoLMatchGamePlayerRole.list(), "role")
