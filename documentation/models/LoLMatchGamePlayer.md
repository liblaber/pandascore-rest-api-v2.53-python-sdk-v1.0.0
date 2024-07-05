# LoLMatchGamePlayer

Player's data for a Game in a LoL Match

**Properties**

| Name                    | Type                   | Required | Description      |
| :---------------------- | :--------------------- | :------- | :--------------- |
| assists                 | int                    | ✅       |                  |
| deaths                  | int                    | ✅       |                  |
| flags                   | LoLFlags               | ✅       |                  |
| kills                   | int                    | ✅       |                  |
| kills_counters          | LoLKillCounters        | ✅       |                  |
| kills_series            | LoLKillsSeries         | ✅       |                  |
| largest_critical_strike | int                    | ✅       |                  |
| largest_killing_spree   | int                    | ✅       |                  |
| largest_multi_kill      | int                    | ✅       |                  |
| player_id               | int                    | ✅       | ID of the player |
| role                    | LoLMatchGamePlayerRole | ✅       |                  |

# LoLMatchGamePlayerRole

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| ADC  | str  | ✅       | "adc"       |
| JUN  | str  | ✅       | "jun"       |
| MID  | str  | ✅       | "mid"       |
| SUP  | str  | ✅       | "sup"       |
| TOP  | str  | ✅       | "top"       |
