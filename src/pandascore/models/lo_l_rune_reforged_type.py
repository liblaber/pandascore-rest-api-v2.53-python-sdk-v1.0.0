from enum import Enum


class LoLRuneReforgedType(Enum):
    """An enumeration representing different categories.

    :cvar KEYSTONE: "keystone"
    :vartype KEYSTONE: str
    :cvar PATH: "path"
    :vartype PATH: str
    :cvar SHARD: "shard"
    :vartype SHARD: str
    :cvar SLOT1: "slot1"
    :vartype SLOT1: str
    :cvar SLOT2: "slot2"
    :vartype SLOT2: str
    :cvar SLOT3: "slot3"
    :vartype SLOT3: str
    """

    KEYSTONE = "keystone"
    PATH = "path"
    SHARD = "shard"
    SLOT1 = "slot1"
    SLOT2 = "slot2"
    SLOT3 = "slot3"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLRuneReforgedType._member_map_.values()))
