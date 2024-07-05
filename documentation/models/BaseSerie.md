# BaseSerie

**Properties**

| Name        | Type                | Required | Description |
| :---------- | :------------------ | :------- | :---------- |
| begin_at    | str                 | ✅       |             |
| end_at      | str                 | ✅       |             |
| full_name   | str                 | ✅       |             |
| id\_        | int                 | ✅       |             |
| league_id   | int                 | ✅       |             |
| modified_at | str                 | ✅       |             |
| name        | str                 | ✅       |             |
| season      | str                 | ✅       |             |
| slug        | str                 | ✅       |             |
| winner_id   | BaseSerieWinnerId   | ✅       |             |
| winner_type | BaseSerieWinnerType | ✅       |             |
| year        | int                 | ✅       |             |

# BaseSerieWinnerId

# BaseSerieWinnerType

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| PLAYER | str  | ✅       | "Player"    |
| TEAM   | str  | ✅       | "Team"      |
