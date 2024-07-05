from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_event_neutral_minion_object import LoLEventNeutralMinionObject


class LoLEventNeutralMinionType(Enum):
    """An enumeration representing different categories.

    :cvar NEUTRAL_MINION: "neutral_minion"
    :vartype NEUTRAL_MINION: str
    """

    NEUTRAL_MINION = "neutral_minion"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, LoLEventNeutralMinionType._member_map_.values())
        )


@JsonMap({"type_": "type"})
class LoLEventNeutralMinion(BaseModel):
    """LoLEventNeutralMinion

    :param object: object
    :type object: LoLEventNeutralMinionObject
    :param type_: type_
    :type type_: LoLEventNeutralMinionType
    """

    def __init__(
        self, object: LoLEventNeutralMinionObject, type_: LoLEventNeutralMinionType
    ):
        self.object = self._define_object(object, LoLEventNeutralMinionObject)
        self.type_ = self._enum_matching(
            type_, LoLEventNeutralMinionType.list(), "type_"
        )
