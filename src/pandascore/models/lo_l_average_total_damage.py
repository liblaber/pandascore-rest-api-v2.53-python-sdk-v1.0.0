from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class LoLAverageTotalDamage(BaseModel):
    """LoLAverageTotalDamage

    :param dealt: dealt
    :type dealt: float
    :param dealt_percentage: Percentage of damage dealt the player had compared to the total damage of the team
    :type dealt_percentage: float
    :param dealt_to_champions: dealt_to_champions
    :type dealt_to_champions: float
    :param dealt_to_champions_percentage: Percentage of damage dealt to champions the player had compared to the total damage of the team
    :type dealt_to_champions_percentage: float
    :param taken: taken
    :type taken: float
    """

    def __init__(
        self,
        dealt: float,
        dealt_percentage: float,
        dealt_to_champions: float,
        dealt_to_champions_percentage: float,
        taken: float,
    ):
        self.dealt = dealt
        self.dealt_percentage = dealt_percentage
        self.dealt_to_champions = dealt_to_champions
        self.dealt_to_champions_percentage = dealt_to_champions_percentage
        self.taken = taken
