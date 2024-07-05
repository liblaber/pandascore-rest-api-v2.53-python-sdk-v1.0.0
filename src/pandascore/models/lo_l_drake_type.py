from enum import Enum


class LoLDrakeType(Enum):
    """An enumeration representing different categories.

    :cvar CHEMTECH: "chemtech"
    :vartype CHEMTECH: str
    :cvar CLOUD: "cloud"
    :vartype CLOUD: str
    :cvar ELDER: "elder"
    :vartype ELDER: str
    :cvar HEXTECH: "hextech"
    :vartype HEXTECH: str
    :cvar INFERNAL: "infernal"
    :vartype INFERNAL: str
    :cvar MOUNTAIN: "mountain"
    :vartype MOUNTAIN: str
    :cvar OCEAN: "ocean"
    :vartype OCEAN: str
    """

    CHEMTECH = "chemtech"
    CLOUD = "cloud"
    ELDER = "elder"
    HEXTECH = "hextech"
    INFERNAL = "infernal"
    MOUNTAIN = "mountain"
    OCEAN = "ocean"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLDrakeType._member_map_.values()))
