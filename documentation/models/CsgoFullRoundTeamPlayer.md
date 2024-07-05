# CsgoFullRoundTeamPlayer

**Properties**

| Name                | Type                       | Required | Description                                     |
| :------------------ | :------------------------- | :------- | :---------------------------------------------- |
| assists             | int                        | ✅       | Player's number of kill assists for a game      |
| freeze_time_economy | CsgoFullRoundPlayerEconomy | ✅       |                                                 |
| id\_                | int                        | ✅       | ID of the player                                |
| is_alive            | bool                       | ✅       | Whether the player is alive or not              |
| kills               | int                        | ✅       | Player's number of kills                        |
| name                | str                        | ✅       | Professional name of the player                 |
| remaining_hp        | int                        | ✅       | Number of health points at the end of the round |
| round_start_economy | CsgoFullRoundPlayerEconomy | ✅       |                                                 |
