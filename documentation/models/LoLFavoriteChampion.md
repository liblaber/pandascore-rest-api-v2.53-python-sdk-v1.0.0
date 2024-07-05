# LoLFavoriteChampion

A player's most used champion

**Properties**

| Name            | Type              | Required | Description                                              |
| :-------------- | :---------------- | :------- | :------------------------------------------------------- |
| champion        | LoLChampion       | ✅       |                                                          |
| games_count     | int               | ✅       | Number of games                                          |
| games_lost      | int               | ✅       | Number of games lost by the player on the given champion |
| games_won       | int               | ✅       | Number of games won by the player on the given champion  |
| most_used_items | List[LoLUsedItem] | ✅       |                                                          |
