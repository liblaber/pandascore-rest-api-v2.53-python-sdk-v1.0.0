from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class LoLEventUnknownType(Enum):
    """An enumeration representing different categories.

    :cvar UNKNOWN: "unknown"
    :vartype UNKNOWN: str
    """

    UNKNOWN = "unknown"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLEventUnknownType._member_map_.values()))


@JsonMap({"type_": "type"})
class LoLEventUnknown(BaseModel):
    """LoLEventUnknown

    :param object: object, defaults to None
    :type object: any, optional
    :param type_: type_
    :type type_: LoLEventUnknownType
    """

    def __init__(self, type_: LoLEventUnknownType, object: any = None):
        if object is not None:
            self.object = object
        self.type_ = self._enum_matching(type_, LoLEventUnknownType.list(), "type_")
