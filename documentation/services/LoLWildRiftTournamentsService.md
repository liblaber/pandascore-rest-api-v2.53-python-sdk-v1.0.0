# LoLWildRiftTournamentsService

A list of all methods in the `LoLWildRiftTournamentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                           | Description                                      |
| :-------------------------------------------------------------------------------- | :----------------------------------------------- |
| [get_lol_wild_rift_tournaments](#get_lol_wild_rift_tournaments)                   | List tournaments for the LoL Wild Rift videogame |
| [get_lol_wild_rift_tournaments_past](#get_lol_wild_rift_tournaments_past)         | List past LoL Wild Rift tournaments              |
| [get_lol_wild_rift_tournaments_running](#get_lol_wild_rift_tournaments_running)   | List running LoL Wild Rift tournaments           |
| [get_lol_wild_rift_tournaments_upcoming](#get_lol_wild_rift_tournaments_upcoming) | List upcoming LoL Wild Rift tournaments          |

## get_lol_wild_rift_tournaments

List tournaments for the LoL Wild Rift videogame

- HTTP Method: `GET`
- Endpoint: `/lol-wild-rift/tournaments`

**Parameters**

| Name     | Type                                                                                        | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLolWildRiftShortTournaments](../models/FilterOverLolWildRiftShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLolWildRiftShortTournaments](../models/RangeOverLolWildRiftShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLolWildRiftShortTournaments](../models/SearchOverLolWildRiftShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLolWildRiftShortTournaments, RangeOverLolWildRiftShortTournaments, SearchOverLolWildRiftShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLolWildRiftShortTournaments(
    begin_at=[
        "e"
    ],
    detailed_stats=True,
    end_at=[
        "fugi"
    ],
    has_bracket=False,
    id_=[
        1
    ],
    live_supported=False,
    modified_at=[
        "Lorem in inc"
    ],
    name=[
        "aliquip la"
    ],
    prizepool=[
        "aliqua"
    ],
    serie_id=[
        9
    ],
    slug=[
        "r5854nkzr"
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
range=RangeOverLolWildRiftShortTournaments(
    begin_at=[
        "in"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "ea u"
    ],
    has_bracket=[
        True
    ],
    id_=[
        10
    ],
    modified_at=[
        "elit dolore"
    ],
    name=[
        "Duis p"
    ],
    prizepool=[
        "laboris in d"
    ],
    serie_id=[
        1
    ],
    slug=[
        "m5"
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
search=SearchOverLolWildRiftShortTournaments(
    name="et cillum repr",
    prizepool="Lorem a",
    slug="qhle8wo8",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.lo_l_wild_rift_tournaments.get_lol_wild_rift_tournaments(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_wild_rift_tournaments_past

List past LoL Wild Rift tournaments

- HTTP Method: `GET`
- Endpoint: `/lol-wild-rift/tournaments/past`

**Parameters**

| Name     | Type                                                                                        | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLolWildRiftShortTournaments](../models/FilterOverLolWildRiftShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLolWildRiftShortTournaments](../models/RangeOverLolWildRiftShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLolWildRiftShortTournaments](../models/SearchOverLolWildRiftShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLolWildRiftShortTournaments, RangeOverLolWildRiftShortTournaments, SearchOverLolWildRiftShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLolWildRiftShortTournaments(
    begin_at=[
        "e"
    ],
    detailed_stats=True,
    end_at=[
        "fugi"
    ],
    has_bracket=False,
    id_=[
        1
    ],
    live_supported=False,
    modified_at=[
        "Lorem in inc"
    ],
    name=[
        "aliquip la"
    ],
    prizepool=[
        "aliqua"
    ],
    serie_id=[
        9
    ],
    slug=[
        "r5854nkzr"
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
range=RangeOverLolWildRiftShortTournaments(
    begin_at=[
        "in"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "ea u"
    ],
    has_bracket=[
        True
    ],
    id_=[
        10
    ],
    modified_at=[
        "elit dolore"
    ],
    name=[
        "Duis p"
    ],
    prizepool=[
        "laboris in d"
    ],
    serie_id=[
        1
    ],
    slug=[
        "m5"
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
search=SearchOverLolWildRiftShortTournaments(
    name="et cillum repr",
    prizepool="Lorem a",
    slug="qhle8wo8",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.lo_l_wild_rift_tournaments.get_lol_wild_rift_tournaments_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_wild_rift_tournaments_running

List running LoL Wild Rift tournaments

- HTTP Method: `GET`
- Endpoint: `/lol-wild-rift/tournaments/running`

**Parameters**

| Name     | Type                                                                                        | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLolWildRiftShortTournaments](../models/FilterOverLolWildRiftShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLolWildRiftShortTournaments](../models/RangeOverLolWildRiftShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLolWildRiftShortTournaments](../models/SearchOverLolWildRiftShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLolWildRiftShortTournaments, RangeOverLolWildRiftShortTournaments, SearchOverLolWildRiftShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLolWildRiftShortTournaments(
    begin_at=[
        "e"
    ],
    detailed_stats=True,
    end_at=[
        "fugi"
    ],
    has_bracket=False,
    id_=[
        1
    ],
    live_supported=False,
    modified_at=[
        "Lorem in inc"
    ],
    name=[
        "aliquip la"
    ],
    prizepool=[
        "aliqua"
    ],
    serie_id=[
        9
    ],
    slug=[
        "r5854nkzr"
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
range=RangeOverLolWildRiftShortTournaments(
    begin_at=[
        "in"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "ea u"
    ],
    has_bracket=[
        True
    ],
    id_=[
        10
    ],
    modified_at=[
        "elit dolore"
    ],
    name=[
        "Duis p"
    ],
    prizepool=[
        "laboris in d"
    ],
    serie_id=[
        1
    ],
    slug=[
        "m5"
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
search=SearchOverLolWildRiftShortTournaments(
    name="et cillum repr",
    prizepool="Lorem a",
    slug="qhle8wo8",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.lo_l_wild_rift_tournaments.get_lol_wild_rift_tournaments_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_wild_rift_tournaments_upcoming

List upcoming LoL Wild Rift tournaments

- HTTP Method: `GET`
- Endpoint: `/lol-wild-rift/tournaments/upcoming`

**Parameters**

| Name     | Type                                                                                        | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLolWildRiftShortTournaments](../models/FilterOverLolWildRiftShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLolWildRiftShortTournaments](../models/RangeOverLolWildRiftShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLolWildRiftShortTournaments](../models/SearchOverLolWildRiftShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLolWildRiftShortTournaments, RangeOverLolWildRiftShortTournaments, SearchOverLolWildRiftShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLolWildRiftShortTournaments(
    begin_at=[
        "e"
    ],
    detailed_stats=True,
    end_at=[
        "fugi"
    ],
    has_bracket=False,
    id_=[
        1
    ],
    live_supported=False,
    modified_at=[
        "Lorem in inc"
    ],
    name=[
        "aliquip la"
    ],
    prizepool=[
        "aliqua"
    ],
    serie_id=[
        9
    ],
    slug=[
        "r5854nkzr"
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
range=RangeOverLolWildRiftShortTournaments(
    begin_at=[
        "in"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "ea u"
    ],
    has_bracket=[
        True
    ],
    id_=[
        10
    ],
    modified_at=[
        "elit dolore"
    ],
    name=[
        "Duis p"
    ],
    prizepool=[
        "laboris in d"
    ],
    serie_id=[
        1
    ],
    slug=[
        "m5"
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
search=SearchOverLolWildRiftShortTournaments(
    name="et cillum repr",
    prizepool="Lorem a",
    slug="qhle8wo8",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.lo_l_wild_rift_tournaments.get_lol_wild_rift_tournaments_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
