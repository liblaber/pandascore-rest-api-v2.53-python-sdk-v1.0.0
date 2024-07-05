from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .dota2_faction import Dota2Faction
from .base_team import BaseTeam


@JsonMap({})
class BarracksStatus(BaseModel):
    """BarracksStatus

    :param bottom_melee: Whether bottom melee barracks are alive
    :type bottom_melee: bool
    :param bottom_ranged: Whether bottom ranged barracks are alive
    :type bottom_ranged: bool
    :param middle_melee: Whether middle melee barracks are alive
    :type middle_melee: bool
    :param middle_ranged: Whether middle ranged barracks are alive
    :type middle_ranged: bool
    :param top_melee: Whether top melee barracks are alive
    :type top_melee: bool
    :param top_ranged: Whether top ranged barracks are alive
    :type top_ranged: bool
    """

    def __init__(
        self,
        bottom_melee: bool,
        bottom_ranged: bool,
        middle_melee: bool,
        middle_ranged: bool,
        top_melee: bool,
        top_ranged: bool,
    ):
        self.bottom_melee = bottom_melee
        self.bottom_ranged = bottom_ranged
        self.middle_melee = middle_melee
        self.middle_ranged = middle_ranged
        self.top_melee = top_melee
        self.top_ranged = top_ranged


@JsonMap({})
class TowerStatus(BaseModel):
    """TowerStatus

    :param ancient_bottom: Whether bottom Ancient is alive
    :type ancient_bottom: bool
    :param ancient_top: Whether top Ancient is alive
    :type ancient_top: bool
    :param bottom_tier_1: Whether bottom tier 1 tower is alive
    :type bottom_tier_1: bool
    :param bottom_tier_2: Whether bottom tier 2 tower is alive
    :type bottom_tier_2: bool
    :param bottom_tier_3: Whether bottom tier 3 tower is alive
    :type bottom_tier_3: bool
    :param middle_tier_1: Whether middle tier 1 tower is alive
    :type middle_tier_1: bool
    :param middle_tier_2: Whether middle tier 2 tower is alive
    :type middle_tier_2: bool
    :param middle_tier_3: Whether middle tier 3 tower is alive
    :type middle_tier_3: bool
    :param top_tier_1: Whether top tier 1 tower is alive
    :type top_tier_1: bool
    :param top_tier_2: Whether top tier 2 tower is alive
    :type top_tier_2: bool
    :param top_tier_3: Whether top tier 3 tower is alive
    :type top_tier_3: bool
    """

    def __init__(
        self,
        ancient_bottom: bool,
        ancient_top: bool,
        bottom_tier_1: bool,
        bottom_tier_2: bool,
        bottom_tier_3: bool,
        middle_tier_1: bool,
        middle_tier_2: bool,
        middle_tier_3: bool,
        top_tier_1: bool,
        top_tier_2: bool,
        top_tier_3: bool,
    ):
        self.ancient_bottom = ancient_bottom
        self.ancient_top = ancient_top
        self.bottom_tier_1 = bottom_tier_1
        self.bottom_tier_2 = bottom_tier_2
        self.bottom_tier_3 = bottom_tier_3
        self.middle_tier_1 = middle_tier_1
        self.middle_tier_2 = middle_tier_2
        self.middle_tier_3 = middle_tier_3
        self.top_tier_1 = top_tier_1
        self.top_tier_2 = top_tier_2
        self.top_tier_3 = top_tier_3


@JsonMap({})
class Dota2GameTeam(BaseModel):
    """Team's data for a game

    :param bans: bans
    :type bans: List[int]
    :param barracks_status: barracks_status
    :type barracks_status: BarracksStatus
    :param faction: faction
    :type faction: Dota2Faction
    :param first_blood: Whether team got first blood
    :type first_blood: bool
    :param first_roshan: Whether team got first Roshan
    :type first_roshan: bool
    :param first_tower: Whether team got first tower
    :type first_tower: bool
    :param picks: picks
    :type picks: List[int]
    :param player_ids: player_ids
    :type player_ids: List[int]
    :param roshan_kills: The total number of Roshans killed by the team in the game
    :type roshan_kills: int
    :param score: score
    :type score: int
    :param team: team
    :type team: BaseTeam
    :param tower_status: tower_status
    :type tower_status: TowerStatus
    """

    def __init__(
        self,
        bans: List[int],
        barracks_status: BarracksStatus,
        faction: Dota2Faction,
        first_blood: bool,
        first_roshan: bool,
        first_tower: bool,
        picks: List[int],
        player_ids: List[int],
        roshan_kills: int,
        score: int,
        team: BaseTeam,
        tower_status: TowerStatus,
    ):
        self.bans = bans
        self.barracks_status = self._define_object(barracks_status, BarracksStatus)
        self.faction = self._enum_matching(faction, Dota2Faction.list(), "faction")
        self.first_blood = first_blood
        self.first_roshan = first_roshan
        self.first_tower = first_tower
        self.picks = picks
        self.player_ids = player_ids
        self.roshan_kills = roshan_kills
        self.score = score
        self.team = self._define_object(team, BaseTeam)
        self.tower_status = self._define_object(tower_status, TowerStatus)
