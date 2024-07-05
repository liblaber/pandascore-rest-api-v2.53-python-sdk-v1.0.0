from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class LoLRunePathRunesObject(BaseModel):
    """LoLRunePathRunesObject

    :param keystones: IDs of the keystone runes available for this path
    :type keystones: List[int]
    :param slot1: IDs of the slot 1 runes available for this path
    :type slot1: List[int]
    :param slot2: IDs of the slot 2 runes available for this path
    :type slot2: List[int]
    :param slot3: IDs of the slot 3 runes available for this path
    :type slot3: List[int]
    """

    def __init__(
        self, keystones: List[int], slot1: List[int], slot2: List[int], slot3: List[int]
    ):
        self.keystones = keystones
        self.slot1 = slot1
        self.slot2 = slot2
        self.slot3 = slot3
