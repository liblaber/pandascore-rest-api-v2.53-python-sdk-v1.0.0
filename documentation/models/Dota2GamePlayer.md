# Dota2GamePlayer

Player's data for a game

**Properties**

| Name                     | Type                      | Required | Description                             |
| :----------------------- | :------------------------ | :------- | :-------------------------------------- |
| abilities                | List[Dota2PerHeroAbility] | ✅       |                                         |
| assists                  | int                       | ✅       | Player's number of assists for a game   |
| camps_stacked            | int                       | ✅       |                                         |
| creeps_stacked           | int                       | ✅       |                                         |
| damage_taken             | int                       | ✅       |                                         |
| deaths                   | int                       | ✅       |                                         |
| denies                   | int                       | ✅       | Number of denies performed by a player  |
| faction                  | Dota2GamePlayerFaction    | ✅       |                                         |
| game_id                  | int                       | ✅       |                                         |
| gold_per_min             | int                       | ✅       |                                         |
| gold_remaining           | int                       | ✅       |                                         |
| gold_spent               | int                       | ✅       |                                         |
| heal                     | int                       | ✅       | Healing (in HP) performed by the player |
| hero                     | Dota2GamePlayerHero       | ✅       |                                         |
| hero_damage              | int                       | ✅       |                                         |
| hero_level               | int                       | ✅       |                                         |
| items                    | List[Dota2Item]           | ✅       |                                         |
| kills                    | int                       | ✅       |                                         |
| lane_creep               | int                       | ✅       |                                         |
| last_hits                | int                       | ✅       |                                         |
| net_worth                | int                       | ✅       | Net worth of the player                 |
| neutral_creep            | int                       | ✅       |                                         |
| observer_used            | int                       | ✅       |                                         |
| observer_wards_destroyed | int                       | ✅       |                                         |
| observer_wards_purchased | int                       | ✅       |                                         |
| opponent                 | Dota2GamePlayerOpponent   | ✅       |                                         |
| player                   | BasePlayer                | ✅       |                                         |
| role                     | int                       | ✅       | Position of the player (1, 2, 3, 4, 5)  |
| sentry_used              | int                       | ✅       |                                         |
| sentry_wards_destroyed   | int                       | ✅       |                                         |
| sentry_wards_purchased   | int                       | ✅       |                                         |
| team_id                  | int                       | ✅       |                                         |
| tower_damage             | int                       | ✅       |                                         |
| tower_kills              | int                       | ✅       |                                         |
| xp_per_min               | int                       | ✅       |                                         |

# Dota2GamePlayerFaction

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| DIRE    | str  | ✅       | "dire"      |
| RADIANT | str  | ✅       | "radiant"   |

# Dota2GamePlayerHero

**Properties**

| Name           | Type | Required | Description |
| :------------- | :--- | :------- | :---------- |
| id\_           | int  | ✅       |             |
| image_url      | str  | ✅       |             |
| localized_name | str  | ✅       |             |
| name           | str  | ✅       |             |

# Dota2GamePlayerOpponent

# Opponent_1_2

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

# Opponent_2_2

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
