# LoLTournamentsService

A list of all methods in the `LoLTournamentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description                                          |
| :------------------------------------------------------------ | :--------------------------------------------------- |
| [get_lol_tournaments](#get_lol_tournaments)                   | List tournaments for the League of Legends videogame |
| [get_lol_tournaments_past](#get_lol_tournaments_past)         | List past League of Legends tournaments              |
| [get_lol_tournaments_running](#get_lol_tournaments_running)   | List running League of Legends tournaments           |
| [get_lol_tournaments_upcoming](#get_lol_tournaments_upcoming) | List upcoming League of Legends tournaments          |

## get_lol_tournaments

List tournaments for the League of Legends videogame

- HTTP Method: `GET`
- Endpoint: `/lol/tournaments`

**Parameters**

| Name     | Type                                                                        | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLShortTournaments](../models/FilterOverLoLShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLShortTournaments](../models/RangeOverLoLShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLShortTournaments](../models/SearchOverLoLShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLShortTournaments, RangeOverLoLShortTournaments, SearchOverLoLShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLoLShortTournaments(
    begin_at=[
        "Excep"
    ],
    detailed_stats=True,
    end_at=[
        "fugiat"
    ],
    has_bracket=False,
    id_=[
        4
    ],
    live_supported=True,
    modified_at=[
        "culpa"
    ],
    name=[
        "Lorem nulla "
    ],
    prizepool=[
        "elit i"
    ],
    serie_id=[
        10
    ],
    slug=[
        "p3_tn7"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        8
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLoLShortTournaments(
    begin_at=[
        "amet ullamco"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "cupidatat"
    ],
    has_bracket=[
        True
    ],
    id_=[
        10
    ],
    modified_at=[
        "irure"
    ],
    name=[
        "eiusmod "
    ],
    prizepool=[
        "id culp"
    ],
    serie_id=[
        10
    ],
    slug=[
        "8dyh"
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
search=SearchOverLoLShortTournaments(
    name="sed p",
    prizepool="laboris ut c",
    slug="pbrmjq9u2_",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.lo_l_tournaments.get_lol_tournaments(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_tournaments_past

List past League of Legends tournaments

- HTTP Method: `GET`
- Endpoint: `/lol/tournaments/past`

**Parameters**

| Name     | Type                                                                        | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLShortTournaments](../models/FilterOverLoLShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLShortTournaments](../models/RangeOverLoLShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLShortTournaments](../models/SearchOverLoLShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLShortTournaments, RangeOverLoLShortTournaments, SearchOverLoLShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLoLShortTournaments(
    begin_at=[
        "Excep"
    ],
    detailed_stats=True,
    end_at=[
        "fugiat"
    ],
    has_bracket=False,
    id_=[
        4
    ],
    live_supported=True,
    modified_at=[
        "culpa"
    ],
    name=[
        "Lorem nulla "
    ],
    prizepool=[
        "elit i"
    ],
    serie_id=[
        10
    ],
    slug=[
        "p3_tn7"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        8
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLoLShortTournaments(
    begin_at=[
        "amet ullamco"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "cupidatat"
    ],
    has_bracket=[
        True
    ],
    id_=[
        10
    ],
    modified_at=[
        "irure"
    ],
    name=[
        "eiusmod "
    ],
    prizepool=[
        "id culp"
    ],
    serie_id=[
        10
    ],
    slug=[
        "8dyh"
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
search=SearchOverLoLShortTournaments(
    name="sed p",
    prizepool="laboris ut c",
    slug="pbrmjq9u2_",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.lo_l_tournaments.get_lol_tournaments_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_tournaments_running

List running League of Legends tournaments

- HTTP Method: `GET`
- Endpoint: `/lol/tournaments/running`

**Parameters**

| Name     | Type                                                                        | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLShortTournaments](../models/FilterOverLoLShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLShortTournaments](../models/RangeOverLoLShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLShortTournaments](../models/SearchOverLoLShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLShortTournaments, RangeOverLoLShortTournaments, SearchOverLoLShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLoLShortTournaments(
    begin_at=[
        "Excep"
    ],
    detailed_stats=True,
    end_at=[
        "fugiat"
    ],
    has_bracket=False,
    id_=[
        4
    ],
    live_supported=True,
    modified_at=[
        "culpa"
    ],
    name=[
        "Lorem nulla "
    ],
    prizepool=[
        "elit i"
    ],
    serie_id=[
        10
    ],
    slug=[
        "p3_tn7"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        8
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLoLShortTournaments(
    begin_at=[
        "amet ullamco"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "cupidatat"
    ],
    has_bracket=[
        True
    ],
    id_=[
        10
    ],
    modified_at=[
        "irure"
    ],
    name=[
        "eiusmod "
    ],
    prizepool=[
        "id culp"
    ],
    serie_id=[
        10
    ],
    slug=[
        "8dyh"
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
search=SearchOverLoLShortTournaments(
    name="sed p",
    prizepool="laboris ut c",
    slug="pbrmjq9u2_",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.lo_l_tournaments.get_lol_tournaments_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_tournaments_upcoming

List upcoming League of Legends tournaments

- HTTP Method: `GET`
- Endpoint: `/lol/tournaments/upcoming`

**Parameters**

| Name     | Type                                                                        | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLShortTournaments](../models/FilterOverLoLShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLShortTournaments](../models/RangeOverLoLShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLShortTournaments](../models/SearchOverLoLShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLShortTournaments, RangeOverLoLShortTournaments, SearchOverLoLShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLoLShortTournaments(
    begin_at=[
        "Excep"
    ],
    detailed_stats=True,
    end_at=[
        "fugiat"
    ],
    has_bracket=False,
    id_=[
        4
    ],
    live_supported=True,
    modified_at=[
        "culpa"
    ],
    name=[
        "Lorem nulla "
    ],
    prizepool=[
        "elit i"
    ],
    serie_id=[
        10
    ],
    slug=[
        "p3_tn7"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        8
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLoLShortTournaments(
    begin_at=[
        "amet ullamco"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "cupidatat"
    ],
    has_bracket=[
        True
    ],
    id_=[
        10
    ],
    modified_at=[
        "irure"
    ],
    name=[
        "eiusmod "
    ],
    prizepool=[
        "id culp"
    ],
    serie_id=[
        10
    ],
    slug=[
        "8dyh"
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
search=SearchOverLoLShortTournaments(
    name="sed p",
    prizepool="laboris ut c",
    slug="pbrmjq9u2_",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.lo_l_tournaments.get_lol_tournaments_upcoming(
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
