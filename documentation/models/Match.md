# Match

**Properties**

| Name                  | Type                  | Required | Description                                                                                                                                                                                                                                                                     |
| :-------------------- | :-------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| begin_at              | str                   | ✅       |                                                                                                                                                                                                                                                                                 |
| detailed_stats        | bool                  | ✅       | Whether the match offers full stats                                                                                                                                                                                                                                             |
| draw                  | bool                  | ✅       | Whether result of the match is a draw                                                                                                                                                                                                                                           |
| end_at                | str                   | ✅       |                                                                                                                                                                                                                                                                                 |
| forfeit               | bool                  | ✅       | Whether match was forfeited                                                                                                                                                                                                                                                     |
| game_advantage        | int                   | ✅       | ID of the opponent with a game advantage                                                                                                                                                                                                                                        |
| games                 | List[Game]            | ✅       |                                                                                                                                                                                                                                                                                 |
| id\_                  | int                   | ✅       |                                                                                                                                                                                                                                                                                 |
| league                | BaseLeague            | ✅       |                                                                                                                                                                                                                                                                                 |
| league_id             | int                   | ✅       |                                                                                                                                                                                                                                                                                 |
| live                  | MatchLive             | ✅       |                                                                                                                                                                                                                                                                                 |
| match_type            | MatchType             | ✅       |                                                                                                                                                                                                                                                                                 |
| modified_at           | str                   | ✅       |                                                                                                                                                                                                                                                                                 |
| name                  | str                   | ✅       |                                                                                                                                                                                                                                                                                 |
| number_of_games       | int                   | ✅       | Number of games                                                                                                                                                                                                                                                                 |
| opponents             | List[Opponent]        | ✅       |                                                                                                                                                                                                                                                                                 |
| original_scheduled_at | str                   | ✅       |                                                                                                                                                                                                                                                                                 |
| rescheduled           | bool                  | ✅       | Whether match has been rescheduled                                                                                                                                                                                                                                              |
| results               | List[MatchResult]     | ✅       |                                                                                                                                                                                                                                                                                 |
| scheduled_at          | str                   | ✅       |                                                                                                                                                                                                                                                                                 |
| serie                 | BaseSerie             | ✅       |                                                                                                                                                                                                                                                                                 |
| serie_id              | int                   | ✅       |                                                                                                                                                                                                                                                                                 |
| slug                  | str                   | ✅       |                                                                                                                                                                                                                                                                                 |
| status                | MatchStatus           | ✅       |                                                                                                                                                                                                                                                                                 |
| streams_list          | List[Stream]          | ✅       |                                                                                                                                                                                                                                                                                 |
| tournament            | BaseTournament        | ✅       |                                                                                                                                                                                                                                                                                 |
| tournament_id         | int                   | ✅       |                                                                                                                                                                                                                                                                                 |
| videogame             | dict                  | ✅       |                                                                                                                                                                                                                                                                                 |
| videogame_title       | MatchVideogameTitle   | ✅       |                                                                                                                                                                                                                                                                                 |
| videogame_version     | MatchVideogameVersion | ✅       |                                                                                                                                                                                                                                                                                 |
| winner                | MatchWinner           | ✅       |                                                                                                                                                                                                                                                                                 |
| winner_id             | MatchWinnerId         | ✅       |                                                                                                                                                                                                                                                                                 |
| winner_type           | MatchWinnerType       | ✅       |                                                                                                                                                                                                                                                                                 |
| map_picks             | List[ValorantMapPick] | ❌       | **Only applies to Valorant matches. The field will not be present on other video games matches.** <br/>Map picks, `null` when map picks data is unavailable. <br/>**Important:** `map_picks` field is only present in the response for subscribers of Valorant Historical plan. |

# MatchVideogameTitle

**Properties**

| Name         | Type        | Required | Description    |
| :----------- | :---------- | :------- | :------------- |
| id\_         | int         | ✅       |                |
| name         | str         | ✅       |                |
| slug         | str         | ✅       |                |
| videogame_id | VideogameId | ✅       | A videogame ID |

# MatchVideogameVersion

**Properties**

| Name    | Type | Required | Description                               |
| :------ | :--- | :------- | :---------------------------------------- |
| current | bool | ✅       | Whether this videogame version is current |
| name    | str  | ✅       |                                           |

# MatchWinner

# Winner_1_1

**Properties**

| Name        | Type  | Required | Description                                                                                                                                                                                                                                    |
| :---------- | :---- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| active      | bool  | ✅       | Whether player is active                                                                                                                                                                                                                       |
| age         | float | ✅       | Age of the player, `null` if unknown. When `birthday` is `null`, `age` is an approxiamation. Read more about [players' age](/docs/about-players-age) <br/>**Note**: This field is only present for users running the Historical plan or above. |
| birthday    | str   | ✅       | Birth day of the player, `YYYY-MM-DD` format. `null` if unknown. <br/>**Note**: This field is only present for users running the Historical plan or above.                                                                                     |
| first_name  | str   | ✅       | First name of the player. `null` if unknown                                                                                                                                                                                                    |
| id\_        | int   | ✅       | ID of the player                                                                                                                                                                                                                               |
| image_url   | str   | ✅       | URL to the photo of the player. `null` if not available.                                                                                                                                                                                       |
| last_name   | str   | ✅       | Last name of the player. `null` if unknown                                                                                                                                                                                                     |
| modified_at | str   | ✅       |                                                                                                                                                                                                                                                |
| name        | str   | ✅       | Professional name of the player                                                                                                                                                                                                                |
| nationality | str   | ✅       | Country code matching the nationality of the player according to the ISO 3166-1 standard (Alpha-2 code). <br/>In addition to the standard, the `XK` code is used for Kosovo. <br/>`null` if unknown                                            |
| role        | str   | ✅       | Role/position of the player. Field value varies depending on the video game.`null` if unknown. <br/>**Note**: role is only available for DotA 2, League of Legends, and Overwatch players. <br/>`null` for other video games.                  |
| slug        | str   | ✅       | Unique, human-readable identifier for the player. <br/>`id` and `slug` can be used interchangeably throughout the API.                                                                                                                         |

# Winner_2_1

**Properties**

| Name        | Type | Required | Description                      |
| :---------- | :--- | :------- | :------------------------------- |
| acronym     | str  | ✅       |                                  |
| id\_        | int  | ✅       |                                  |
| image_url   | str  | ✅       | URL of the team logo             |
| location    | str  | ✅       | The team's organization location |
| modified_at | str  | ✅       |                                  |
| name        | str  | ✅       | The name of the team.            |
| slug        | str  | ✅       |                                  |

# MatchWinnerId

<!-- This file was generated by liblab | https://liblab.com/ -->
