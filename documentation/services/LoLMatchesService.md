# LoLMatchesService

A list of all methods in the `LoLMatchesService` service. Click on the method name to view detailed information about that method.

| Methods                                                               | Description                                        |
| :-------------------------------------------------------------------- | :------------------------------------------------- |
| [get_lol_matches](#get_lol_matches)                                   | List matches for the League of Legends videogame   |
| [get_lol_matches_past](#get_lol_matches_past)                         | List past League of Legends matches                |
| [get_lol_matches_running](#get_lol_matches_running)                   | List running League of Legends matches             |
| [get_lol_matches_upcoming](#get_lol_matches_upcoming)                 | List upcoming League of Legends matches            |
| [get_lol_matches_match_id_or_slug](#get_lol_matches_match_id_or_slug) | Get a single League of Legends match by ID or slug |

## get_lol_matches

List matches for the League of Legends videogame

- HTTP Method: `GET`
- Endpoint: `/lol/matches`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLMatches](../models/FilterOverLoLMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLMatches](../models/RangeOverLoLMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLMatches](../models/SearchOverLoLMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLMatches, RangeOverLoLMatches, SearchOverLoLMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLoLMatches(
    begin_at=[
        "nisi e"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "deserun"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        6
    ],
    league_id=[
        10
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "laborum "
    ],
    name=[
        "sint velit"
    ],
    not_started=False,
    number_of_games=[
        0
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=False,
    running=True,
    scheduled_at=[
        "Duis Lorem"
    ],
    serie_id=[
        1
    ],
    slug=[
        "rki"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        6
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        9
    ],
    videogame_version=[
        "076677.94865001934.580355685"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLoLMatches(
    begin_at=[
        "occaecat"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "velit est"
    ],
    forfeit=[
        False
    ],
    id_=[
        3
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "labori"
    ],
    name=[
        "cillum"
    ],
    number_of_games=[
        6
    ],
    scheduled_at=[
        "ad dolor qu"
    ],
    slug=[
        "XMb"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverLoLMatches(
    match_type="all_games_played",
    name="etocc",
    slug="WYcNZudjm l",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.lo_l_matches.get_lol_matches(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_matches_past

List past League of Legends matches

- HTTP Method: `GET`
- Endpoint: `/lol/matches/past`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLMatches](../models/FilterOverLoLMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLMatches](../models/RangeOverLoLMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLMatches](../models/SearchOverLoLMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLMatches, RangeOverLoLMatches, SearchOverLoLMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLoLMatches(
    begin_at=[
        "nisi e"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "deserun"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        6
    ],
    league_id=[
        10
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "laborum "
    ],
    name=[
        "sint velit"
    ],
    not_started=False,
    number_of_games=[
        0
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=False,
    running=True,
    scheduled_at=[
        "Duis Lorem"
    ],
    serie_id=[
        1
    ],
    slug=[
        "rki"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        6
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        9
    ],
    videogame_version=[
        "076677.94865001934.580355685"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLoLMatches(
    begin_at=[
        "occaecat"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "velit est"
    ],
    forfeit=[
        False
    ],
    id_=[
        3
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "labori"
    ],
    name=[
        "cillum"
    ],
    number_of_games=[
        6
    ],
    scheduled_at=[
        "ad dolor qu"
    ],
    slug=[
        "XMb"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverLoLMatches(
    match_type="all_games_played",
    name="etocc",
    slug="WYcNZudjm l",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.lo_l_matches.get_lol_matches_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_matches_running

List running League of Legends matches

- HTTP Method: `GET`
- Endpoint: `/lol/matches/running`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLMatches](../models/FilterOverLoLMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLMatches](../models/RangeOverLoLMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLMatches](../models/SearchOverLoLMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLMatches, RangeOverLoLMatches, SearchOverLoLMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLoLMatches(
    begin_at=[
        "nisi e"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "deserun"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        6
    ],
    league_id=[
        10
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "laborum "
    ],
    name=[
        "sint velit"
    ],
    not_started=False,
    number_of_games=[
        0
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=False,
    running=True,
    scheduled_at=[
        "Duis Lorem"
    ],
    serie_id=[
        1
    ],
    slug=[
        "rki"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        6
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        9
    ],
    videogame_version=[
        "076677.94865001934.580355685"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLoLMatches(
    begin_at=[
        "occaecat"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "velit est"
    ],
    forfeit=[
        False
    ],
    id_=[
        3
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "labori"
    ],
    name=[
        "cillum"
    ],
    number_of_games=[
        6
    ],
    scheduled_at=[
        "ad dolor qu"
    ],
    slug=[
        "XMb"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverLoLMatches(
    match_type="all_games_played",
    name="etocc",
    slug="WYcNZudjm l",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.lo_l_matches.get_lol_matches_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_matches_upcoming

List upcoming League of Legends matches

- HTTP Method: `GET`
- Endpoint: `/lol/matches/upcoming`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLMatches](../models/FilterOverLoLMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLMatches](../models/RangeOverLoLMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLMatches](../models/SearchOverLoLMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLMatches, RangeOverLoLMatches, SearchOverLoLMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLoLMatches(
    begin_at=[
        "nisi e"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "deserun"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        6
    ],
    league_id=[
        10
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "laborum "
    ],
    name=[
        "sint velit"
    ],
    not_started=False,
    number_of_games=[
        0
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=False,
    running=True,
    scheduled_at=[
        "Duis Lorem"
    ],
    serie_id=[
        1
    ],
    slug=[
        "rki"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        6
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        9
    ],
    videogame_version=[
        "076677.94865001934.580355685"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLoLMatches(
    begin_at=[
        "occaecat"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "velit est"
    ],
    forfeit=[
        False
    ],
    id_=[
        3
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "labori"
    ],
    name=[
        "cillum"
    ],
    number_of_games=[
        6
    ],
    scheduled_at=[
        "ad dolor qu"
    ],
    slug=[
        "XMb"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverLoLMatches(
    match_type="all_games_played",
    name="etocc",
    slug="WYcNZudjm l",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.lo_l_matches.get_lol_matches_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_matches_match_id_or_slug

Get a single League of Legends match by ID or slug

- HTTP Method: `GET`
- Endpoint: `/lol/matches/{match_id_or_slug}`

**Parameters**

| Name             | Type                                        | Required | Description        |
| :--------------- | :------------------------------------------ | :------- | :----------------- |
| match_id_or_slug | [MatchIdOrSlug](../models/MatchIdOrSlug.md) | ✅       | A match ID or slug |

**Return Type**

`LoLMatch`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
match_id_or_slug=5

result = sdk.lo_l_matches.get_lol_matches_match_id_or_slug(match_id_or_slug=match_id_or_slug)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
