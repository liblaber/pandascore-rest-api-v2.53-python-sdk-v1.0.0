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
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.counter_strike_games.get_csgo_games_csgo_game_id(csgo_game_id=5)

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
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
page=1

result = sdk.counter_strike_games.get_csgo_games_csgo_game_id_events(
    csgo_game_id=10,
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
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
page=1

result = sdk.counter_strike_games.get_csgo_games_csgo_game_id_rounds(
    csgo_game_id=3,
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCsgoGames, RangeOverCsgoGames, SearchOverCsgoGames

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
match_id_or_slug=5
filter=FilterOverCsgoGames(
    begin_at=[
        "ad anim ut i"
    ],
    complete=True,
    detailed_stats=False,
    end_at=[
        "reprehende"
    ],
    finished=True,
    forfeit=True,
    id_=[
        6
    ],
    length=[
        7
    ],
    match_id=[
        1
    ],
    position=[
        9
    ],
    status=[
        "finished"
    ]
)
range=RangeOverCsgoGames(
    begin_at=[
        "i"
    ],
    complete=[
        False
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "en"
    ],
    finished=[
        True
    ],
    forfeit=[
        False
    ],
    id_=[
        1
    ],
    length=[
        7
    ],
    match_id=[
        8
    ],
    position=[
        9
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

<!-- This file was generated by liblab | https://liblab.com/ -->
