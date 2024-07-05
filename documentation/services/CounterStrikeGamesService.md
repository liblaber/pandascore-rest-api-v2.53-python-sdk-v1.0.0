# CounterStrikeGamesService

A list of all methods in the `CounterStrikeGamesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                             | Description                                 |
| :---------------------------------------------------------------------------------- | :------------------------------------------ |
| [get_csgo_games_csgo_game_id](#get_csgo_games_csgo_game_id)                         | Get a single Counter-Strike game by ID      |
| [get_csgo_games_csgo_game_id_events](#get_csgo_games_csgo_game_id_events)           | List events for a given Counter-Strike game |
| [get_csgo_games_csgo_game_id_rounds](#get_csgo_games_csgo_game_id_rounds)           | List rounds in a Counter-Strike game        |
| [get_csgo_matches_match_id_or_slug_games](#get_csgo_matches_match_id_or_slug_games) | List games for a given Counter-Strike match |

## get_csgo_games_csgo_game_id

Get a single Counter-Strike game by ID

- HTTP Method: `GET`
- Endpoint: `/csgo/games/{csgo_game_id}`

**Parameters**

| Name         | Type | Required | Description              |
| :----------- | :--- | :------- | :----------------------- |
| csgo_game_id | int  | ✅       | A Counter-Strike game ID |

**Return Type**

`CsgoGame`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.counter_strike_games.get_csgo_games_csgo_game_id(csgo_game_id=4)

print(result)
```

## get_csgo_games_csgo_game_id_events

List events for a given Counter-Strike game

- HTTP Method: `GET`
- Endpoint: `/csgo/games/{csgo_game_id}/events`

**Parameters**

| Name         | Type                      | Required | Description                                                          |
| :----------- | :------------------------ | :------- | :------------------------------------------------------------------- |
| csgo_game_id | int                       | ✅       | A Counter-Strike game ID                                             |
| page         | [Page](../models/Page.md) | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2` |
| per_page     | int                       | ❌       | Equivalent to `page[size]`                                           |

**Return Type**

`List[CsgoEvent]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
page=1

result = sdk.counter_strike_games.get_csgo_games_csgo_game_id_events(
    csgo_game_id=2,
    page=page,
    per_page=50
)

print(result)
```

## get_csgo_games_csgo_game_id_rounds

List rounds in a Counter-Strike game

- HTTP Method: `GET`
- Endpoint: `/csgo/games/{csgo_game_id}/rounds`

**Parameters**

| Name         | Type                      | Required | Description                                                          |
| :----------- | :------------------------ | :------- | :------------------------------------------------------------------- |
| csgo_game_id | int                       | ✅       | A Counter-Strike game ID                                             |
| page         | [Page](../models/Page.md) | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2` |
| per_page     | int                       | ❌       | Equivalent to `page[size]`                                           |

**Return Type**

`List[CsgoFullRound]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
page=1

result = sdk.counter_strike_games.get_csgo_games_csgo_game_id_rounds(
    csgo_game_id=2,
    page=page,
    per_page=50
)

print(result)
```

## get_csgo_matches_match_id_or_slug_games

List games for a given Counter-Strike match

- HTTP Method: `GET`
- Endpoint: `/csgo/matches/{match_id_or_slug}/games`

**Parameters**

| Name             | Type                                                    | Required | Description                                                                                                                                         |
| :--------------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| match_id_or_slug | [MatchIdOrSlug](../models/MatchIdOrSlug.md)             | ✅       | A match ID or slug                                                                                                                                  |
| filter           | [FilterOverCsgoGames](../models/FilterOverCsgoGames.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range            | [RangeOverCsgoGames](../models/RangeOverCsgoGames.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort             | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search           | [SearchOverCsgoGames](../models/SearchOverCsgoGames.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page             | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page         | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[CsgoGame]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCsgoGames, RangeOverCsgoGames, SearchOverCsgoGames

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
match_id_or_slug=8
filter=FilterOverCsgoGames(
    begin_at=[
        "eu"
    ],
    complete=False,
    detailed_stats=True,
    end_at=[
        "sit"
    ],
    finished=True,
    forfeit=False,
    id_=[
        8
    ],
    length=[
        9
    ],
    match_id=[
        2
    ],
    position=[
        10
    ],
    status=[
        "finished"
    ]
)
range=RangeOverCsgoGames(
    begin_at=[
        "enim mini"
    ],
    complete=[
        False
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "nulla"
    ],
    finished=[
        True
    ],
    forfeit=[
        True
    ],
    id_=[
        9
    ],
    length=[
        6
    ],
    match_id=[
        4
    ],
    position=[
        4
    ],
    status=[
        "finished"
    ]
)
sort=[
    ""
]
search=SearchOverCsgoGames(
    status="finished"
)
page=1

result = sdk.counter_strike_games.get_csgo_matches_match_id_or_slug_games(
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
