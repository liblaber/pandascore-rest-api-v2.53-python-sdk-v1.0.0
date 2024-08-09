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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLolWildRiftShortTournaments, RangeOverLolWildRiftShortTournaments, SearchOverLolWildRiftShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLolWildRiftShortTournaments(
    begin_at=[
        "ex"
    ],
    detailed_stats=True,
    end_at=[
        "ipsu"
    ],
    has_bracket=False,
    id_=[
        2
    ],
    live_supported=True,
    modified_at=[
        "aliqua dol"
    ],
    name=[
        "fugiat de"
    ],
    prizepool=[
        "ipsum"
    ],
    serie_id=[
        6
    ],
    slug=[
        "_5i7"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        10
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLolWildRiftShortTournaments(
    begin_at=[
        "culpa vol"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "sit"
    ],
    has_bracket=[
        True
    ],
    id_=[
        1
    ],
    modified_at=[
        "s"
    ],
    name=[
        "ullamco magna "
    ],
    prizepool=[
        "dolor in"
    ],
    serie_id=[
        4
    ],
    slug=[
        "_acxcod3epr"
    ],
    tier=[
        "a"
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
search=SearchOverLolWildRiftShortTournaments(
    name="cillum",
    prizepool="cillum aliqu",
    slug="omd-",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLolWildRiftShortTournaments, RangeOverLolWildRiftShortTournaments, SearchOverLolWildRiftShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLolWildRiftShortTournaments(
    begin_at=[
        "ex"
    ],
    detailed_stats=True,
    end_at=[
        "ipsu"
    ],
    has_bracket=False,
    id_=[
        2
    ],
    live_supported=True,
    modified_at=[
        "aliqua dol"
    ],
    name=[
        "fugiat de"
    ],
    prizepool=[
        "ipsum"
    ],
    serie_id=[
        6
    ],
    slug=[
        "_5i7"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        10
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLolWildRiftShortTournaments(
    begin_at=[
        "culpa vol"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "sit"
    ],
    has_bracket=[
        True
    ],
    id_=[
        1
    ],
    modified_at=[
        "s"
    ],
    name=[
        "ullamco magna "
    ],
    prizepool=[
        "dolor in"
    ],
    serie_id=[
        4
    ],
    slug=[
        "_acxcod3epr"
    ],
    tier=[
        "a"
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
search=SearchOverLolWildRiftShortTournaments(
    name="cillum",
    prizepool="cillum aliqu",
    slug="omd-",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLolWildRiftShortTournaments, RangeOverLolWildRiftShortTournaments, SearchOverLolWildRiftShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLolWildRiftShortTournaments(
    begin_at=[
        "ex"
    ],
    detailed_stats=True,
    end_at=[
        "ipsu"
    ],
    has_bracket=False,
    id_=[
        2
    ],
    live_supported=True,
    modified_at=[
        "aliqua dol"
    ],
    name=[
        "fugiat de"
    ],
    prizepool=[
        "ipsum"
    ],
    serie_id=[
        6
    ],
    slug=[
        "_5i7"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        10
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLolWildRiftShortTournaments(
    begin_at=[
        "culpa vol"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "sit"
    ],
    has_bracket=[
        True
    ],
    id_=[
        1
    ],
    modified_at=[
        "s"
    ],
    name=[
        "ullamco magna "
    ],
    prizepool=[
        "dolor in"
    ],
    serie_id=[
        4
    ],
    slug=[
        "_acxcod3epr"
    ],
    tier=[
        "a"
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
search=SearchOverLolWildRiftShortTournaments(
    name="cillum",
    prizepool="cillum aliqu",
    slug="omd-",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLolWildRiftShortTournaments, RangeOverLolWildRiftShortTournaments, SearchOverLolWildRiftShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLolWildRiftShortTournaments(
    begin_at=[
        "ex"
    ],
    detailed_stats=True,
    end_at=[
        "ipsu"
    ],
    has_bracket=False,
    id_=[
        2
    ],
    live_supported=True,
    modified_at=[
        "aliqua dol"
    ],
    name=[
        "fugiat de"
    ],
    prizepool=[
        "ipsum"
    ],
    serie_id=[
        6
    ],
    slug=[
        "_5i7"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        10
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLolWildRiftShortTournaments(
    begin_at=[
        "culpa vol"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "sit"
    ],
    has_bracket=[
        True
    ],
    id_=[
        1
    ],
    modified_at=[
        "s"
    ],
    name=[
        "ullamco magna "
    ],
    prizepool=[
        "dolor in"
    ],
    serie_id=[
        4
    ],
    slug=[
        "_acxcod3epr"
    ],
    tier=[
        "a"
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
search=SearchOverLolWildRiftShortTournaments(
    name="cillum",
    prizepool="cillum aliqu",
    slug="omd-",
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

<!-- This file was generated by liblab | https://liblab.com/ -->
