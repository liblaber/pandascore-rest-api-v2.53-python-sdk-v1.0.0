# ValorantMatchesService

A list of all methods in the `ValorantMatchesService` service. Click on the method name to view detailed information about that method.

| Methods                                                         | Description                             |
| :-------------------------------------------------------------- | :-------------------------------------- |
| [get_valorant_matches](#get_valorant_matches)                   | List matches for the Valorant videogame |
| [get_valorant_matches_past](#get_valorant_matches_past)         | List past Valorant matches              |
| [get_valorant_matches_running](#get_valorant_matches_running)   | List running Valorant matches           |
| [get_valorant_matches_upcoming](#get_valorant_matches_upcoming) | List upcoming Valorant matches          |

## get_valorant_matches

List matches for the Valorant videogame

- HTTP Method: `GET`
- Endpoint: `/valorant/matches`

**Parameters**

| Name     | Type                                                                | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantMatches](../models/FilterOverValorantMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantMatches](../models/RangeOverValorantMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantMatches](../models/SearchOverValorantMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverValorantMatches, RangeOverValorantMatches, SearchOverValorantMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverValorantMatches(
    begin_at=[
        "dolor"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "ex"
    ],
    finished=True,
    forfeit=True,
    future=True,
    id_=[
        9
    ],
    league_id=[
        9
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "dolor velit"
    ],
    name=[
        "minim"
    ],
    not_started=False,
    number_of_games=[
        8
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=False,
    running=False,
    scheduled_at=[
        "repre"
    ],
    serie_id=[
        1
    ],
    slug=[
        "P"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        3
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        5
    ],
    videogame_version=[
        "848.5017114648.16441010106"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverValorantMatches(
    begin_at=[
        "off"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "f"
    ],
    forfeit=[
        False
    ],
    id_=[
        8
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "adipisicin"
    ],
    name=[
        "elit dolore in"
    ],
    number_of_games=[
        4
    ],
    scheduled_at=[
        "sunt s"
    ],
    slug=[
        "PUIjB6P_Y"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        3
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
search=SearchOverValorantMatches(
    match_type="all_games_played",
    name="laboris ",
    slug="vBwZ20H7NVH",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.valorant_matches.get_valorant_matches(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_valorant_matches_past

List past Valorant matches

- HTTP Method: `GET`
- Endpoint: `/valorant/matches/past`

**Parameters**

| Name     | Type                                                                | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantMatches](../models/FilterOverValorantMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantMatches](../models/RangeOverValorantMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantMatches](../models/SearchOverValorantMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverValorantMatches, RangeOverValorantMatches, SearchOverValorantMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverValorantMatches(
    begin_at=[
        "dolor"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "ex"
    ],
    finished=True,
    forfeit=True,
    future=True,
    id_=[
        9
    ],
    league_id=[
        9
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "dolor velit"
    ],
    name=[
        "minim"
    ],
    not_started=False,
    number_of_games=[
        8
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=False,
    running=False,
    scheduled_at=[
        "repre"
    ],
    serie_id=[
        1
    ],
    slug=[
        "P"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        3
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        5
    ],
    videogame_version=[
        "848.5017114648.16441010106"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverValorantMatches(
    begin_at=[
        "off"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "f"
    ],
    forfeit=[
        False
    ],
    id_=[
        8
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "adipisicin"
    ],
    name=[
        "elit dolore in"
    ],
    number_of_games=[
        4
    ],
    scheduled_at=[
        "sunt s"
    ],
    slug=[
        "PUIjB6P_Y"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        3
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
search=SearchOverValorantMatches(
    match_type="all_games_played",
    name="laboris ",
    slug="vBwZ20H7NVH",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.valorant_matches.get_valorant_matches_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_valorant_matches_running

List running Valorant matches

- HTTP Method: `GET`
- Endpoint: `/valorant/matches/running`

**Parameters**

| Name     | Type                                                                | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantMatches](../models/FilterOverValorantMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantMatches](../models/RangeOverValorantMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantMatches](../models/SearchOverValorantMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverValorantMatches, RangeOverValorantMatches, SearchOverValorantMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverValorantMatches(
    begin_at=[
        "dolor"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "ex"
    ],
    finished=True,
    forfeit=True,
    future=True,
    id_=[
        9
    ],
    league_id=[
        9
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "dolor velit"
    ],
    name=[
        "minim"
    ],
    not_started=False,
    number_of_games=[
        8
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=False,
    running=False,
    scheduled_at=[
        "repre"
    ],
    serie_id=[
        1
    ],
    slug=[
        "P"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        3
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        5
    ],
    videogame_version=[
        "848.5017114648.16441010106"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverValorantMatches(
    begin_at=[
        "off"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "f"
    ],
    forfeit=[
        False
    ],
    id_=[
        8
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "adipisicin"
    ],
    name=[
        "elit dolore in"
    ],
    number_of_games=[
        4
    ],
    scheduled_at=[
        "sunt s"
    ],
    slug=[
        "PUIjB6P_Y"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        3
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
search=SearchOverValorantMatches(
    match_type="all_games_played",
    name="laboris ",
    slug="vBwZ20H7NVH",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.valorant_matches.get_valorant_matches_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_valorant_matches_upcoming

List upcoming Valorant matches

- HTTP Method: `GET`
- Endpoint: `/valorant/matches/upcoming`

**Parameters**

| Name     | Type                                                                | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantMatches](../models/FilterOverValorantMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantMatches](../models/RangeOverValorantMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantMatches](../models/SearchOverValorantMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverValorantMatches, RangeOverValorantMatches, SearchOverValorantMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverValorantMatches(
    begin_at=[
        "dolor"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "ex"
    ],
    finished=True,
    forfeit=True,
    future=True,
    id_=[
        9
    ],
    league_id=[
        9
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "dolor velit"
    ],
    name=[
        "minim"
    ],
    not_started=False,
    number_of_games=[
        8
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=False,
    running=False,
    scheduled_at=[
        "repre"
    ],
    serie_id=[
        1
    ],
    slug=[
        "P"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        3
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        5
    ],
    videogame_version=[
        "848.5017114648.16441010106"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverValorantMatches(
    begin_at=[
        "off"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "f"
    ],
    forfeit=[
        False
    ],
    id_=[
        8
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "adipisicin"
    ],
    name=[
        "elit dolore in"
    ],
    number_of_games=[
        4
    ],
    scheduled_at=[
        "sunt s"
    ],
    slug=[
        "PUIjB6P_Y"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        3
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
search=SearchOverValorantMatches(
    match_type="all_games_played",
    name="laboris ",
    slug="vBwZ20H7NVH",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.valorant_matches.get_valorant_matches_upcoming(
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
