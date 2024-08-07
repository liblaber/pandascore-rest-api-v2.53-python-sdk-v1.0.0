from enum import Enum


class LoLDrakeName(Enum):
    """An enumeration representing different categories.

    :cvar CHEMTECH_DRAKE: "Chemtech Drake"
    :vartype CHEMTECH_DRAKE: str
    :cvar CLOUD_DRAKE: "Cloud Drake"
    :vartype CLOUD_DRAKE: str
    :cvar ELDER_DRAKE: "Elder Drake"
    :vartype ELDER_DRAKE: str
    :cvar HEXTECH_DRAKE: "Hextech Drake"
    :vartype HEXTECH_DRAKE: str
    :cvar INFERNAL_DRAKE: "Infernal Drake"
    :vartype INFERNAL_DRAKE: str
    :cvar MOUNTAIN_DRAKE: "Mountain Drake"
    :vartype MOUNTAIN_DRAKE: str
    :cvar OCEAN_DRAKE: "Ocean Drake"
    :vartype OCEAN_DRAKE: str
    """

    CHEMTECH_DRAKE = "Chemtech Drake"
    CLOUD_DRAKE = "Cloud Drake"
    ELDER_DRAKE = "Elder Drake"
    HEXTECH_DRAKE = "Hextech Drake"
    INFERNAL_DRAKE = "Infernal Drake"
    MOUNTAIN_DRAKE = "Mountain Drake"
    OCEAN_DRAKE = "Ocean Drake"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLDrakeName._member_map_.values()))
