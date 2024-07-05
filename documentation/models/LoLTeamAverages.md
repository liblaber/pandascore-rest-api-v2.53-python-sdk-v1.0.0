# LoLTeamAverages

**Properties**

| Name                 | Type          | Required | Description                                                                         |
| :------------------- | :------------ | :------- | :---------------------------------------------------------------------------------- |
| assists              | float         | ✅       |                                                                                     |
| baron_kills          | float         | ✅       |                                                                                     |
| deaths               | float         | ✅       |                                                                                     |
| dragon_kills         | float         | ✅       |                                                                                     |
| game_length          | int           | ✅       | Duration of the game in seconds. <br/>`null` when the game status is not `finished` |
| gold_earned          | float         | ✅       |                                                                                     |
| herald_kill          | float         | ✅       |                                                                                     |
| inhibitor_kills      | float         | ✅       |                                                                                     |
| kills                | float         | ✅       |                                                                                     |
| ratios               | LoLTeamRatios | ✅       |                                                                                     |
| total_minions_killed | float         | ✅       |                                                                                     |
| tower_kills          | float         | ✅       |                                                                                     |
| voidgrub_kills       | float         | ✅       | The number of voidgrubs killed by a team.                                           |
| wards_placed         | float         | ✅       |                                                                                     |
