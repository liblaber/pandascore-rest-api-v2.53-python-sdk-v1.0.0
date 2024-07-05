from enum import Enum


class LoLEventVoidgrubValue(Enum):
    """An enumeration representing different categories.

    :cvar VOIDGRUB: "Voidgrub"
    :vartype VOIDGRUB: str
    """

    VOIDGRUB = "Voidgrub"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLEventVoidgrubValue._member_map_.values()))
