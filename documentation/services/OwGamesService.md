# OwGamesService

A list of all methods in the `OwGamesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                         | Description                            |
| :------------------------------------------------------------------------------ | :------------------------------------- |
| [get_ow_games_ow_game_id](#get_ow_games_ow_game_id)                             | Get a single Overwatch game by ID      |
| [get_ow_matches_match_id_or_slug_games](#get_ow_matches_match_id_or_slug_games) | List games for a given Overwatch match |

## get_ow_games_ow_game_id

Get a single Overwatch game by ID

- HTTP Method: `GET`
- Endpoint: `/ow/games/{ow_game_id}`

**Parameters**

| Name       | Type | Required | Description          |
| :--------- | :--- | :------- | :------------------- |
| ow_game_id | int  | ✅       | An Overwatch game ID |

**Return Type**

`OwGame`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.ow_games.get_ow_games_ow_game_id(ow_game_id=2)

print(result)
```

## get_ow_matches_match_id_or_slug_games

List games for a given Overwatch match

- HTTP Method: `GET`
- Endpoint: `/ow/matches/{match_id_or_slug}/games`

**Parameters**

| Name             | Type                                                | Required | Description                                                                                                                                         |
| :--------------- | :-------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| match_id_or_slug | [MatchIdOrSlug](../models/MatchIdOrSlug.md)         | ✅       | A match ID or slug                                                                                                                                  |
| filter           | [FilterOverOwGames](../models/FilterOverOwGames.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range            | [RangeOverOwGames](../models/RangeOverOwGames.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort             | List[any]                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search           | [SearchOverOwGames](../models/SearchOverOwGames.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page             | [Page](../models/Page.md)                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page         | int                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[OwGame]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverOwGames, RangeOverOwGames, SearchOverOwGames

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
match_id_or_slug=8
filter=FilterOverOwGames(
    begin_at=[
        "eu"
    ],
    complete=True,
    detailed_stats=True,
    end_at=[
        "si"
    ],
    finished=False,
    forfeit=False,
    id_=[
        7
    ],
    length=[
        3
    ],
    match_id=[
        6
    ],
    position=[
        4
    ],
    status=[
        "finished"
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverOwGames(
    begin_at=[
        "nis"
    ],
    complete=[
        True
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "in"
    ],
    finished=[
        False
    ],
    forfeit=[
        False
    ],
    id_=[
        6
    ],
    length=[
        8
    ],
    match_id=[
        3
    ],
    position=[
        8
    ],
    status=[
        "finished"
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverOwGames(
    status="finished",
    winner_type="Player"
)
page=1

result = sdk.ow_games.get_ow_matches_match_id_or_slug_games(
    match_id_or_slug=match_id_or_slug,
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
