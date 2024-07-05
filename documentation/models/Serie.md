# Serie

A serie, an occurrence of a league event

**Properties**

| Name            | Type                 | Required | Description |
| :-------------- | :------------------- | :------- | :---------- |
| begin_at        | str                  | ✅       |             |
| end_at          | str                  | ✅       |             |
| full_name       | str                  | ✅       |             |
| id\_            | int                  | ✅       |             |
| league          | BaseLeague           | ✅       |             |
| league_id       | int                  | ✅       |             |
| modified_at     | str                  | ✅       |             |
| name            | str                  | ✅       |             |
| season          | str                  | ✅       |             |
| slug            | str                  | ✅       |             |
| tournaments     | List[BaseTournament] | ✅       |             |
| videogame       | dict                 | ✅       |             |
| videogame_title | SerieVideogameTitle  | ✅       |             |
| winner_id       | SerieWinnerId        | ✅       |             |
| winner_type     | SerieWinnerType      | ✅       |             |
| year            | int                  | ✅       |             |

# SerieVideogameTitle

**Properties**

| Name         | Type        | Required | Description    |
| :----------- | :---------- | :------- | :------------- |
| id\_         | int         | ✅       |                |
| name         | str         | ✅       |                |
| slug         | str         | ✅       |                |
| videogame_id | VideogameId | ✅       | A videogame ID |

# SerieWinnerId

# SerieWinnerType

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| PLAYER | str  | ✅       | "Player"    |
| TEAM   | str  | ✅       | "Team"      |
