# CodmwTournamentsService

A list of all methods in the `CodmwTournamentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                           | Description                              |
| :---------------------------------------------------------------- | :--------------------------------------- |
| [get_codmw_tournaments](#get_codmw_tournaments)                   | List tournaments for the CODMW videogame |
| [get_codmw_tournaments_past](#get_codmw_tournaments_past)         | List past CODMW tournaments              |
| [get_codmw_tournaments_running](#get_codmw_tournaments_running)   | List running CODMW tournaments           |
| [get_codmw_tournaments_upcoming](#get_codmw_tournaments_upcoming) | List upcoming CODMW tournaments          |

## get_codmw_tournaments

List tournaments for the CODMW videogame

- HTTP Method: `GET`
- Endpoint: `/codmw/tournaments`

**Parameters**

| Name     | Type                                                                            | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCodmwShortTournaments](../models/FilterOverCodmwShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCodmwShortTournaments](../models/RangeOverCodmwShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                       | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCodmwShortTournaments](../models/SearchOverCodmwShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                       | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                             | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCodmwShortTournaments, RangeOverCodmwShortTournaments, SearchOverCodmwShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCodmwShortTournaments(
    begin_at=[
        "n"
    ],
    detailed_stats=False,
    end_at=[
        "ad"
    ],
    has_bracket=False,
    id_=[
        10
    ],
    live_supported=True,
    modified_at=[
        "elit qui"
    ],
    name=[
        "dolor Ut "
    ],
    prizepool=[
        "reprehenderit"
    ],
    serie_id=[
        5
    ],
    slug=[
        "14rd"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        5
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCodmwShortTournaments(
    begin_at=[
        "laboris cupida"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "Excep"
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "nulla cu"
    ],
    name=[
        "officia est m"
    ],
    prizepool=[
        "nulla"
    ],
    serie_id=[
        3
    ],
    slug=[
        "uyx2u_a_t"
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
search=SearchOverCodmwShortTournaments(
    name="in dolor de",
    prizepool="incididunt dol",
    slug="q_",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.codmw_tournaments.get_codmw_tournaments(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_codmw_tournaments_past

List past CODMW tournaments

- HTTP Method: `GET`
- Endpoint: `/codmw/tournaments/past`

**Parameters**

| Name     | Type                                                                            | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCodmwShortTournaments](../models/FilterOverCodmwShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCodmwShortTournaments](../models/RangeOverCodmwShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                       | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCodmwShortTournaments](../models/SearchOverCodmwShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                       | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                             | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCodmwShortTournaments, RangeOverCodmwShortTournaments, SearchOverCodmwShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCodmwShortTournaments(
    begin_at=[
        "n"
    ],
    detailed_stats=False,
    end_at=[
        "ad"
    ],
    has_bracket=False,
    id_=[
        10
    ],
    live_supported=True,
    modified_at=[
        "elit qui"
    ],
    name=[
        "dolor Ut "
    ],
    prizepool=[
        "reprehenderit"
    ],
    serie_id=[
        5
    ],
    slug=[
        "14rd"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        5
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCodmwShortTournaments(
    begin_at=[
        "laboris cupida"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "Excep"
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "nulla cu"
    ],
    name=[
        "officia est m"
    ],
    prizepool=[
        "nulla"
    ],
    serie_id=[
        3
    ],
    slug=[
        "uyx2u_a_t"
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
search=SearchOverCodmwShortTournaments(
    name="in dolor de",
    prizepool="incididunt dol",
    slug="q_",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.codmw_tournaments.get_codmw_tournaments_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_codmw_tournaments_running

List running CODMW tournaments

- HTTP Method: `GET`
- Endpoint: `/codmw/tournaments/running`

**Parameters**

| Name     | Type                                                                            | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCodmwShortTournaments](../models/FilterOverCodmwShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCodmwShortTournaments](../models/RangeOverCodmwShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                       | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCodmwShortTournaments](../models/SearchOverCodmwShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                       | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                             | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCodmwShortTournaments, RangeOverCodmwShortTournaments, SearchOverCodmwShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCodmwShortTournaments(
    begin_at=[
        "n"
    ],
    detailed_stats=False,
    end_at=[
        "ad"
    ],
    has_bracket=False,
    id_=[
        10
    ],
    live_supported=True,
    modified_at=[
        "elit qui"
    ],
    name=[
        "dolor Ut "
    ],
    prizepool=[
        "reprehenderit"
    ],
    serie_id=[
        5
    ],
    slug=[
        "14rd"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        5
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCodmwShortTournaments(
    begin_at=[
        "laboris cupida"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "Excep"
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "nulla cu"
    ],
    name=[
        "officia est m"
    ],
    prizepool=[
        "nulla"
    ],
    serie_id=[
        3
    ],
    slug=[
        "uyx2u_a_t"
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
search=SearchOverCodmwShortTournaments(
    name="in dolor de",
    prizepool="incididunt dol",
    slug="q_",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.codmw_tournaments.get_codmw_tournaments_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_codmw_tournaments_upcoming

List upcoming CODMW tournaments

- HTTP Method: `GET`
- Endpoint: `/codmw/tournaments/upcoming`

**Parameters**

| Name     | Type                                                                            | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCodmwShortTournaments](../models/FilterOverCodmwShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCodmwShortTournaments](../models/RangeOverCodmwShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                       | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCodmwShortTournaments](../models/SearchOverCodmwShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                       | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                             | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCodmwShortTournaments, RangeOverCodmwShortTournaments, SearchOverCodmwShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCodmwShortTournaments(
    begin_at=[
        "n"
    ],
    detailed_stats=False,
    end_at=[
        "ad"
    ],
    has_bracket=False,
    id_=[
        10
    ],
    live_supported=True,
    modified_at=[
        "elit qui"
    ],
    name=[
        "dolor Ut "
    ],
    prizepool=[
        "reprehenderit"
    ],
    serie_id=[
        5
    ],
    slug=[
        "14rd"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        5
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCodmwShortTournaments(
    begin_at=[
        "laboris cupida"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "Excep"
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "nulla cu"
    ],
    name=[
        "officia est m"
    ],
    prizepool=[
        "nulla"
    ],
    serie_id=[
        3
    ],
    slug=[
        "uyx2u_a_t"
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
search=SearchOverCodmwShortTournaments(
    name="in dolor de",
    prizepool="incididunt dol",
    slug="q_",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.codmw_tournaments.get_codmw_tournaments_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
