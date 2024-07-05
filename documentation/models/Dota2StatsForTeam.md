# Dota2StatsForTeam

Aggregated statistics for a team grouped by serie

**Properties**

| Name                | Type                       | Required | Description                      |
| :------------------ | :------------------------- | :------- | :------------------------------- |
| acronym             | str                        | ✅       |                                  |
| id\_                | int                        | ✅       |                                  |
| image_url           | str                        | ✅       | URL of the team logo             |
| last_games          | List[BaseDota2Game]        | ✅       |                                  |
| location            | str                        | ✅       | The team's organization location |
| modified_at         | str                        | ✅       |                                  |
| most_banned         | List[Dota2BannedHero]      | ✅       |                                  |
| most_banned_against | List[Dota2BannedHero]      | ✅       |                                  |
| most_picked         | List[Dota2PickedHero]      | ✅       |                                  |
| name                | str                        | ✅       | The name of the team.            |
| players             | List[BasePlayer]           | ✅       |                                  |
| slug                | str                        | ✅       |                                  |
| stats               | List[Dota2TeamBySerieStat] | ✅       |                                  |
| total_stats         | Dota2TotalTeamStat         | ✅       | Total Team's statistics          |
| videogame           | dict                       | ✅       |                                  |
