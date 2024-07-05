# LoLStatsForTeam

Aggregated statistics for a team grouped by serie

**Properties**

| Name                | Type                     | Required | Description                      |
| :------------------ | :----------------------- | :------- | :------------------------------- |
| acronym             | str                      | ✅       |                                  |
| id\_                | int                      | ✅       |                                  |
| image_url           | str                      | ✅       | URL of the team logo             |
| last_games          | List[LoLTeamLastGame]    | ✅       |                                  |
| location            | str                      | ✅       | The team's organization location |
| modified_at         | str                      | ✅       |                                  |
| most_banned         | List[LoLBannedChampion]  | ✅       |                                  |
| most_banned_against | List[LoLBannedChampion]  | ✅       |                                  |
| most_picked         | List[LoLPickedChampion]  | ✅       |                                  |
| name                | str                      | ✅       | The name of the team.            |
| players             | List[BasePlayer]         | ✅       |                                  |
| slug                | str                      | ✅       |                                  |
| stats               | List[LoLTeamBySerieStat] | ✅       |                                  |
| total_stats         | LoLTotalTeamStat         | ✅       | Total Team's statistics          |
