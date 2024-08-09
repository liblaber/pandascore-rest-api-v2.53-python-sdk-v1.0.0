# Tournament

**Properties**

| Name            | Type                       | Required | Description                                                                                                  |
| :-------------- | :------------------------- | :------- | :----------------------------------------------------------------------------------------------------------- |
| begin_at        | str                        | ✅       |                                                                                                              |
| detailed_stats  | bool                       | ✅       | Whether the tournament is expected to have detailed statistics available                                     |
| end_at          | str                        | ✅       |                                                                                                              |
| expected_roster | List[TournamentRosterItem] | ✅       |                                                                                                              |
| has_bracket     | bool                       | ✅       | Whether the tournament has a bracket                                                                         |
| id\_            | int                        | ✅       |                                                                                                              |
| league          | BaseLeague                 | ✅       |                                                                                                              |
| league_id       | int                        | ✅       |                                                                                                              |
| live_supported  | bool                       | ✅       | Whether live is supported                                                                                    |
| matches         | List[BaseMatch]            | ✅       |                                                                                                              |
| modified_at     | str                        | ✅       |                                                                                                              |
| name            | str                        | ✅       |                                                                                                              |
| prizepool       | str                        | ✅       |                                                                                                              |
| serie           | BaseSerie                  | ✅       |                                                                                                              |
| serie_id        | int                        | ✅       |                                                                                                              |
| slug            | str                        | ✅       |                                                                                                              |
| teams           | List[BaseTeam]             | ✅       |                                                                                                              |
| tier            | TournamentTier1            | ✅       | The tier of the tournament, ranging from 'S' to 'Unranked'. Ranking 'S' > 'A' > 'B' > 'C' > 'D' > 'Unranked' |
| videogame       | dict                       | ✅       |                                                                                                              |
| videogame_title | TournamentVideogameTitle   | ✅       |                                                                                                              |
| winner_id       | TournamentWinnerId         | ✅       |                                                                                                              |
| winner_type     | TournamentWinnerType       | ✅       |                                                                                                              |

# TournamentTier_1

The tier of the tournament, ranging from 'S' to 'Unranked'. Ranking 'S' > 'A' > 'B' > 'C' > 'D' > 'Unranked'

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| A        | str  | ✅       | "a"         |
| B        | str  | ✅       | "b"         |
| C        | str  | ✅       | "c"         |
| D        | str  | ✅       | "d"         |
| S        | str  | ✅       | "s"         |
| UNRANKED | str  | ✅       | "unranked"  |

# TournamentVideogameTitle

**Properties**

| Name         | Type        | Required | Description    |
| :----------- | :---------- | :------- | :------------- |
| id\_         | int         | ✅       |                |
| name         | str         | ✅       |                |
| slug         | str         | ✅       |                |
| videogame_id | VideogameId | ✅       | A videogame ID |

# TournamentWinnerId

# TournamentWinnerType

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| PLAYER | str  | ✅       | "Player"    |
| TEAM   | str  | ✅       | "Team"      |

<!-- This file was generated by liblab | https://liblab.com/ -->
