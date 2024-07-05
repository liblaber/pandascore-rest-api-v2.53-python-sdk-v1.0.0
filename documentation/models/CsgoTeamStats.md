# CsgoTeamStats

Statistics for all matches

**Properties**

| Name               | Type                      | Required | Description |
| :----------------- | :------------------------ | :------- | :---------- |
| counts             | CsgoStatsCounts           | ✅       |             |
| maps               | List[CsgoTeamMapStats]    | ✅       |             |
| per_game_averages  | CsgoTeamStatsGameAverages | ✅       |             |
| per_round_averages | CsgoStatsRoundAverages    | ✅       |             |
