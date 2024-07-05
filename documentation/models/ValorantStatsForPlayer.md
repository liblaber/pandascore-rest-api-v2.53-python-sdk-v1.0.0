# ValorantStatsForPlayer

**Properties**

| Name                     | Type                     | Required | Description                                               |
| :----------------------- | :----------------------- | :------- | :-------------------------------------------------------- |
| agents                   | List[ValorantAgentStats] | ✅       | Agents picks, wins, and losses stats for this map         |
| assists                  | int                      | ✅       | Number of player's assists                                |
| average_damage_per_round | float                    | ✅       | Average damage per round (ADR) of the player              |
| clutch_wins              | ValorantPlayerClutchWins | ✅       | Round wins when the player was the last team member alive |
| deaths                   | int                      | ✅       | Number of player's death                                  |
| defused_spikes           | int                      | ✅       | Number of spikes defused by the player                    |
| first_deaths             | int                      | ✅       | Number of rounds where the player died first              |
| first_kill_percentage    | float                    | ✅       | First kill percentage of the player                       |
| first_kills              | int                      | ✅       | Number of rounds where the player did the first kill      |
| headshot_percentage      | float                    | ✅       | Percentage of headshots within the player's shots         |
| kills                    | int                      | ✅       | Number of player's kills                                  |
| last_games               | List[ValorantGamePlayer] | ✅       |                                                           |
| planted_spikes           | int                      | ✅       | Number of spikes planted by the player                    |
| player                   | BasePlayer               | ✅       |                                                           |
| streaks                  | ValorantPlayerStreaks    | ✅       | Streaks done by the player (in a given round)             |
| total_games              | int                      | ✅       | Amount of games played by the player                      |
