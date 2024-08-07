from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class LoLTrueDamage(BaseModel):
    """LoLTrueDamage

    :param dealt: dealt
    :type dealt: int
    :param dealt_percentage: Percentage of damage dealt the player had compared to the total damage of the team
    :type dealt_percentage: float
    :param dealt_to_champions: dealt_to_champions
    :type dealt_to_champions: int
    :param dealt_to_champions_percentage: Percentage of damage dealt to champions the player had compared to the total damage of the team
    :type dealt_to_champions_percentage: float
    :param taken: taken
    :type taken: int
    """

    def __init__(
        self,
        dealt: int,
        dealt_percentage: float,
        dealt_to_champions: int,
        dealt_to_champions_percentage: float,
        taken: int,
    ):
        self.dealt = dealt
        self.dealt_percentage = dealt_percentage
        self.dealt_to_champions = dealt_to_champions
        self.dealt_to_champions_percentage = dealt_to_champions_percentage
        self.taken = taken
