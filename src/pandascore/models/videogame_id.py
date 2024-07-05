from enum import Enum


class VideogameId(Enum):
    """An enumeration representing different categories.

    :cvar _1: 1
    :vartype _1: str
    :cvar _3: 3
    :vartype _3: str
    :cvar _4: 4
    :vartype _4: str
    :cvar _14: 14
    :vartype _14: str
    :cvar _20: 20
    :vartype _20: str
    :cvar _22: 22
    :vartype _22: str
    :cvar _23: 23
    :vartype _23: str
    :cvar _24: 24
    :vartype _24: str
    :cvar _25: 25
    :vartype _25: str
    :cvar _26: 26
    :vartype _26: str
    :cvar _27: 27
    :vartype _27: str
    :cvar _28: 28
    :vartype _28: str
    :cvar _29: 29
    :vartype _29: str
    :cvar _30: 30
    :vartype _30: str
    :cvar _31: 31
    :vartype _31: str
    :cvar _32: 32
    :vartype _32: str
    :cvar _33: 33
    :vartype _33: str
    """

    _1 = 1
    _3 = 3
    _4 = 4
    _14 = 14
    _20 = 20
    _22 = 22
    _23 = 23
    _24 = 24
    _25 = 25
    _26 = 26
    _27 = 27
    _28 = 28
    _29 = 29
    _30 = 30
    _31 = 31
    _32 = 32
    _33 = 33

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, VideogameId._member_map_.values()))
