# CsgoStatsForTeam

Team's aggregated statistics

**Properties**

| Name              | Type               | Required | Description                      |
| :---------------- | :----------------- | :------- | :------------------------------- |
| acronym           | str                | ✅       |                                  |
| current_videogame | dict               | ✅       |                                  |
| id\_              | int                | ✅       |                                  |
| image_url         | str                | ✅       | URL of the team logo             |
| last_games        | List[BaseCsgoGame] | ✅       |                                  |
| location          | str                | ✅       | The team's organization location |
| modified_at       | str                | ✅       |                                  |
| name              | str                | ✅       | The name of the team.            |
| players           | List[BasePlayer]   | ✅       |                                  |
| slug              | str                | ✅       |                                  |
| stats             | CsgoTeamStats      | ✅       | Statistics for all matches       |
