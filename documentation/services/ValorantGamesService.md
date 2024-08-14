# ValorantGamesService

A list of all methods in the `ValorantGamesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                     | Description                           |
| :------------------------------------------------------------------------------------------ | :------------------------------------ |
| [get_valorant_games_valorant_game_id](#get_valorant_games_valorant_game_id)                 | Get a single Valorant game by ID      |
| [get_valorant_games_valorant_game_id_events](#get_valorant_games_valorant_game_id_events)   | List events for a given Valorant game |
| [get_valorant_games_valorant_game_id_rounds](#get_valorant_games_valorant_game_id_rounds)   | List rounds in a Valorant game        |
| [get_valorant_matches_match_id_or_slug_games](#get_valorant_matches_match_id_or_slug_games) | List games for a given Valorant match |

## get_valorant_games_valorant_game_id

Get a single Valorant game by ID

- HTTP Method: `GET`
- Endpoint: `/valorant/games/{valorant_game_id}`

**Parameters**

| Name             | Type | Required | Description        |
| :--------------- | :--- | :------- | :----------------- |
| valorant_game_id | int  | ✅       | A Valorant game ID |

**Return Type**

`ValorantGame`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.valorant_games.get_valorant_games_valorant_game_id(valorant_game_id=1)

print(result)
```

## get_valorant_games_valorant_game_id_events

List events for a given Valorant game

- HTTP Method: `GET`
- Endpoint: `/valorant/games/{valorant_game_id}/events`

**Parameters**

| Name             | Type                      | Required | Description                                                          |
| :--------------- | :------------------------ | :------- | :------------------------------------------------------------------- |
| valorant_game_id | int                       | ✅       | A Valorant game ID                                                   |
| page             | [Page](../models/Page.md) | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2` |
| per_page         | int                       | ❌       | Equivalent to `page[size]`                                           |

**Return Type**

`List[ValorantGameEvent]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
page=1

result = sdk.valorant_games.get_valorant_games_valorant_game_id_events(
    valorant_game_id=9,
    page=page,
    per_page=50
)

print(result)
```

## get_valorant_games_valorant_game_id_rounds

List rounds in a Valorant game

- HTTP Method: `GET`
- Endpoint: `/valorant/games/{valorant_game_id}/rounds`

**Parameters**

| Name             | Type                      | Required | Description                                                          |
| :--------------- | :------------------------ | :------- | :------------------------------------------------------------------- |
| valorant_game_id | int                       | ✅       | A Valorant game ID                                                   |
| page             | [Page](../models/Page.md) | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2` |
| per_page         | int                       | ❌       | Equivalent to `page[size]`                                           |

**Return Type**

`List[ValorantFullRound]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
page=1

result = sdk.valorant_games.get_valorant_games_valorant_game_id_rounds(
    valorant_game_id=2,
    page=page,
    per_page=50
)

print(result)
```

## get_valorant_matches_match_id_or_slug_games

List games for a given Valorant match

- HTTP Method: `GET`
- Endpoint: `/valorant/matches/{match_id_or_slug}/games`

**Parameters**

| Name             | Type                                                            | Required | Description                                                                                                                                         |
| :--------------- | :-------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| match_id_or_slug | [MatchIdOrSlug](../models/MatchIdOrSlug.md)                     | ✅       | A match ID or slug                                                                                                                                  |
| filter           | [FilterOverValorantGames](../models/FilterOverValorantGames.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range            | [RangeOverValorantGames](../models/RangeOverValorantGames.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort             | List[any]                                                       | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search           | [SearchOverValorantGames](../models/SearchOverValorantGames.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page             | [Page](../models/Page.md)                                       | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page         | int                                                             | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ValorantGame]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverValorantGames, RangeOverValorantGames, SearchOverValorantGames

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
match_id_or_slug=5
filter=FilterOverValorantGames(
    begin_at=[
        "in nisi"
    ],
    complete=False,
    detailed_stats=True,
    end_at=[
        "e"
    ],
    finished=True,
    forfeit=False,
    id_=[
        6
    ],
    length=[
        7
    ],
    position=[
        2
    ],
    status=[
        "finished"
    ]
)
range=RangeOverValorantGames(
    begin_at=[
        "au"
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
        5
    ],
    length=[
        10
    ],
    position=[
        10
    ],
    status=[
        "finished"
    ]
)
sort=[
    ""
]
search=SearchOverValorantGames(
    status="finished"
)
page=1

result = sdk.valorant_games.get_valorant_matches_match_id_or_slug_games(
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
