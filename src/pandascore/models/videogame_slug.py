from enum import Enum


class VideogameSlug(Enum):
    """An enumeration representing different categories.

    :cvar COD_MW: "cod-mw"
    :vartype COD_MW: str
    :cvar CS_GO: "cs-go"
    :vartype CS_GO: str
    :cvar DOTA_2: "dota-2"
    :vartype DOTA_2: str
    :cvar E_BASKETBALL: "e-basketball"
    :vartype E_BASKETBALL: str
    :cvar E_CRICKET: "e-cricket"
    :vartype E_CRICKET: str
    :cvar E_SOCCER: "e-soccer"
    :vartype E_SOCCER: str
    :cvar FIFA: "fifa"
    :vartype FIFA: str
    :cvar KOG: "kog"
    :vartype KOG: str
    :cvar LEAGUE_OF_LEGENDS: "league-of-legends"
    :vartype LEAGUE_OF_LEGENDS: str
    :cvar LOL_WILD_RIFT: "lol-wild-rift"
    :vartype LOL_WILD_RIFT: str
    :cvar OW: "ow"
    :vartype OW: str
    :cvar PUBG: "pubg"
    :vartype PUBG: str
    :cvar R6_SIEGE: "r6-siege"
    :vartype R6_SIEGE: str
    :cvar RL: "rl"
    :vartype RL: str
    :cvar STARCRAFT_2: "starcraft-2"
    :vartype STARCRAFT_2: str
    :cvar STARCRAFT_BROOD_WAR: "starcraft-brood-war"
    :vartype STARCRAFT_BROOD_WAR: str
    :cvar VALORANT: "valorant"
    :vartype VALORANT: str
    """

    COD_MW = "cod-mw"
    CS_GO = "cs-go"
    DOTA_2 = "dota-2"
    E_BASKETBALL = "e-basketball"
    E_CRICKET = "e-cricket"
    E_SOCCER = "e-soccer"
    FIFA = "fifa"
    KOG = "kog"
    LEAGUE_OF_LEGENDS = "league-of-legends"
    LOL_WILD_RIFT = "lol-wild-rift"
    OW = "ow"
    PUBG = "pubg"
    R6_SIEGE = "r6-siege"
    RL = "rl"
    STARCRAFT_2 = "starcraft-2"
    STARCRAFT_BROOD_WAR = "starcraft-brood-war"
    VALORANT = "valorant"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, VideogameSlug._member_map_.values()))
