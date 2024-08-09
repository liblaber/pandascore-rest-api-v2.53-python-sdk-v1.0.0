# R6SiegeMatchesService

A list of all methods in the `R6SiegeMatchesService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description                                      |
| :------------------------------------------------------------ | :----------------------------------------------- |
| [get_r6siege_matches](#get_r6siege_matches)                   | List matches for the Rainbow Six Siege videogame |
| [get_r6siege_matches_past](#get_r6siege_matches_past)         | List past Rainbow Six Siege matches              |
| [get_r6siege_matches_running](#get_r6siege_matches_running)   | List running Rainbow Six Siege matches           |
| [get_r6siege_matches_upcoming](#get_r6siege_matches_upcoming) | List upcoming Rainbow Six Siege matches          |

## get_r6siege_matches

List matches for the Rainbow Six Siege videogame

- HTTP Method: `GET`
- Endpoint: `/r6siege/matches`

**Parameters**

| Name     | Type                                                              | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverR6SiegeMatches](../models/FilterOverR6SiegeMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverR6SiegeMatches](../models/RangeOverR6SiegeMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                         | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverR6SiegeMatches](../models/SearchOverR6SiegeMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                         | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                               | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverR6SiegeMatches, RangeOverR6SiegeMatches, SearchOverR6SiegeMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverR6SiegeMatches(
    begin_at=[
        "ut proident"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "magn"
    ],
    finished=True,
    forfeit=True,
    future=True,
    id_=[
        3
    ],
    league_id=[
        3
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ani"
    ],
    name=[
        "aliquip culpa"
    ],
    not_started=True,
    number_of_games=[
        9
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=True,
    scheduled_at=[
        "ad eu consec"
    ],
    serie_id=[
        1
    ],
    slug=[
        "6A0c8"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        4
    ],
    videogame_version=[
        "266391336.84111"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverR6SiegeMatches(
    begin_at=[
        "t"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "dolor"
    ],
    forfeit=[
        False
    ],
    id_=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "mo"
    ],
    name=[
        "commodo"
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "sed"
    ],
    slug=[
        "SXr_"
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
search=SearchOverR6SiegeMatches(
    match_type="all_games_played",
    name="culpa deserun",
    slug="rYbtGes",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.r6_siege_matches.get_r6siege_matches(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_r6siege_matches_past

List past Rainbow Six Siege matches

- HTTP Method: `GET`
- Endpoint: `/r6siege/matches/past`

**Parameters**

| Name     | Type                                                              | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverR6SiegeMatches](../models/FilterOverR6SiegeMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverR6SiegeMatches](../models/RangeOverR6SiegeMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                         | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverR6SiegeMatches](../models/SearchOverR6SiegeMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                         | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                               | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverR6SiegeMatches, RangeOverR6SiegeMatches, SearchOverR6SiegeMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverR6SiegeMatches(
    begin_at=[
        "ut proident"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "magn"
    ],
    finished=True,
    forfeit=True,
    future=True,
    id_=[
        3
    ],
    league_id=[
        3
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ani"
    ],
    name=[
        "aliquip culpa"
    ],
    not_started=True,
    number_of_games=[
        9
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=True,
    scheduled_at=[
        "ad eu consec"
    ],
    serie_id=[
        1
    ],
    slug=[
        "6A0c8"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        4
    ],
    videogame_version=[
        "266391336.84111"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverR6SiegeMatches(
    begin_at=[
        "t"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "dolor"
    ],
    forfeit=[
        False
    ],
    id_=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "mo"
    ],
    name=[
        "commodo"
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "sed"
    ],
    slug=[
        "SXr_"
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
search=SearchOverR6SiegeMatches(
    match_type="all_games_played",
    name="culpa deserun",
    slug="rYbtGes",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.r6_siege_matches.get_r6siege_matches_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_r6siege_matches_running

List running Rainbow Six Siege matches

- HTTP Method: `GET`
- Endpoint: `/r6siege/matches/running`

**Parameters**

| Name     | Type                                                              | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverR6SiegeMatches](../models/FilterOverR6SiegeMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverR6SiegeMatches](../models/RangeOverR6SiegeMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                         | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverR6SiegeMatches](../models/SearchOverR6SiegeMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                         | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                               | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverR6SiegeMatches, RangeOverR6SiegeMatches, SearchOverR6SiegeMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverR6SiegeMatches(
    begin_at=[
        "ut proident"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "magn"
    ],
    finished=True,
    forfeit=True,
    future=True,
    id_=[
        3
    ],
    league_id=[
        3
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ani"
    ],
    name=[
        "aliquip culpa"
    ],
    not_started=True,
    number_of_games=[
        9
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=True,
    scheduled_at=[
        "ad eu consec"
    ],
    serie_id=[
        1
    ],
    slug=[
        "6A0c8"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        4
    ],
    videogame_version=[
        "266391336.84111"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverR6SiegeMatches(
    begin_at=[
        "t"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "dolor"
    ],
    forfeit=[
        False
    ],
    id_=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "mo"
    ],
    name=[
        "commodo"
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "sed"
    ],
    slug=[
        "SXr_"
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
search=SearchOverR6SiegeMatches(
    match_type="all_games_played",
    name="culpa deserun",
    slug="rYbtGes",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.r6_siege_matches.get_r6siege_matches_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_r6siege_matches_upcoming

List upcoming Rainbow Six Siege matches

- HTTP Method: `GET`
- Endpoint: `/r6siege/matches/upcoming`

**Parameters**

| Name     | Type                                                              | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverR6SiegeMatches](../models/FilterOverR6SiegeMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverR6SiegeMatches](../models/RangeOverR6SiegeMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                         | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverR6SiegeMatches](../models/SearchOverR6SiegeMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                         | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                               | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverR6SiegeMatches, RangeOverR6SiegeMatches, SearchOverR6SiegeMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverR6SiegeMatches(
    begin_at=[
        "ut proident"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "magn"
    ],
    finished=True,
    forfeit=True,
    future=True,
    id_=[
        3
    ],
    league_id=[
        3
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ani"
    ],
    name=[
        "aliquip culpa"
    ],
    not_started=True,
    number_of_games=[
        9
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=True,
    scheduled_at=[
        "ad eu consec"
    ],
    serie_id=[
        1
    ],
    slug=[
        "6A0c8"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        4
    ],
    videogame_version=[
        "266391336.84111"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverR6SiegeMatches(
    begin_at=[
        "t"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "dolor"
    ],
    forfeit=[
        False
    ],
    id_=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "mo"
    ],
    name=[
        "commodo"
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "sed"
    ],
    slug=[
        "SXr_"
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
search=SearchOverR6SiegeMatches(
    match_type="all_games_played",
    name="culpa deserun",
    slug="rYbtGes",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.r6_siege_matches.get_r6siege_matches_upcoming(
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
