# CounterStrikeTournamentsService

A list of all methods in the `CounterStrikeTournamentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                         | Description                                       |
| :-------------------------------------------------------------- | :------------------------------------------------ |
| [get_csgo_tournaments](#get_csgo_tournaments)                   | List tournaments for the Counter-Strike videogame |
| [get_csgo_tournaments_past](#get_csgo_tournaments_past)         | List past Counter-Strike tournaments              |
| [get_csgo_tournaments_running](#get_csgo_tournaments_running)   | List running Counter-Strike tournaments           |
| [get_csgo_tournaments_upcoming](#get_csgo_tournaments_upcoming) | List upcoming Counter-Strike tournaments          |

## get_csgo_tournaments

List tournaments for the Counter-Strike videogame

- HTTP Method: `GET`
- Endpoint: `/csgo/tournaments`

**Parameters**

| Name     | Type                                                                          | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCsgoShortTournaments](../models/FilterOverCsgoShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCsgoShortTournaments](../models/RangeOverCsgoShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCsgoShortTournaments](../models/SearchOverCsgoShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCsgoShortTournaments, RangeOverCsgoShortTournaments, SearchOverCsgoShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCsgoShortTournaments(
    begin_at=[
        "ad"
    ],
    detailed_stats=False,
    end_at=[
        "do cupidatat a"
    ],
    has_bracket=False,
    id_=[
        10
    ],
    live_supported=True,
    modified_at=[
        "fugiat aliqua t"
    ],
    name=[
        "nisioccaecat"
    ],
    prizepool=[
        "et la"
    ],
    serie_id=[
        1
    ],
    slug=[
        "by"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        2
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCsgoShortTournaments(
    begin_at=[
        "ma"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "n"
    ],
    has_bracket=[
        False
    ],
    id_=[
        6
    ],
    modified_at=[
        "ad exe"
    ],
    name=[
        "ullamco a"
    ],
    prizepool=[
        "qui pr"
    ],
    serie_id=[
        2
    ],
    slug=[
        "yst"
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
search=SearchOverCsgoShortTournaments(
    name="tempor repr",
    prizepool="nostrud ullamc",
    slug="5hi",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.counter_strike_tournaments.get_csgo_tournaments(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_csgo_tournaments_past

List past Counter-Strike tournaments

- HTTP Method: `GET`
- Endpoint: `/csgo/tournaments/past`

**Parameters**

| Name     | Type                                                                          | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCsgoShortTournaments](../models/FilterOverCsgoShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCsgoShortTournaments](../models/RangeOverCsgoShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCsgoShortTournaments](../models/SearchOverCsgoShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCsgoShortTournaments, RangeOverCsgoShortTournaments, SearchOverCsgoShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCsgoShortTournaments(
    begin_at=[
        "ad"
    ],
    detailed_stats=False,
    end_at=[
        "do cupidatat a"
    ],
    has_bracket=False,
    id_=[
        10
    ],
    live_supported=True,
    modified_at=[
        "fugiat aliqua t"
    ],
    name=[
        "nisioccaecat"
    ],
    prizepool=[
        "et la"
    ],
    serie_id=[
        1
    ],
    slug=[
        "by"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        2
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCsgoShortTournaments(
    begin_at=[
        "ma"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "n"
    ],
    has_bracket=[
        False
    ],
    id_=[
        6
    ],
    modified_at=[
        "ad exe"
    ],
    name=[
        "ullamco a"
    ],
    prizepool=[
        "qui pr"
    ],
    serie_id=[
        2
    ],
    slug=[
        "yst"
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
search=SearchOverCsgoShortTournaments(
    name="tempor repr",
    prizepool="nostrud ullamc",
    slug="5hi",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.counter_strike_tournaments.get_csgo_tournaments_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_csgo_tournaments_running

List running Counter-Strike tournaments

- HTTP Method: `GET`
- Endpoint: `/csgo/tournaments/running`

**Parameters**

| Name     | Type                                                                          | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCsgoShortTournaments](../models/FilterOverCsgoShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCsgoShortTournaments](../models/RangeOverCsgoShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCsgoShortTournaments](../models/SearchOverCsgoShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCsgoShortTournaments, RangeOverCsgoShortTournaments, SearchOverCsgoShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCsgoShortTournaments(
    begin_at=[
        "ad"
    ],
    detailed_stats=False,
    end_at=[
        "do cupidatat a"
    ],
    has_bracket=False,
    id_=[
        10
    ],
    live_supported=True,
    modified_at=[
        "fugiat aliqua t"
    ],
    name=[
        "nisioccaecat"
    ],
    prizepool=[
        "et la"
    ],
    serie_id=[
        1
    ],
    slug=[
        "by"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        2
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCsgoShortTournaments(
    begin_at=[
        "ma"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "n"
    ],
    has_bracket=[
        False
    ],
    id_=[
        6
    ],
    modified_at=[
        "ad exe"
    ],
    name=[
        "ullamco a"
    ],
    prizepool=[
        "qui pr"
    ],
    serie_id=[
        2
    ],
    slug=[
        "yst"
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
search=SearchOverCsgoShortTournaments(
    name="tempor repr",
    prizepool="nostrud ullamc",
    slug="5hi",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.counter_strike_tournaments.get_csgo_tournaments_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_csgo_tournaments_upcoming

List upcoming Counter-Strike tournaments

- HTTP Method: `GET`
- Endpoint: `/csgo/tournaments/upcoming`

**Parameters**

| Name     | Type                                                                          | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCsgoShortTournaments](../models/FilterOverCsgoShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCsgoShortTournaments](../models/RangeOverCsgoShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCsgoShortTournaments](../models/SearchOverCsgoShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCsgoShortTournaments, RangeOverCsgoShortTournaments, SearchOverCsgoShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCsgoShortTournaments(
    begin_at=[
        "ad"
    ],
    detailed_stats=False,
    end_at=[
        "do cupidatat a"
    ],
    has_bracket=False,
    id_=[
        10
    ],
    live_supported=True,
    modified_at=[
        "fugiat aliqua t"
    ],
    name=[
        "nisioccaecat"
    ],
    prizepool=[
        "et la"
    ],
    serie_id=[
        1
    ],
    slug=[
        "by"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        2
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCsgoShortTournaments(
    begin_at=[
        "ma"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "n"
    ],
    has_bracket=[
        False
    ],
    id_=[
        6
    ],
    modified_at=[
        "ad exe"
    ],
    name=[
        "ullamco a"
    ],
    prizepool=[
        "qui pr"
    ],
    serie_id=[
        2
    ],
    slug=[
        "yst"
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
search=SearchOverCsgoShortTournaments(
    name="tempor repr",
    prizepool="nostrud ullamc",
    slug="5hi",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.counter_strike_tournaments.get_csgo_tournaments_upcoming(
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
