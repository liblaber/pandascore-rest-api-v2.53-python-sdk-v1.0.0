# CodmwMatchesService

A list of all methods in the `CodmwMatchesService` service. Click on the method name to view detailed information about that method.

| Methods                                                   | Description                           |
| :-------------------------------------------------------- | :------------------------------------ |
| [get_codmw_matches](#get_codmw_matches)                   | List matches for the COD MW videogame |
| [get_codmw_matches_past](#get_codmw_matches_past)         | List past CODMW matches               |
| [get_codmw_matches_running](#get_codmw_matches_running)   | List running CODMW matches            |
| [get_codmw_matches_upcoming](#get_codmw_matches_upcoming) | List upcoming CODMW matches           |

## get_codmw_matches

List matches for the COD MW videogame

- HTTP Method: `GET`
- Endpoint: `/codmw/matches`

**Parameters**

| Name     | Type                                                          | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCodmwMatches](../models/FilterOverCodmwMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCodmwMatches](../models/RangeOverCodmwMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCodmwMatches](../models/SearchOverCodmwMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCodmwMatches, RangeOverCodmwMatches, SearchOverCodmwMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCodmwMatches(
    begin_at=[
        "min"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "re"
    ],
    finished=True,
    forfeit=True,
    future=False,
    id_=[
        3
    ],
    league_id=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "dolore Excepte"
    ],
    name=[
        "ut laborum labo"
    ],
    not_started=True,
    number_of_games=[
        1
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=False,
    scheduled_at=[
        "in eiu"
    ],
    serie_id=[
        9
    ],
    slug=[
        "FyZHzUQlMqf"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        9
    ],
    videogame_version=[
        "49265.58843243.7069641"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCodmwMatches(
    begin_at=[
        "sunt pari"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "et mollit"
    ],
    forfeit=[
        True
    ],
    id_=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "consequat au"
    ],
    name=[
        "animirure c"
    ],
    number_of_games=[
        7
    ],
    scheduled_at=[
        "exercitation U"
    ],
    slug=[
        "b"
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
search=SearchOverCodmwMatches(
    match_type="all_games_played",
    name="culpa ad do Du",
    slug="QnETMGeSVO4",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.codmw_matches.get_codmw_matches(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_codmw_matches_past

List past CODMW matches

- HTTP Method: `GET`
- Endpoint: `/codmw/matches/past`

**Parameters**

| Name     | Type                                                          | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCodmwMatches](../models/FilterOverCodmwMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCodmwMatches](../models/RangeOverCodmwMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCodmwMatches](../models/SearchOverCodmwMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCodmwMatches, RangeOverCodmwMatches, SearchOverCodmwMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCodmwMatches(
    begin_at=[
        "min"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "re"
    ],
    finished=True,
    forfeit=True,
    future=False,
    id_=[
        3
    ],
    league_id=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "dolore Excepte"
    ],
    name=[
        "ut laborum labo"
    ],
    not_started=True,
    number_of_games=[
        1
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=False,
    scheduled_at=[
        "in eiu"
    ],
    serie_id=[
        9
    ],
    slug=[
        "FyZHzUQlMqf"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        9
    ],
    videogame_version=[
        "49265.58843243.7069641"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCodmwMatches(
    begin_at=[
        "sunt pari"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "et mollit"
    ],
    forfeit=[
        True
    ],
    id_=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "consequat au"
    ],
    name=[
        "animirure c"
    ],
    number_of_games=[
        7
    ],
    scheduled_at=[
        "exercitation U"
    ],
    slug=[
        "b"
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
search=SearchOverCodmwMatches(
    match_type="all_games_played",
    name="culpa ad do Du",
    slug="QnETMGeSVO4",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.codmw_matches.get_codmw_matches_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_codmw_matches_running

List running CODMW matches

- HTTP Method: `GET`
- Endpoint: `/codmw/matches/running`

**Parameters**

| Name     | Type                                                          | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCodmwMatches](../models/FilterOverCodmwMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCodmwMatches](../models/RangeOverCodmwMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCodmwMatches](../models/SearchOverCodmwMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCodmwMatches, RangeOverCodmwMatches, SearchOverCodmwMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCodmwMatches(
    begin_at=[
        "min"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "re"
    ],
    finished=True,
    forfeit=True,
    future=False,
    id_=[
        3
    ],
    league_id=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "dolore Excepte"
    ],
    name=[
        "ut laborum labo"
    ],
    not_started=True,
    number_of_games=[
        1
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=False,
    scheduled_at=[
        "in eiu"
    ],
    serie_id=[
        9
    ],
    slug=[
        "FyZHzUQlMqf"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        9
    ],
    videogame_version=[
        "49265.58843243.7069641"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCodmwMatches(
    begin_at=[
        "sunt pari"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "et mollit"
    ],
    forfeit=[
        True
    ],
    id_=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "consequat au"
    ],
    name=[
        "animirure c"
    ],
    number_of_games=[
        7
    ],
    scheduled_at=[
        "exercitation U"
    ],
    slug=[
        "b"
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
search=SearchOverCodmwMatches(
    match_type="all_games_played",
    name="culpa ad do Du",
    slug="QnETMGeSVO4",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.codmw_matches.get_codmw_matches_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_codmw_matches_upcoming

List upcoming CODMW matches

- HTTP Method: `GET`
- Endpoint: `/codmw/matches/upcoming`

**Parameters**

| Name     | Type                                                          | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCodmwMatches](../models/FilterOverCodmwMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCodmwMatches](../models/RangeOverCodmwMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCodmwMatches](../models/SearchOverCodmwMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCodmwMatches, RangeOverCodmwMatches, SearchOverCodmwMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCodmwMatches(
    begin_at=[
        "min"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "re"
    ],
    finished=True,
    forfeit=True,
    future=False,
    id_=[
        3
    ],
    league_id=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "dolore Excepte"
    ],
    name=[
        "ut laborum labo"
    ],
    not_started=True,
    number_of_games=[
        1
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=False,
    scheduled_at=[
        "in eiu"
    ],
    serie_id=[
        9
    ],
    slug=[
        "FyZHzUQlMqf"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        9
    ],
    videogame_version=[
        "49265.58843243.7069641"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCodmwMatches(
    begin_at=[
        "sunt pari"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "et mollit"
    ],
    forfeit=[
        True
    ],
    id_=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "consequat au"
    ],
    name=[
        "animirure c"
    ],
    number_of_games=[
        7
    ],
    scheduled_at=[
        "exercitation U"
    ],
    slug=[
        "b"
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
search=SearchOverCodmwMatches(
    match_type="all_games_played",
    name="culpa ad do Du",
    slug="QnETMGeSVO4",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.codmw_matches.get_codmw_matches_upcoming(
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
