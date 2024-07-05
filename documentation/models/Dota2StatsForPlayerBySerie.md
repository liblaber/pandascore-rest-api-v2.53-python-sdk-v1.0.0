# Dota2StatsForPlayerBySerie

Player's aggregated statistics for a serie

**Properties**

| Name              | Type                                  | Required | Description                                                                                                                                                                                                                                    |
| :---------------- | :------------------------------------ | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| active            | bool                                  | ✅       | Whether player is active                                                                                                                                                                                                                       |
| age               | float                                 | ✅       | Age of the player, `null` if unknown. When `birthday` is `null`, `age` is an approxiamation. Read more about [players' age](/docs/about-players-age) <br/>**Note**: This field is only present for users running the Historical plan or above. |
| birthday          | str                                   | ✅       | Birth day of the player, `YYYY-MM-DD` format. `null` if unknown. <br/>**Note**: This field is only present for users running the Historical plan or above.                                                                                     |
| current_team      | Dota2StatsForPlayerBySerieCurrentTeam | ✅       |                                                                                                                                                                                                                                                |
| current_videogame | dict                                  | ✅       |                                                                                                                                                                                                                                                |
| favorite_heroes   | List[Dota2FavoriteHero]               | ✅       |                                                                                                                                                                                                                                                |
| first_name        | str                                   | ✅       | First name of the player. `null` if unknown                                                                                                                                                                                                    |
| id\_              | int                                   | ✅       | ID of the player                                                                                                                                                                                                                               |
| image_url         | str                                   | ✅       | URL to the photo of the player. `null` if not available.                                                                                                                                                                                       |
| last_games        | List[Dota2GamePlayer]                 | ✅       |                                                                                                                                                                                                                                                |
| last_name         | str                                   | ✅       | Last name of the player. `null` if unknown                                                                                                                                                                                                     |
| modified_at       | str                                   | ✅       |                                                                                                                                                                                                                                                |
| name              | str                                   | ✅       | Professional name of the player                                                                                                                                                                                                                |
| nationality       | str                                   | ✅       | Country code matching the nationality of the player according to the ISO 3166-1 standard (Alpha-2 code). <br/>In addition to the standard, the `XK` code is used for Kosovo. <br/>`null` if unknown                                            |
| role              | str                                   | ✅       | Role/position of the player. Field value varies depending on the video game.`null` if unknown. <br/>**Note**: role is only available for DotA 2, League of Legends, and Overwatch players. <br/>`null` for other video games.                  |
| slug              | str                                   | ✅       | Unique, human-readable identifier for the player. <br/>`id` and `slug` can be used interchangeably throughout the API.                                                                                                                         |
| stats             | Dota2PlayerBySerieStat                | ✅       | Player's statistics for a serie                                                                                                                                                                                                                |
| teams             | List[BaseTeam]                        | ✅       |                                                                                                                                                                                                                                                |

# Dota2StatsForPlayerBySerieCurrentTeam

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
