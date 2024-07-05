# BaseDota2Game

**Properties**

| Name           | Type                      | Required | Description                                                                         |
| :------------- | :------------------------ | :------- | :---------------------------------------------------------------------------------- |
| begin_at       | str                       | ✅       | The game begin time, UTC. <br/>`null` when the game status is `not_started`         |
| complete       | bool                      | ✅       | Whether When `true`, the game statistics are complete and will not be updated again |
| detailed_stats | bool                      | ✅       | Whether historical data is available for the game                                   |
| end_at         | str                       | ✅       | The game end time, UTC. <br/>`null` when the game status is not `finished`          |
| finished       | bool                      | ✅       | Whether the game is finished                                                        |
| first_blood    | int                       | ✅       |                                                                                     |
| forfeit        | bool                      | ✅       | Whether the game has been forfeited                                                 |
| id\_           | int                       | ✅       |                                                                                     |
| length         | int                       | ✅       | Duration of the game in seconds. <br/>`null` when the game status is not `finished` |
| match_id       | int                       | ✅       |                                                                                     |
| players        | List[Dota2FullGamePlayer] | ✅       |                                                                                     |
| position       | int                       | ✅       | Game position in the match. Starts at 1                                             |
| status         | GameStatus                | ✅       | The game status                                                                     |
| teams          | List[Dota2GameTeam]       | ✅       |                                                                                     |
| winner         | GameWinner                | ✅       |                                                                                     |
| winner_type    | BaseDota2GameWinnerType   | ✅       |                                                                                     |

# BaseDota2GameWinnerType

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| PLAYER | str  | ✅       | "Player"    |
| TEAM   | str  | ✅       | "Team"      |
