# OwGame

A game

**Properties**

| Name           | Type              | Required | Description                                                                         |
| :------------- | :---------------- | :------- | :---------------------------------------------------------------------------------- |
| begin_at       | str               | ✅       | The game begin time, UTC. <br/>`null` when the game status is `not_started`         |
| complete       | bool              | ✅       | Whether When `true`, the game statistics are complete and will not be updated again |
| detailed_stats | bool              | ✅       | Whether historical data is available for the game                                   |
| end_at         | str               | ✅       | The game end time, UTC. <br/>`null` when the game status is not `finished`          |
| finished       | bool              | ✅       | Whether the game is finished                                                        |
| forfeit        | bool              | ✅       | Whether the game has been forfeited                                                 |
| id\_           | int               | ✅       |                                                                                     |
| length         | int               | ✅       | Duration of the game in seconds. <br/>`null` when the game status is not `finished` |
| map            | OwGameMap         | ✅       |                                                                                     |
| match          | FullGameMatch     | ✅       | A match                                                                             |
| match_id       | int               | ✅       |                                                                                     |
| position       | int               | ✅       | Game position in the match. Starts at 1                                             |
| rounds         | List[OwGameRound] | ✅       |                                                                                     |
| status         | GameStatus        | ✅       | The game status                                                                     |
| winner         | GameWinner        | ✅       |                                                                                     |
| winner_type    | OwGameWinnerType  | ✅       |                                                                                     |

# OwGameMap

**Properties**

| Name          | Type          | Required | Description |
| :------------ | :------------ | :------- | :---------- |
| game_mode     | OwMapGameMode | ✅       |             |
| id\_          | int           | ✅       |             |
| image_url     | str           | ✅       |             |
| name          | str           | ✅       |             |
| slug          | str           | ✅       |             |
| thumbnail_url | str           | ✅       |             |

# OwGameWinnerType

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| PLAYER | str  | ✅       | "Player"    |
| TEAM   | str  | ✅       | "Team"      |
