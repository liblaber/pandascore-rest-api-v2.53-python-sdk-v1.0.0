# KogTournamentsService

A list of all methods in the `KogTournamentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description                                      |
| :------------------------------------------------------------ | :----------------------------------------------- |
| [get_kog_tournaments](#get_kog_tournaments)                   | List tournaments for the King of Glory videogame |
| [get_kog_tournaments_past](#get_kog_tournaments_past)         | List past King of Glory tournaments              |
| [get_kog_tournaments_running](#get_kog_tournaments_running)   | List running King of Glory tournaments           |
| [get_kog_tournaments_upcoming](#get_kog_tournaments_upcoming) | List upcoming King of Glory tournaments          |

## get_kog_tournaments

List tournaments for the King of Glory videogame

- HTTP Method: `GET`
- Endpoint: `/kog/tournaments`

**Parameters**

| Name     | Type                                                                        | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverKogShortTournaments](../models/FilterOverKogShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverKogShortTournaments](../models/RangeOverKogShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverKogShortTournaments](../models/SearchOverKogShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverKogShortTournaments, RangeOverKogShortTournaments, SearchOverKogShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverKogShortTournaments(
    begin_at=[
        "voluptate i"
    ],
    detailed_stats=True,
    end_at=[
        "Lo"
    ],
    has_bracket=False,
    id_=[
        8
    ],
    live_supported=False,
    modified_at=[
        "adipisici"
    ],
    name=[
        "deserunt "
    ],
    prizepool=[
        "incidi"
    ],
    serie_id=[
        8
    ],
    slug=[
        "jb0"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        4
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverKogShortTournaments(
    begin_at=[
        "do des"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "a"
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "ut D"
    ],
    name=[
        "et ea "
    ],
    prizepool=[
        "ex et Lo"
    ],
    serie_id=[
        3
    ],
    slug=[
        "hpq1rop"
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
search=SearchOverKogShortTournaments(
    name="amet ut ",
    prizepool="laborum in v",
    slug="csu",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.kog_tournaments.get_kog_tournaments(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_kog_tournaments_past

List past King of Glory tournaments

- HTTP Method: `GET`
- Endpoint: `/kog/tournaments/past`

**Parameters**

| Name     | Type                                                                        | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverKogShortTournaments](../models/FilterOverKogShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverKogShortTournaments](../models/RangeOverKogShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverKogShortTournaments](../models/SearchOverKogShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverKogShortTournaments, RangeOverKogShortTournaments, SearchOverKogShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverKogShortTournaments(
    begin_at=[
        "voluptate i"
    ],
    detailed_stats=True,
    end_at=[
        "Lo"
    ],
    has_bracket=False,
    id_=[
        8
    ],
    live_supported=False,
    modified_at=[
        "adipisici"
    ],
    name=[
        "deserunt "
    ],
    prizepool=[
        "incidi"
    ],
    serie_id=[
        8
    ],
    slug=[
        "jb0"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        4
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverKogShortTournaments(
    begin_at=[
        "do des"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "a"
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "ut D"
    ],
    name=[
        "et ea "
    ],
    prizepool=[
        "ex et Lo"
    ],
    serie_id=[
        3
    ],
    slug=[
        "hpq1rop"
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
search=SearchOverKogShortTournaments(
    name="amet ut ",
    prizepool="laborum in v",
    slug="csu",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.kog_tournaments.get_kog_tournaments_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_kog_tournaments_running

List running King of Glory tournaments

- HTTP Method: `GET`
- Endpoint: `/kog/tournaments/running`

**Parameters**

| Name     | Type                                                                        | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverKogShortTournaments](../models/FilterOverKogShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverKogShortTournaments](../models/RangeOverKogShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverKogShortTournaments](../models/SearchOverKogShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverKogShortTournaments, RangeOverKogShortTournaments, SearchOverKogShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverKogShortTournaments(
    begin_at=[
        "voluptate i"
    ],
    detailed_stats=True,
    end_at=[
        "Lo"
    ],
    has_bracket=False,
    id_=[
        8
    ],
    live_supported=False,
    modified_at=[
        "adipisici"
    ],
    name=[
        "deserunt "
    ],
    prizepool=[
        "incidi"
    ],
    serie_id=[
        8
    ],
    slug=[
        "jb0"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        4
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverKogShortTournaments(
    begin_at=[
        "do des"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "a"
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "ut D"
    ],
    name=[
        "et ea "
    ],
    prizepool=[
        "ex et Lo"
    ],
    serie_id=[
        3
    ],
    slug=[
        "hpq1rop"
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
search=SearchOverKogShortTournaments(
    name="amet ut ",
    prizepool="laborum in v",
    slug="csu",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.kog_tournaments.get_kog_tournaments_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_kog_tournaments_upcoming

List upcoming King of Glory tournaments

- HTTP Method: `GET`
- Endpoint: `/kog/tournaments/upcoming`

**Parameters**

| Name     | Type                                                                        | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverKogShortTournaments](../models/FilterOverKogShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverKogShortTournaments](../models/RangeOverKogShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverKogShortTournaments](../models/SearchOverKogShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverKogShortTournaments, RangeOverKogShortTournaments, SearchOverKogShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverKogShortTournaments(
    begin_at=[
        "voluptate i"
    ],
    detailed_stats=True,
    end_at=[
        "Lo"
    ],
    has_bracket=False,
    id_=[
        8
    ],
    live_supported=False,
    modified_at=[
        "adipisici"
    ],
    name=[
        "deserunt "
    ],
    prizepool=[
        "incidi"
    ],
    serie_id=[
        8
    ],
    slug=[
        "jb0"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        4
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverKogShortTournaments(
    begin_at=[
        "do des"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "a"
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "ut D"
    ],
    name=[
        "et ea "
    ],
    prizepool=[
        "ex et Lo"
    ],
    serie_id=[
        3
    ],
    slug=[
        "hpq1rop"
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
search=SearchOverKogShortTournaments(
    name="amet ut ",
    prizepool="laborum in v",
    slug="csu",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.kog_tournaments.get_kog_tournaments_upcoming(
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
