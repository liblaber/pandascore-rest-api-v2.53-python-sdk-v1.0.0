# LoLWildRiftMatchesService

A list of all methods in the `LoLWildRiftMatchesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                                  |
| :------------------------------------------------------------------------ | :------------------------------------------- |
| [get_lol_wild_rift_matches](#get_lol_wild_rift_matches)                   | List matches for the LoL Wild Rift videogame |
| [get_lol_wild_rift_matches_past](#get_lol_wild_rift_matches_past)         | List past LoL Wild Rift matches              |
| [get_lol_wild_rift_matches_running](#get_lol_wild_rift_matches_running)   | List running LoL Wild Rift matches           |
| [get_lol_wild_rift_matches_upcoming](#get_lol_wild_rift_matches_upcoming) | List upcoming LoL Wild Rift matches          |

## get_lol_wild_rift_matches

List matches for the LoL Wild Rift videogame

- HTTP Method: `GET`
- Endpoint: `/lol-wild-rift/matches`

**Parameters**

| Name     | Type                                                                      | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLolWildRiftMatches](../models/FilterOverLolWildRiftMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLolWildRiftMatches](../models/RangeOverLolWildRiftMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLolWildRiftMatches](../models/SearchOverLolWildRiftMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLolWildRiftMatches, RangeOverLolWildRiftMatches, SearchOverLolWildRiftMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLolWildRiftMatches(
    begin_at=[
        "velit irure"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "ani"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        10
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "aliquip"
    ],
    name=[
        "velit Except"
    ],
    not_started=False,
    number_of_games=[
        2
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "aliqua ulla"
    ],
    serie_id=[
        5
    ],
    slug=[
        "REqPO"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        8
    ],
    videogame_version=[
        "156.75188480.912455326"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLolWildRiftMatches(
    begin_at=[
        "qui laboris"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "occaecat commo"
    ],
    forfeit=[
        True
    ],
    id_=[
        1
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ullamco ex do"
    ],
    name=[
        "dolore "
    ],
    number_of_games=[
        6
    ],
    scheduled_at=[
        "amet "
    ],
    slug=[
        "SWMMt"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        8
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
search=SearchOverLolWildRiftMatches(
    match_type="all_games_played",
    name="nostrud",
    slug="P-",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.lo_l_wild_rift_matches.get_lol_wild_rift_matches(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_wild_rift_matches_past

List past LoL Wild Rift matches

- HTTP Method: `GET`
- Endpoint: `/lol-wild-rift/matches/past`

**Parameters**

| Name     | Type                                                                      | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLolWildRiftMatches](../models/FilterOverLolWildRiftMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLolWildRiftMatches](../models/RangeOverLolWildRiftMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLolWildRiftMatches](../models/SearchOverLolWildRiftMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLolWildRiftMatches, RangeOverLolWildRiftMatches, SearchOverLolWildRiftMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLolWildRiftMatches(
    begin_at=[
        "velit irure"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "ani"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        10
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "aliquip"
    ],
    name=[
        "velit Except"
    ],
    not_started=False,
    number_of_games=[
        2
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "aliqua ulla"
    ],
    serie_id=[
        5
    ],
    slug=[
        "REqPO"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        8
    ],
    videogame_version=[
        "156.75188480.912455326"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLolWildRiftMatches(
    begin_at=[
        "qui laboris"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "occaecat commo"
    ],
    forfeit=[
        True
    ],
    id_=[
        1
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ullamco ex do"
    ],
    name=[
        "dolore "
    ],
    number_of_games=[
        6
    ],
    scheduled_at=[
        "amet "
    ],
    slug=[
        "SWMMt"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        8
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
search=SearchOverLolWildRiftMatches(
    match_type="all_games_played",
    name="nostrud",
    slug="P-",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.lo_l_wild_rift_matches.get_lol_wild_rift_matches_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_wild_rift_matches_running

List running LoL Wild Rift matches

- HTTP Method: `GET`
- Endpoint: `/lol-wild-rift/matches/running`

**Parameters**

| Name     | Type                                                                      | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLolWildRiftMatches](../models/FilterOverLolWildRiftMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLolWildRiftMatches](../models/RangeOverLolWildRiftMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLolWildRiftMatches](../models/SearchOverLolWildRiftMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLolWildRiftMatches, RangeOverLolWildRiftMatches, SearchOverLolWildRiftMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLolWildRiftMatches(
    begin_at=[
        "velit irure"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "ani"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        10
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "aliquip"
    ],
    name=[
        "velit Except"
    ],
    not_started=False,
    number_of_games=[
        2
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "aliqua ulla"
    ],
    serie_id=[
        5
    ],
    slug=[
        "REqPO"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        8
    ],
    videogame_version=[
        "156.75188480.912455326"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLolWildRiftMatches(
    begin_at=[
        "qui laboris"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "occaecat commo"
    ],
    forfeit=[
        True
    ],
    id_=[
        1
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ullamco ex do"
    ],
    name=[
        "dolore "
    ],
    number_of_games=[
        6
    ],
    scheduled_at=[
        "amet "
    ],
    slug=[
        "SWMMt"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        8
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
search=SearchOverLolWildRiftMatches(
    match_type="all_games_played",
    name="nostrud",
    slug="P-",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.lo_l_wild_rift_matches.get_lol_wild_rift_matches_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_wild_rift_matches_upcoming

List upcoming LoL Wild Rift matches

- HTTP Method: `GET`
- Endpoint: `/lol-wild-rift/matches/upcoming`

**Parameters**

| Name     | Type                                                                      | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLolWildRiftMatches](../models/FilterOverLolWildRiftMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLolWildRiftMatches](../models/RangeOverLolWildRiftMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLolWildRiftMatches](../models/SearchOverLolWildRiftMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLolWildRiftMatches, RangeOverLolWildRiftMatches, SearchOverLolWildRiftMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLolWildRiftMatches(
    begin_at=[
        "velit irure"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "ani"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        10
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "aliquip"
    ],
    name=[
        "velit Except"
    ],
    not_started=False,
    number_of_games=[
        2
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "aliqua ulla"
    ],
    serie_id=[
        5
    ],
    slug=[
        "REqPO"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        8
    ],
    videogame_version=[
        "156.75188480.912455326"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLolWildRiftMatches(
    begin_at=[
        "qui laboris"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "occaecat commo"
    ],
    forfeit=[
        True
    ],
    id_=[
        1
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ullamco ex do"
    ],
    name=[
        "dolore "
    ],
    number_of_games=[
        6
    ],
    scheduled_at=[
        "amet "
    ],
    slug=[
        "SWMMt"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        8
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
search=SearchOverLolWildRiftMatches(
    match_type="all_games_played",
    name="nostrud",
    slug="P-",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.lo_l_wild_rift_matches.get_lol_wild_rift_matches_upcoming(
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
