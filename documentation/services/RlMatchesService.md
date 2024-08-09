# RlMatchesService

A list of all methods in the `RlMatchesService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description                                  |
| :-------------------------------------------------- | :------------------------------------------- |
| [get_rl_matches](#get_rl_matches)                   | List matches for the Rocket League videogame |
| [get_rl_matches_past](#get_rl_matches_past)         | List past Rocket League matches              |
| [get_rl_matches_running](#get_rl_matches_running)   | List running Rocket League matches           |
| [get_rl_matches_upcoming](#get_rl_matches_upcoming) | List upcoming Rocket League matches          |

## get_rl_matches

List matches for the Rocket League videogame

- HTTP Method: `GET`
- Endpoint: `/rl/matches`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverRlMatches](../models/FilterOverRlMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverRlMatches](../models/RangeOverRlMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverRlMatches](../models/SearchOverRlMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverRlMatches, RangeOverRlMatches, SearchOverRlMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverRlMatches(
    begin_at=[
        "culpa r"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "in Ut "
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        9
    ],
    league_id=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ut"
    ],
    name=[
        "ullamco en"
    ],
    not_started=False,
    number_of_games=[
        8
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "dolore"
    ],
    serie_id=[
        6
    ],
    slug=[
        "L2B6u2"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        4
    ],
    videogame_version=[
        "6734585794.51.57967777"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverRlMatches(
    begin_at=[
        "amet "
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "eu officia id d"
    ],
    forfeit=[
        False
    ],
    id_=[
        9
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "i"
    ],
    name=[
        "reprehend"
    ],
    number_of_games=[
        7
    ],
    scheduled_at=[
        "occaecat mo"
    ],
    slug=[
        "SC"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        6
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
search=SearchOverRlMatches(
    match_type="all_games_played",
    name="commodo pariatu",
    slug="Y",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.rl_matches.get_rl_matches(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_rl_matches_past

List past Rocket League matches

- HTTP Method: `GET`
- Endpoint: `/rl/matches/past`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverRlMatches](../models/FilterOverRlMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverRlMatches](../models/RangeOverRlMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverRlMatches](../models/SearchOverRlMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverRlMatches, RangeOverRlMatches, SearchOverRlMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverRlMatches(
    begin_at=[
        "culpa r"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "in Ut "
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        9
    ],
    league_id=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ut"
    ],
    name=[
        "ullamco en"
    ],
    not_started=False,
    number_of_games=[
        8
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "dolore"
    ],
    serie_id=[
        6
    ],
    slug=[
        "L2B6u2"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        4
    ],
    videogame_version=[
        "6734585794.51.57967777"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverRlMatches(
    begin_at=[
        "amet "
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "eu officia id d"
    ],
    forfeit=[
        False
    ],
    id_=[
        9
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "i"
    ],
    name=[
        "reprehend"
    ],
    number_of_games=[
        7
    ],
    scheduled_at=[
        "occaecat mo"
    ],
    slug=[
        "SC"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        6
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
search=SearchOverRlMatches(
    match_type="all_games_played",
    name="commodo pariatu",
    slug="Y",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.rl_matches.get_rl_matches_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_rl_matches_running

List running Rocket League matches

- HTTP Method: `GET`
- Endpoint: `/rl/matches/running`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverRlMatches](../models/FilterOverRlMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverRlMatches](../models/RangeOverRlMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverRlMatches](../models/SearchOverRlMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverRlMatches, RangeOverRlMatches, SearchOverRlMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverRlMatches(
    begin_at=[
        "culpa r"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "in Ut "
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        9
    ],
    league_id=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ut"
    ],
    name=[
        "ullamco en"
    ],
    not_started=False,
    number_of_games=[
        8
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "dolore"
    ],
    serie_id=[
        6
    ],
    slug=[
        "L2B6u2"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        4
    ],
    videogame_version=[
        "6734585794.51.57967777"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverRlMatches(
    begin_at=[
        "amet "
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "eu officia id d"
    ],
    forfeit=[
        False
    ],
    id_=[
        9
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "i"
    ],
    name=[
        "reprehend"
    ],
    number_of_games=[
        7
    ],
    scheduled_at=[
        "occaecat mo"
    ],
    slug=[
        "SC"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        6
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
search=SearchOverRlMatches(
    match_type="all_games_played",
    name="commodo pariatu",
    slug="Y",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.rl_matches.get_rl_matches_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_rl_matches_upcoming

List upcoming Rocket League matches

- HTTP Method: `GET`
- Endpoint: `/rl/matches/upcoming`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverRlMatches](../models/FilterOverRlMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverRlMatches](../models/RangeOverRlMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverRlMatches](../models/SearchOverRlMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverRlMatches, RangeOverRlMatches, SearchOverRlMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverRlMatches(
    begin_at=[
        "culpa r"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "in Ut "
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        9
    ],
    league_id=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ut"
    ],
    name=[
        "ullamco en"
    ],
    not_started=False,
    number_of_games=[
        8
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "dolore"
    ],
    serie_id=[
        6
    ],
    slug=[
        "L2B6u2"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        4
    ],
    videogame_version=[
        "6734585794.51.57967777"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverRlMatches(
    begin_at=[
        "amet "
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "eu officia id d"
    ],
    forfeit=[
        False
    ],
    id_=[
        9
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "i"
    ],
    name=[
        "reprehend"
    ],
    number_of_games=[
        7
    ],
    scheduled_at=[
        "occaecat mo"
    ],
    slug=[
        "SC"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        6
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
search=SearchOverRlMatches(
    match_type="all_games_played",
    name="commodo pariatu",
    slug="Y",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.rl_matches.get_rl_matches_upcoming(
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
