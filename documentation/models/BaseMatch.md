# BaseMatch

**Properties**

| Name                  | Type              | Required | Description                              |
| :-------------------- | :---------------- | :------- | :--------------------------------------- |
| begin_at              | str               | ✅       |                                          |
| detailed_stats        | bool              | ✅       | Whether the match offers full stats      |
| draw                  | bool              | ✅       | Whether result of the match is a draw    |
| end_at                | str               | ✅       |                                          |
| forfeit               | bool              | ✅       | Whether match was forfeited              |
| game_advantage        | int               | ✅       | ID of the opponent with a game advantage |
| id\_                  | int               | ✅       |                                          |
| live                  | MatchLive         | ✅       |                                          |
| match_type            | MatchType         | ✅       |                                          |
| modified_at           | str               | ✅       |                                          |
| name                  | str               | ✅       |                                          |
| number_of_games       | int               | ✅       | Number of games                          |
| original_scheduled_at | str               | ✅       |                                          |
| rescheduled           | bool              | ✅       | Whether match has been rescheduled       |
| scheduled_at          | str               | ✅       |                                          |
| slug                  | str               | ✅       |                                          |
| status                | MatchStatus       | ✅       |                                          |
| streams_list          | List[Stream]      | ✅       |                                          |
| tournament_id         | int               | ✅       |                                          |
| winner_id             | BaseMatchWinnerId | ✅       |                                          |
| winner_type           | MatchWinnerType   | ✅       |                                          |

# BaseMatchWinnerId

<!-- This file was generated by liblab | https://liblab.com/ -->
