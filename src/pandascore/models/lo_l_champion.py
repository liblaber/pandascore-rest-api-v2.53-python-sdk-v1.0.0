from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class LoLChampion(BaseModel):
    """LoLChampion

    :param armor: armor
    :type armor: float
    :param armorperlevel: armorperlevel
    :type armorperlevel: float
    :param attackdamage: attackdamage
    :type attackdamage: float
    :param attackdamageperlevel: attackdamageperlevel
    :type attackdamageperlevel: float
    :param attackrange: attackrange
    :type attackrange: float
    :param attackspeedoffset: attackspeedoffset
    :type attackspeedoffset: float
    :param attackspeedperlevel: attackspeedperlevel
    :type attackspeedperlevel: float
    :param big_image_url: big_image_url
    :type big_image_url: str
    :param crit: crit
    :type crit: float
    :param critperlevel: critperlevel
    :type critperlevel: float
    :param hp: hp
    :type hp: float
    :param hpperlevel: hpperlevel
    :type hpperlevel: float
    :param hpregen: hpregen
    :type hpregen: float
    :param hpregenperlevel: hpregenperlevel
    :type hpregenperlevel: float
    :param id_: id_
    :type id_: int
    :param image_url: image_url
    :type image_url: str
    :param movespeed: movespeed
    :type movespeed: float
    :param mp: mp
    :type mp: float
    :param mpperlevel: mpperlevel
    :type mpperlevel: float
    :param mpregen: mpregen
    :type mpregen: float
    :param mpregenperlevel: mpregenperlevel
    :type mpregenperlevel: float
    :param name: name
    :type name: str
    :param spellblock: spellblock
    :type spellblock: float
    :param spellblockperlevel: spellblockperlevel
    :type spellblockperlevel: float
    :param videogame_versions: Array of of video game versions (ie. patches) for this resource
    :type videogame_versions: List[str]
    """

    def __init__(
        self,
        armor: float,
        armorperlevel: float,
        attackdamage: float,
        attackdamageperlevel: float,
        attackrange: float,
        attackspeedoffset: float,
        attackspeedperlevel: float,
        big_image_url: str,
        crit: float,
        critperlevel: float,
        hp: float,
        hpperlevel: float,
        hpregen: float,
        hpregenperlevel: float,
        id_: int,
        image_url: str,
        movespeed: float,
        mp: float,
        mpperlevel: float,
        mpregen: float,
        mpregenperlevel: float,
        name: str,
        spellblock: float,
        spellblockperlevel: float,
        videogame_versions: List[str],
    ):
        self.armor = armor
        self.armorperlevel = armorperlevel
        self.attackdamage = attackdamage
        self.attackdamageperlevel = attackdamageperlevel
        self.attackrange = attackrange
        self.attackspeedoffset = attackspeedoffset
        self.attackspeedperlevel = attackspeedperlevel
        self.big_image_url = big_image_url
        self.crit = crit
        self.critperlevel = critperlevel
        self.hp = hp
        self.hpperlevel = hpperlevel
        self.hpregen = hpregen
        self.hpregenperlevel = hpregenperlevel
        self.id_ = id_
        self.image_url = image_url
        self.movespeed = movespeed
        self.mp = mp
        self.mpperlevel = mpperlevel
        self.mpregen = mpregen
        self.mpregenperlevel = mpregenperlevel
        self.name = name
        self.spellblock = spellblock
        self.spellblockperlevel = spellblockperlevel
        self.videogame_versions = videogame_versions
