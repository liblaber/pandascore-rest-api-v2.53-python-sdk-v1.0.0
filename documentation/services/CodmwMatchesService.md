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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCodmwMatches, RangeOverCodmwMatches, SearchOverCodmwMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCodmwMatches(
    begin_at=[
        "aute do"
    ],
    detailed_stats=False,
    draw=True,
    end_at=[
        "dolore occaeca"
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        8
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "consectetur"
    ],
    name=[
        "irure "
    ],
    not_started=True,
    number_of_games=[
        3
    ],
    opponent_id=[
        7
    ],
    opponents_filled=True,
    past=False,
    running=True,
    scheduled_at=[
        "Ex"
    ],
    serie_id=[
        1
    ],
    slug=[
        "nyGgsi"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        3
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        3
    ],
    videogame_version=[
        "9206043.379237680"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCodmwMatches(
    begin_at=[
        "et pariat"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "commo"
    ],
    forfeit=[
        True
    ],
    id_=[
        7
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "te"
    ],
    name=[
        "sint repreh"
    ],
    number_of_games=[
        0
    ],
    scheduled_at=[
        "officia anim"
    ],
    slug=[
        "hKOBGa4"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    winner_id=[
        9
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
    name="irure incid",
    slug="1byxpI4",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCodmwMatches, RangeOverCodmwMatches, SearchOverCodmwMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCodmwMatches(
    begin_at=[
        "aute do"
    ],
    detailed_stats=False,
    draw=True,
    end_at=[
        "dolore occaeca"
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        8
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "consectetur"
    ],
    name=[
        "irure "
    ],
    not_started=True,
    number_of_games=[
        3
    ],
    opponent_id=[
        7
    ],
    opponents_filled=True,
    past=False,
    running=True,
    scheduled_at=[
        "Ex"
    ],
    serie_id=[
        1
    ],
    slug=[
        "nyGgsi"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        3
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        3
    ],
    videogame_version=[
        "9206043.379237680"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCodmwMatches(
    begin_at=[
        "et pariat"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "commo"
    ],
    forfeit=[
        True
    ],
    id_=[
        7
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "te"
    ],
    name=[
        "sint repreh"
    ],
    number_of_games=[
        0
    ],
    scheduled_at=[
        "officia anim"
    ],
    slug=[
        "hKOBGa4"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    winner_id=[
        9
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
    name="irure incid",
    slug="1byxpI4",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCodmwMatches, RangeOverCodmwMatches, SearchOverCodmwMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCodmwMatches(
    begin_at=[
        "aute do"
    ],
    detailed_stats=False,
    draw=True,
    end_at=[
        "dolore occaeca"
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        8
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "consectetur"
    ],
    name=[
        "irure "
    ],
    not_started=True,
    number_of_games=[
        3
    ],
    opponent_id=[
        7
    ],
    opponents_filled=True,
    past=False,
    running=True,
    scheduled_at=[
        "Ex"
    ],
    serie_id=[
        1
    ],
    slug=[
        "nyGgsi"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        3
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        3
    ],
    videogame_version=[
        "9206043.379237680"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCodmwMatches(
    begin_at=[
        "et pariat"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "commo"
    ],
    forfeit=[
        True
    ],
    id_=[
        7
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "te"
    ],
    name=[
        "sint repreh"
    ],
    number_of_games=[
        0
    ],
    scheduled_at=[
        "officia anim"
    ],
    slug=[
        "hKOBGa4"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    winner_id=[
        9
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
    name="irure incid",
    slug="1byxpI4",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCodmwMatches, RangeOverCodmwMatches, SearchOverCodmwMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCodmwMatches(
    begin_at=[
        "aute do"
    ],
    detailed_stats=False,
    draw=True,
    end_at=[
        "dolore occaeca"
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        8
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "consectetur"
    ],
    name=[
        "irure "
    ],
    not_started=True,
    number_of_games=[
        3
    ],
    opponent_id=[
        7
    ],
    opponents_filled=True,
    past=False,
    running=True,
    scheduled_at=[
        "Ex"
    ],
    serie_id=[
        1
    ],
    slug=[
        "nyGgsi"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        3
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        3
    ],
    videogame_version=[
        "9206043.379237680"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCodmwMatches(
    begin_at=[
        "et pariat"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "commo"
    ],
    forfeit=[
        True
    ],
    id_=[
        7
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "te"
    ],
    name=[
        "sint repreh"
    ],
    number_of_games=[
        0
    ],
    scheduled_at=[
        "officia anim"
    ],
    slug=[
        "hKOBGa4"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    winner_id=[
        9
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
    name="irure incid",
    slug="1byxpI4",
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
