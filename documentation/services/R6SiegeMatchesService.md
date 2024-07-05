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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverR6SiegeMatches, RangeOverR6SiegeMatches, SearchOverR6SiegeMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverR6SiegeMatches(
    begin_at=[
        "in"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "conse"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        3
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "proident repreh"
    ],
    name=[
        "irure "
    ],
    not_started=False,
    number_of_games=[
        4
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=False,
    running=True,
    scheduled_at=[
        "enim offici"
    ],
    serie_id=[
        4
    ],
    slug=[
        "y-R0S1G7Ae"
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
        8
    ],
    videogame_version=[
        "91490764700.14068944977"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverR6SiegeMatches(
    begin_at=[
        "e"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "e"
    ],
    forfeit=[
        True
    ],
    id_=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ad "
    ],
    name=[
        "deserunt dol"
    ],
    number_of_games=[
        8
    ],
    scheduled_at=[
        "in"
    ],
    slug=[
        "J40PU-E6"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        9
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
search=SearchOverR6SiegeMatches(
    match_type="all_games_played",
    name="fugiat qui",
    slug="YQMpz2yof",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverR6SiegeMatches, RangeOverR6SiegeMatches, SearchOverR6SiegeMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverR6SiegeMatches(
    begin_at=[
        "in"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "conse"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        3
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "proident repreh"
    ],
    name=[
        "irure "
    ],
    not_started=False,
    number_of_games=[
        4
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=False,
    running=True,
    scheduled_at=[
        "enim offici"
    ],
    serie_id=[
        4
    ],
    slug=[
        "y-R0S1G7Ae"
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
        8
    ],
    videogame_version=[
        "91490764700.14068944977"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverR6SiegeMatches(
    begin_at=[
        "e"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "e"
    ],
    forfeit=[
        True
    ],
    id_=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ad "
    ],
    name=[
        "deserunt dol"
    ],
    number_of_games=[
        8
    ],
    scheduled_at=[
        "in"
    ],
    slug=[
        "J40PU-E6"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        9
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
search=SearchOverR6SiegeMatches(
    match_type="all_games_played",
    name="fugiat qui",
    slug="YQMpz2yof",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverR6SiegeMatches, RangeOverR6SiegeMatches, SearchOverR6SiegeMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverR6SiegeMatches(
    begin_at=[
        "in"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "conse"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        3
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "proident repreh"
    ],
    name=[
        "irure "
    ],
    not_started=False,
    number_of_games=[
        4
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=False,
    running=True,
    scheduled_at=[
        "enim offici"
    ],
    serie_id=[
        4
    ],
    slug=[
        "y-R0S1G7Ae"
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
        8
    ],
    videogame_version=[
        "91490764700.14068944977"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverR6SiegeMatches(
    begin_at=[
        "e"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "e"
    ],
    forfeit=[
        True
    ],
    id_=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ad "
    ],
    name=[
        "deserunt dol"
    ],
    number_of_games=[
        8
    ],
    scheduled_at=[
        "in"
    ],
    slug=[
        "J40PU-E6"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        9
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
search=SearchOverR6SiegeMatches(
    match_type="all_games_played",
    name="fugiat qui",
    slug="YQMpz2yof",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverR6SiegeMatches, RangeOverR6SiegeMatches, SearchOverR6SiegeMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverR6SiegeMatches(
    begin_at=[
        "in"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "conse"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        3
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "proident repreh"
    ],
    name=[
        "irure "
    ],
    not_started=False,
    number_of_games=[
        4
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=False,
    running=True,
    scheduled_at=[
        "enim offici"
    ],
    serie_id=[
        4
    ],
    slug=[
        "y-R0S1G7Ae"
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
        8
    ],
    videogame_version=[
        "91490764700.14068944977"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverR6SiegeMatches(
    begin_at=[
        "e"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "e"
    ],
    forfeit=[
        True
    ],
    id_=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ad "
    ],
    name=[
        "deserunt dol"
    ],
    number_of_games=[
        8
    ],
    scheduled_at=[
        "in"
    ],
    slug=[
        "J40PU-E6"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        9
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
search=SearchOverR6SiegeMatches(
    match_type="all_games_played",
    name="fugiat qui",
    slug="YQMpz2yof",
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
