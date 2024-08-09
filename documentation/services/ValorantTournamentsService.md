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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverValorantShortTournaments, RangeOverValorantShortTournaments, SearchOverValorantShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverValorantShortTournaments(
    begin_at=[
        "officia in"
    ],
    detailed_stats=True,
    end_at=[
        "mollit e"
    ],
    has_bracket=True,
    id_=[
        7
    ],
    live_supported=False,
    modified_at=[
        "a"
    ],
    name=[
        "ullamco "
    ],
    prizepool=[
        "ex cul"
    ],
    serie_id=[
        9
    ],
    slug=[
        "e2vhv2hg3i"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        6
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverValorantShortTournaments(
    begin_at=[
        "deser"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "do pro"
    ],
    has_bracket=[
        False
    ],
    id_=[
        6
    ],
    modified_at=[
        "i"
    ],
    name=[
        "veniam "
    ],
    prizepool=[
        "tempor Except"
    ],
    serie_id=[
        2
    ],
    slug=[
        "m2czt"
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
search=SearchOverValorantShortTournaments(
    name="nisi es",
    prizepool="Duis eiusmod ",
    slug="roj8g5wbb",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverValorantShortTournaments, RangeOverValorantShortTournaments, SearchOverValorantShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverValorantShortTournaments(
    begin_at=[
        "officia in"
    ],
    detailed_stats=True,
    end_at=[
        "mollit e"
    ],
    has_bracket=True,
    id_=[
        7
    ],
    live_supported=False,
    modified_at=[
        "a"
    ],
    name=[
        "ullamco "
    ],
    prizepool=[
        "ex cul"
    ],
    serie_id=[
        9
    ],
    slug=[
        "e2vhv2hg3i"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        6
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverValorantShortTournaments(
    begin_at=[
        "deser"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "do pro"
    ],
    has_bracket=[
        False
    ],
    id_=[
        6
    ],
    modified_at=[
        "i"
    ],
    name=[
        "veniam "
    ],
    prizepool=[
        "tempor Except"
    ],
    serie_id=[
        2
    ],
    slug=[
        "m2czt"
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
search=SearchOverValorantShortTournaments(
    name="nisi es",
    prizepool="Duis eiusmod ",
    slug="roj8g5wbb",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverValorantShortTournaments, RangeOverValorantShortTournaments, SearchOverValorantShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverValorantShortTournaments(
    begin_at=[
        "officia in"
    ],
    detailed_stats=True,
    end_at=[
        "mollit e"
    ],
    has_bracket=True,
    id_=[
        7
    ],
    live_supported=False,
    modified_at=[
        "a"
    ],
    name=[
        "ullamco "
    ],
    prizepool=[
        "ex cul"
    ],
    serie_id=[
        9
    ],
    slug=[
        "e2vhv2hg3i"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        6
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverValorantShortTournaments(
    begin_at=[
        "deser"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "do pro"
    ],
    has_bracket=[
        False
    ],
    id_=[
        6
    ],
    modified_at=[
        "i"
    ],
    name=[
        "veniam "
    ],
    prizepool=[
        "tempor Except"
    ],
    serie_id=[
        2
    ],
    slug=[
        "m2czt"
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
search=SearchOverValorantShortTournaments(
    name="nisi es",
    prizepool="Duis eiusmod ",
    slug="roj8g5wbb",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverValorantShortTournaments, RangeOverValorantShortTournaments, SearchOverValorantShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverValorantShortTournaments(
    begin_at=[
        "officia in"
    ],
    detailed_stats=True,
    end_at=[
        "mollit e"
    ],
    has_bracket=True,
    id_=[
        7
    ],
    live_supported=False,
    modified_at=[
        "a"
    ],
    name=[
        "ullamco "
    ],
    prizepool=[
        "ex cul"
    ],
    serie_id=[
        9
    ],
    slug=[
        "e2vhv2hg3i"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        6
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverValorantShortTournaments(
    begin_at=[
        "deser"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "do pro"
    ],
    has_bracket=[
        False
    ],
    id_=[
        6
    ],
    modified_at=[
        "i"
    ],
    name=[
        "veniam "
    ],
    prizepool=[
        "tempor Except"
    ],
    serie_id=[
        2
    ],
    slug=[
        "m2czt"
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
search=SearchOverValorantShortTournaments(
    name="nisi es",
    prizepool="Duis eiusmod ",
    slug="roj8g5wbb",
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

<!-- This file was generated by liblab | https://liblab.com/ -->
