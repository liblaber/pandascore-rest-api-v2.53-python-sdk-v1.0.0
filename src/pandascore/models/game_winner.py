from enum import Enum
from typing import Union
from .utils.json_map import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel


class IdGuard(OneOfBaseModel):
    class_list = {"int": int, "int": int}


Id = Union[int, int]


class GameWinnerType2(Enum):
    """An enumeration representing different categories.

    :cvar PLAYER: "Player"
    :vartype PLAYER: str
    :cvar TEAM: "Team"
    :vartype TEAM: str
    """

    PLAYER = "Player"
    TEAM = "Team"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, GameWinnerType2._member_map_.values()))


@JsonMap({"id_": "id", "type_": "type"})
class GameWinner(BaseModel):
    """GameWinner

    :param id_: id_
    :type id_: Id
    :param type_: type_
    :type type_: GameWinnerType2
    """

    def __init__(self, id_: Id, type_: GameWinnerType2):
        self.id_ = IdGuard.return_one_of(id_)
        self.type_ = self._enum_matching(type_, GameWinnerType2.list(), "type_")
