# LoLGamePlayerForStats

Player's data for a Game

**Properties**

| Name                           | Type                          | Required | Description                                                                                                                                                |
| :----------------------------- | :---------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| assists                        | int                           | ✅       |                                                                                                                                                            |
| champion                       | LoLGamePlayerForStatsChampion | ✅       |                                                                                                                                                            |
| creep_score                    | int                           | ✅       | The player's Creep Score (CS.) <br/> <br/>NB: Creep Score can be different that the number of minions killed because neutral monsters can give more score. |
| cs_at_14                       | int                           | ✅       | The player's Creep Score (CS.) at 14minutes                                                                                                                |
| deaths                         | int                           | ✅       |                                                                                                                                                            |
| flags                          | LoLFlags                      | ✅       |                                                                                                                                                            |
| game_id                        | int                           | ✅       | LoL game ID                                                                                                                                                |
| gold_earned                    | int                           | ✅       |                                                                                                                                                            |
| gold_spent                     | int                           | ✅       |                                                                                                                                                            |
| items                          | List[BaseLoLItem]             | ✅       |                                                                                                                                                            |
| kills                          | int                           | ✅       |                                                                                                                                                            |
| kills_counters                 | LoLKillCounters               | ✅       |                                                                                                                                                            |
| kills_series                   | LoLKillsSeries                | ✅       |                                                                                                                                                            |
| largest_critical_strike        | int                           | ✅       |                                                                                                                                                            |
| largest_killing_spree          | int                           | ✅       |                                                                                                                                                            |
| largest_multi_kill             | int                           | ✅       |                                                                                                                                                            |
| level                          | int                           | ✅       |                                                                                                                                                            |
| magic_damage                   | LoLGamePlayerDamageForStats   | ✅       |                                                                                                                                                            |
| masteries                      | List[LoLMastery]              | ✅       |                                                                                                                                                            |
| minions_killed                 | int                           | ✅       | The player's Creep Score (CS.)                                                                                                                             |
| opponent                       | LoLGamePlayerForStatsOpponent | ✅       |                                                                                                                                                            |
| physical_damage                | LoLGamePlayerDamageForStats   | ✅       |                                                                                                                                                            |
| player                         | BasePlayer                    | ✅       |                                                                                                                                                            |
| player_id                      | int                           | ✅       | ID of the player                                                                                                                                           |
| role                           | LoLGamePlayerForStatsRole     | ✅       |                                                                                                                                                            |
| runes                          | List[LoLRune]                 | ✅       |                                                                                                                                                            |
| runes_reforged                 | LoLPlayerRunesReforged        | ✅       |                                                                                                                                                            |
| spells                         | List[LoLSpell]                | ✅       |                                                                                                                                                            |
| team                           | BaseTeam                      | ✅       |                                                                                                                                                            |
| total_damage                   | LoLGamePlayerDamageForStats   | ✅       |                                                                                                                                                            |
| total_heal                     | int                           | ✅       |                                                                                                                                                            |
| total_time_crowd_control_dealt | int                           | ✅       |                                                                                                                                                            |
| total_units_healed             | int                           | ✅       |                                                                                                                                                            |
| true_damage                    | LoLGamePlayerDamageForStats   | ✅       |                                                                                                                                                            |
| wards                          | LoLWards                      | ✅       |                                                                                                                                                            |
| wards_placed                   | int                           | ✅       |                                                                                                                                                            |

# LoLGamePlayerForStatsChampion

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| id\_      | int  | ✅       |             |
| image_url | str  | ✅       |             |
| name      | str  | ✅       |             |

# LoLGamePlayerForStatsOpponent

# Opponent_1_4

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

# Opponent_2_4

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

# LoLGamePlayerForStatsRole

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| ADC  | str  | ✅       | "adc"       |
| JUN  | str  | ✅       | "jun"       |
| MID  | str  | ✅       | "mid"       |
| SUP  | str  | ✅       | "sup"       |
| TOP  | str  | ✅       | "top"       |

<!-- This file was generated by liblab | https://liblab.com/ -->
