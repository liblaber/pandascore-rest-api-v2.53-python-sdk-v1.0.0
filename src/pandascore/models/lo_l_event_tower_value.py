from enum import Enum


class LoLEventTowerValue(Enum):
    """An enumeration representing different categories.

    :cvar TOWER: "Tower"
    :vartype TOWER: str
    """

    TOWER = "Tower"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLEventTowerValue._member_map_.values()))
