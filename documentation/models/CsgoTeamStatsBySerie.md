# CsgoTeamStatsBySerie

Statistics for a serie

**Properties**

| Name               | Type                      | Required | Description                              |
| :----------------- | :------------------------ | :------- | :--------------------------------------- |
| counts             | CsgoStatsCounts           | ✅       |                                          |
| maps               | List[CsgoTeamMapStats]    | ✅       |                                          |
| per_game_averages  | CsgoTeamStatsGameAverages | ✅       |                                          |
| per_round_averages | CsgoStatsRoundAverages    | ✅       |                                          |
| serie              | Serie                     | ✅       | A serie, an occurrence of a league event |
