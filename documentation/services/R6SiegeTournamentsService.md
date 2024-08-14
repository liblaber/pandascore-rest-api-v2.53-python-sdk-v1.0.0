# R6SiegeTournamentsService

A list of all methods in the `R6SiegeTournamentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                               | Description                                          |
| :-------------------------------------------------------------------- | :--------------------------------------------------- |
| [get_r6siege_tournaments](#get_r6siege_tournaments)                   | List tournaments for the Rainbow Six Siege videogame |
| [get_r6siege_tournaments_past](#get_r6siege_tournaments_past)         | List past Rainbow Six Siege tournaments              |
| [get_r6siege_tournaments_running](#get_r6siege_tournaments_running)   | List running Rainbow Six Siege tournaments           |
| [get_r6siege_tournaments_upcoming](#get_r6siege_tournaments_upcoming) | List upcoming Rainbow Six Siege tournaments          |

## get_r6siege_tournaments

List tournaments for the Rainbow Six Siege videogame

- HTTP Method: `GET`
- Endpoint: `/r6siege/tournaments`

**Parameters**

| Name     | Type                                                                                | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverR6SiegeShortTournaments](../models/FilterOverR6SiegeShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverR6SiegeShortTournaments](../models/RangeOverR6SiegeShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverR6SiegeShortTournaments](../models/SearchOverR6SiegeShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverR6SiegeShortTournaments, RangeOverR6SiegeShortTournaments, SearchOverR6SiegeShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverR6SiegeShortTournaments(
    begin_at=[
        "dolore esse"
    ],
    detailed_stats=True,
    end_at=[
        "aliquip"
    ],
    has_bracket=False,
    id_=[
        10
    ],
    live_supported=True,
    modified_at=[
        "aliqua fu"
    ],
    name=[
        "quisullamc"
    ],
    prizepool=[
        "nulla"
    ],
    serie_id=[
        3
    ],
    slug=[
        "8"
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
range=RangeOverR6SiegeShortTournaments(
    begin_at=[
        "veniam "
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "adipis"
    ],
    has_bracket=[
        True
    ],
    id_=[
        4
    ],
    modified_at=[
        "dolore eli"
    ],
    name=[
        "exercitat"
    ],
    prizepool=[
        "indolor eiu"
    ],
    serie_id=[
        9
    ],
    slug=[
        "owgd"
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
search=SearchOverR6SiegeShortTournaments(
    name="ullam",
    prizepool="incididun",
    slug="6ix7vd2l-ow",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.r6_siege_tournaments.get_r6siege_tournaments(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_r6siege_tournaments_past

List past Rainbow Six Siege tournaments

- HTTP Method: `GET`
- Endpoint: `/r6siege/tournaments/past`

**Parameters**

| Name     | Type                                                                                | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverR6SiegeShortTournaments](../models/FilterOverR6SiegeShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverR6SiegeShortTournaments](../models/RangeOverR6SiegeShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverR6SiegeShortTournaments](../models/SearchOverR6SiegeShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverR6SiegeShortTournaments, RangeOverR6SiegeShortTournaments, SearchOverR6SiegeShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverR6SiegeShortTournaments(
    begin_at=[
        "dolore esse"
    ],
    detailed_stats=True,
    end_at=[
        "aliquip"
    ],
    has_bracket=False,
    id_=[
        10
    ],
    live_supported=True,
    modified_at=[
        "aliqua fu"
    ],
    name=[
        "quisullamc"
    ],
    prizepool=[
        "nulla"
    ],
    serie_id=[
        3
    ],
    slug=[
        "8"
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
range=RangeOverR6SiegeShortTournaments(
    begin_at=[
        "veniam "
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "adipis"
    ],
    has_bracket=[
        True
    ],
    id_=[
        4
    ],
    modified_at=[
        "dolore eli"
    ],
    name=[
        "exercitat"
    ],
    prizepool=[
        "indolor eiu"
    ],
    serie_id=[
        9
    ],
    slug=[
        "owgd"
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
search=SearchOverR6SiegeShortTournaments(
    name="ullam",
    prizepool="incididun",
    slug="6ix7vd2l-ow",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.r6_siege_tournaments.get_r6siege_tournaments_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_r6siege_tournaments_running

List running Rainbow Six Siege tournaments

- HTTP Method: `GET`
- Endpoint: `/r6siege/tournaments/running`

**Parameters**

| Name     | Type                                                                                | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverR6SiegeShortTournaments](../models/FilterOverR6SiegeShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverR6SiegeShortTournaments](../models/RangeOverR6SiegeShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverR6SiegeShortTournaments](../models/SearchOverR6SiegeShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverR6SiegeShortTournaments, RangeOverR6SiegeShortTournaments, SearchOverR6SiegeShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverR6SiegeShortTournaments(
    begin_at=[
        "dolore esse"
    ],
    detailed_stats=True,
    end_at=[
        "aliquip"
    ],
    has_bracket=False,
    id_=[
        10
    ],
    live_supported=True,
    modified_at=[
        "aliqua fu"
    ],
    name=[
        "quisullamc"
    ],
    prizepool=[
        "nulla"
    ],
    serie_id=[
        3
    ],
    slug=[
        "8"
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
range=RangeOverR6SiegeShortTournaments(
    begin_at=[
        "veniam "
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "adipis"
    ],
    has_bracket=[
        True
    ],
    id_=[
        4
    ],
    modified_at=[
        "dolore eli"
    ],
    name=[
        "exercitat"
    ],
    prizepool=[
        "indolor eiu"
    ],
    serie_id=[
        9
    ],
    slug=[
        "owgd"
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
search=SearchOverR6SiegeShortTournaments(
    name="ullam",
    prizepool="incididun",
    slug="6ix7vd2l-ow",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.r6_siege_tournaments.get_r6siege_tournaments_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_r6siege_tournaments_upcoming

List upcoming Rainbow Six Siege tournaments

- HTTP Method: `GET`
- Endpoint: `/r6siege/tournaments/upcoming`

**Parameters**

| Name     | Type                                                                                | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverR6SiegeShortTournaments](../models/FilterOverR6SiegeShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverR6SiegeShortTournaments](../models/RangeOverR6SiegeShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverR6SiegeShortTournaments](../models/SearchOverR6SiegeShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverR6SiegeShortTournaments, RangeOverR6SiegeShortTournaments, SearchOverR6SiegeShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverR6SiegeShortTournaments(
    begin_at=[
        "dolore esse"
    ],
    detailed_stats=True,
    end_at=[
        "aliquip"
    ],
    has_bracket=False,
    id_=[
        10
    ],
    live_supported=True,
    modified_at=[
        "aliqua fu"
    ],
    name=[
        "quisullamc"
    ],
    prizepool=[
        "nulla"
    ],
    serie_id=[
        3
    ],
    slug=[
        "8"
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
range=RangeOverR6SiegeShortTournaments(
    begin_at=[
        "veniam "
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "adipis"
    ],
    has_bracket=[
        True
    ],
    id_=[
        4
    ],
    modified_at=[
        "dolore eli"
    ],
    name=[
        "exercitat"
    ],
    prizepool=[
        "indolor eiu"
    ],
    serie_id=[
        9
    ],
    slug=[
        "owgd"
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
search=SearchOverR6SiegeShortTournaments(
    name="ullam",
    prizepool="incididun",
    slug="6ix7vd2l-ow",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.r6_siege_tournaments.get_r6siege_tournaments_upcoming(
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
