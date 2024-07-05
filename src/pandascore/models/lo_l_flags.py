from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class LoLFlags(BaseModel):
    """LoLFlags

    :param first_blood_assist: Whether player got first blood assist
    :type first_blood_assist: bool
    :param first_blood_kill: Whether player got first blood kill
    :type first_blood_kill: bool
    :param first_inhibitor_assist: Whether player got first inhibitor assist
    :type first_inhibitor_assist: bool
    :param first_inhibitor_kill: Whether player got first inhibitor kill
    :type first_inhibitor_kill: bool
    :param first_tower_assist: Whether player got first tower assist
    :type first_tower_assist: bool
    :param first_tower_kill: Whether player got first tower kill
    :type first_tower_kill: bool
    """

    def __init__(
        self,
        first_blood_assist: bool,
        first_blood_kill: bool,
        first_inhibitor_assist: bool,
        first_inhibitor_kill: bool,
        first_tower_assist: bool,
        first_tower_kill: bool,
    ):
        self.first_blood_assist = first_blood_assist
        self.first_blood_kill = first_blood_kill
        self.first_inhibitor_assist = first_inhibitor_assist
        self.first_inhibitor_kill = first_inhibitor_kill
        self.first_tower_assist = first_tower_assist
        self.first_tower_kill = first_tower_kill
