# BaseCsgoGame

A game

**Properties**

| Name           | Type                   | Required | Description                                                                         |
| :------------- | :--------------------- | :------- | :---------------------------------------------------------------------------------- |
| begin_at       | str                    | ✅       | The game begin time, UTC. <br/>`null` when the game status is `not_started`         |
| complete       | bool                   | ✅       | Whether When `true`, the game statistics are complete and will not be updated again |
| detailed_stats | bool                   | ✅       | Whether historical data is available for the game                                   |
| end_at         | str                    | ✅       | The game end time, UTC. <br/>`null` when the game status is not `finished`          |
| finished       | bool                   | ✅       | Whether the game is finished                                                        |
| forfeit        | bool                   | ✅       | Whether the game has been forfeited                                                 |
| id\_           | int                    | ✅       | Counter-Strike game ID                                                              |
| length         | int                    | ✅       | Duration of the game in seconds. <br/>`null` when the game status is not `finished` |
| map            | BaseCsgoGameMap        | ✅       |                                                                                     |
| match_id       | int                    | ✅       |                                                                                     |
| players        | List[CsgoGamePlayer]   | ✅       |                                                                                     |
| position       | int                    | ✅       | Game position in the match. Starts at 1                                             |
| rounds         | List[CsgoRound]        | ✅       |                                                                                     |
| rounds_score   | List[CsgoRoundsScore]  | ✅       |                                                                                     |
| status         | GameStatus             | ✅       | The game status                                                                     |
| teams          | List[BaseTeam]         | ✅       |                                                                                     |
| winner         | GameWinner             | ✅       |                                                                                     |
| winner_type    | BaseCsgoGameWinnerType | ✅       |                                                                                     |

# BaseCsgoGameMap

**Properties**

| Name      | Type | Required | Description                          |
| :-------- | :--- | :------- | :----------------------------------- |
| id\_      | int  | ✅       | The ID of the map.                   |
| image_url | str  | ✅       | A URL to the image of the map.       |
| name      | str  | ✅       | The name of the map.                 |
| slug      | str  | ✅       | Human-readable identifier of the map |

# BaseCsgoGameWinnerType

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| PLAYER | str  | ✅       | "Player"    |
| TEAM   | str  | ✅       | "Team"      |
