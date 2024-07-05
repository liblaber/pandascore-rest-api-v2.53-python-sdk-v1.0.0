# ValorantTournamentsService

A list of all methods in the `ValorantTournamentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                                 |
| :---------------------------------------------------------------------- | :------------------------------------------ |
| [get_valorant_tournaments](#get_valorant_tournaments)                   | List tournaments for the Valorant videogame |
| [get_valorant_tournaments_past](#get_valorant_tournaments_past)         | List past Valorant tournaments              |
| [get_valorant_tournaments_running](#get_valorant_tournaments_running)   | List running Valorant tournaments           |
| [get_valorant_tournaments_upcoming](#get_valorant_tournaments_upcoming) | List upcoming Valorant tournaments          |

## get_valorant_tournaments

List tournaments for the Valorant videogame

- HTTP Method: `GET`
- Endpoint: `/valorant/tournaments`

**Parameters**

| Name     | Type                                                                                  | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantShortTournaments](../models/FilterOverValorantShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantShortTournaments](../models/RangeOverValorantShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantShortTournaments](../models/SearchOverValorantShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverValorantShortTournaments, RangeOverValorantShortTournaments, SearchOverValorantShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverValorantShortTournaments(
    begin_at=[
        "minim l"
    ],
    detailed_stats=True,
    end_at=[
        "in dolore co"
    ],
    has_bracket=True,
    id_=[
        3
    ],
    live_supported=True,
    modified_at=[
        "in"
    ],
    name=[
        "in ipsum sint "
    ],
    prizepool=[
        "dolor te"
    ],
    serie_id=[
        8
    ],
    slug=[
        "enin"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        6
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverValorantShortTournaments(
    begin_at=[
        "proident"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "c"
    ],
    has_bracket=[
        False
    ],
    id_=[
        7
    ],
    modified_at=[
        "s"
    ],
    name=[
        "occaecat"
    ],
    prizepool=[
        "aute "
    ],
    serie_id=[
        5
    ],
    slug=[
        "vr"
    ],
    tier=[
        "a"
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
search=SearchOverValorantShortTournaments(
    name="occaeca",
    prizepool="cillum irure a",
    slug="rq8",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.valorant_tournaments.get_valorant_tournaments(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_valorant_tournaments_past

List past Valorant tournaments

- HTTP Method: `GET`
- Endpoint: `/valorant/tournaments/past`

**Parameters**

| Name     | Type                                                                                  | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantShortTournaments](../models/FilterOverValorantShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantShortTournaments](../models/RangeOverValorantShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantShortTournaments](../models/SearchOverValorantShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverValorantShortTournaments, RangeOverValorantShortTournaments, SearchOverValorantShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverValorantShortTournaments(
    begin_at=[
        "minim l"
    ],
    detailed_stats=True,
    end_at=[
        "in dolore co"
    ],
    has_bracket=True,
    id_=[
        3
    ],
    live_supported=True,
    modified_at=[
        "in"
    ],
    name=[
        "in ipsum sint "
    ],
    prizepool=[
        "dolor te"
    ],
    serie_id=[
        8
    ],
    slug=[
        "enin"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        6
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverValorantShortTournaments(
    begin_at=[
        "proident"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "c"
    ],
    has_bracket=[
        False
    ],
    id_=[
        7
    ],
    modified_at=[
        "s"
    ],
    name=[
        "occaecat"
    ],
    prizepool=[
        "aute "
    ],
    serie_id=[
        5
    ],
    slug=[
        "vr"
    ],
    tier=[
        "a"
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
search=SearchOverValorantShortTournaments(
    name="occaeca",
    prizepool="cillum irure a",
    slug="rq8",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.valorant_tournaments.get_valorant_tournaments_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_valorant_tournaments_running

List running Valorant tournaments

- HTTP Method: `GET`
- Endpoint: `/valorant/tournaments/running`

**Parameters**

| Name     | Type                                                                                  | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantShortTournaments](../models/FilterOverValorantShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantShortTournaments](../models/RangeOverValorantShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantShortTournaments](../models/SearchOverValorantShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverValorantShortTournaments, RangeOverValorantShortTournaments, SearchOverValorantShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverValorantShortTournaments(
    begin_at=[
        "minim l"
    ],
    detailed_stats=True,
    end_at=[
        "in dolore co"
    ],
    has_bracket=True,
    id_=[
        3
    ],
    live_supported=True,
    modified_at=[
        "in"
    ],
    name=[
        "in ipsum sint "
    ],
    prizepool=[
        "dolor te"
    ],
    serie_id=[
        8
    ],
    slug=[
        "enin"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        6
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverValorantShortTournaments(
    begin_at=[
        "proident"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "c"
    ],
    has_bracket=[
        False
    ],
    id_=[
        7
    ],
    modified_at=[
        "s"
    ],
    name=[
        "occaecat"
    ],
    prizepool=[
        "aute "
    ],
    serie_id=[
        5
    ],
    slug=[
        "vr"
    ],
    tier=[
        "a"
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
search=SearchOverValorantShortTournaments(
    name="occaeca",
    prizepool="cillum irure a",
    slug="rq8",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.valorant_tournaments.get_valorant_tournaments_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_valorant_tournaments_upcoming

List upcoming Valorant tournaments

- HTTP Method: `GET`
- Endpoint: `/valorant/tournaments/upcoming`

**Parameters**

| Name     | Type                                                                                  | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantShortTournaments](../models/FilterOverValorantShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantShortTournaments](../models/RangeOverValorantShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantShortTournaments](../models/SearchOverValorantShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverValorantShortTournaments, RangeOverValorantShortTournaments, SearchOverValorantShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverValorantShortTournaments(
    begin_at=[
        "minim l"
    ],
    detailed_stats=True,
    end_at=[
        "in dolore co"
    ],
    has_bracket=True,
    id_=[
        3
    ],
    live_supported=True,
    modified_at=[
        "in"
    ],
    name=[
        "in ipsum sint "
    ],
    prizepool=[
        "dolor te"
    ],
    serie_id=[
        8
    ],
    slug=[
        "enin"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        6
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverValorantShortTournaments(
    begin_at=[
        "proident"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "c"
    ],
    has_bracket=[
        False
    ],
    id_=[
        7
    ],
    modified_at=[
        "s"
    ],
    name=[
        "occaecat"
    ],
    prizepool=[
        "aute "
    ],
    serie_id=[
        5
    ],
    slug=[
        "vr"
    ],
    tier=[
        "a"
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
search=SearchOverValorantShortTournaments(
    name="occaeca",
    prizepool="cillum irure a",
    slug="rq8",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.valorant_tournaments.get_valorant_tournaments_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
