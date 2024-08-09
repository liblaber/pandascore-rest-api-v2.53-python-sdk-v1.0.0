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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCodmwShortTournaments, RangeOverCodmwShortTournaments, SearchOverCodmwShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCodmwShortTournaments(
    begin_at=[
        "ad tempor"
    ],
    detailed_stats=True,
    end_at=[
        "Duis esse"
    ],
    has_bracket=False,
    id_=[
        2
    ],
    live_supported=False,
    modified_at=[
        "enim esse p"
    ],
    name=[
        "sit mollit"
    ],
    prizepool=[
        "labore offic"
    ],
    serie_id=[
        1
    ],
    slug=[
        "p_bnz1"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        5
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCodmwShortTournaments(
    begin_at=[
        "non ven"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "dolor"
    ],
    has_bracket=[
        False
    ],
    id_=[
        8
    ],
    modified_at=[
        "nostrud labo"
    ],
    name=[
        "est nisi sun"
    ],
    prizepool=[
        "fugiat el"
    ],
    serie_id=[
        1
    ],
    slug=[
        "ghzvnc"
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
search=SearchOverCodmwShortTournaments(
    name="ipsum ",
    prizepool="dolore ea",
    slug="1-543h88_",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCodmwShortTournaments, RangeOverCodmwShortTournaments, SearchOverCodmwShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCodmwShortTournaments(
    begin_at=[
        "ad tempor"
    ],
    detailed_stats=True,
    end_at=[
        "Duis esse"
    ],
    has_bracket=False,
    id_=[
        2
    ],
    live_supported=False,
    modified_at=[
        "enim esse p"
    ],
    name=[
        "sit mollit"
    ],
    prizepool=[
        "labore offic"
    ],
    serie_id=[
        1
    ],
    slug=[
        "p_bnz1"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        5
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCodmwShortTournaments(
    begin_at=[
        "non ven"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "dolor"
    ],
    has_bracket=[
        False
    ],
    id_=[
        8
    ],
    modified_at=[
        "nostrud labo"
    ],
    name=[
        "est nisi sun"
    ],
    prizepool=[
        "fugiat el"
    ],
    serie_id=[
        1
    ],
    slug=[
        "ghzvnc"
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
search=SearchOverCodmwShortTournaments(
    name="ipsum ",
    prizepool="dolore ea",
    slug="1-543h88_",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCodmwShortTournaments, RangeOverCodmwShortTournaments, SearchOverCodmwShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCodmwShortTournaments(
    begin_at=[
        "ad tempor"
    ],
    detailed_stats=True,
    end_at=[
        "Duis esse"
    ],
    has_bracket=False,
    id_=[
        2
    ],
    live_supported=False,
    modified_at=[
        "enim esse p"
    ],
    name=[
        "sit mollit"
    ],
    prizepool=[
        "labore offic"
    ],
    serie_id=[
        1
    ],
    slug=[
        "p_bnz1"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        5
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCodmwShortTournaments(
    begin_at=[
        "non ven"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "dolor"
    ],
    has_bracket=[
        False
    ],
    id_=[
        8
    ],
    modified_at=[
        "nostrud labo"
    ],
    name=[
        "est nisi sun"
    ],
    prizepool=[
        "fugiat el"
    ],
    serie_id=[
        1
    ],
    slug=[
        "ghzvnc"
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
search=SearchOverCodmwShortTournaments(
    name="ipsum ",
    prizepool="dolore ea",
    slug="1-543h88_",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCodmwShortTournaments, RangeOverCodmwShortTournaments, SearchOverCodmwShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCodmwShortTournaments(
    begin_at=[
        "ad tempor"
    ],
    detailed_stats=True,
    end_at=[
        "Duis esse"
    ],
    has_bracket=False,
    id_=[
        2
    ],
    live_supported=False,
    modified_at=[
        "enim esse p"
    ],
    name=[
        "sit mollit"
    ],
    prizepool=[
        "labore offic"
    ],
    serie_id=[
        1
    ],
    slug=[
        "p_bnz1"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        5
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCodmwShortTournaments(
    begin_at=[
        "non ven"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "dolor"
    ],
    has_bracket=[
        False
    ],
    id_=[
        8
    ],
    modified_at=[
        "nostrud labo"
    ],
    name=[
        "est nisi sun"
    ],
    prizepool=[
        "fugiat el"
    ],
    serie_id=[
        1
    ],
    slug=[
        "ghzvnc"
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
search=SearchOverCodmwShortTournaments(
    name="ipsum ",
    prizepool="dolore ea",
    slug="1-543h88_",
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

<!-- This file was generated by liblab | https://liblab.com/ -->
