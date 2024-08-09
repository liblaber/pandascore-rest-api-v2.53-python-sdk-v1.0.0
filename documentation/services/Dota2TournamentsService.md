# Dota2TournamentsService

A list of all methods in the `Dota2TournamentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                           | Description                               |
| :---------------------------------------------------------------- | :---------------------------------------- |
| [get_dota2_tournaments](#get_dota2_tournaments)                   | List tournaments for the Dota 2 videogame |
| [get_dota2_tournaments_past](#get_dota2_tournaments_past)         | List past Dota 2 tournaments              |
| [get_dota2_tournaments_running](#get_dota2_tournaments_running)   | List running Dota 2 tournaments           |
| [get_dota2_tournaments_upcoming](#get_dota2_tournaments_upcoming) | List upcoming Dota 2 tournaments          |

## get_dota2_tournaments

List tournaments for the Dota 2 videogame

- HTTP Method: `GET`
- Endpoint: `/dota2/tournaments`

**Parameters**

| Name     | Type                                                                            | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverDota2ShortTournaments](../models/FilterOverDota2ShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverDota2ShortTournaments](../models/RangeOverDota2ShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                       | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverDota2ShortTournaments](../models/SearchOverDota2ShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                       | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                             | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverDota2ShortTournaments, RangeOverDota2ShortTournaments, SearchOverDota2ShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverDota2ShortTournaments(
    begin_at=[
        "elit laboris"
    ],
    detailed_stats=False,
    end_at=[
        "anim sunt"
    ],
    has_bracket=False,
    id_=[
        10
    ],
    live_supported=True,
    modified_at=[
        "lab"
    ],
    name=[
        "ea sunt pro"
    ],
    prizepool=[
        "incidid"
    ],
    serie_id=[
        10
    ],
    slug=[
        "sh2x1_ti7"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        3
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverDota2ShortTournaments(
    begin_at=[
        "dolor en"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "quis amet an"
    ],
    has_bracket=[
        True
    ],
    id_=[
        4
    ],
    modified_at=[
        "in "
    ],
    name=[
        "aute qui"
    ],
    prizepool=[
        "mollit et"
    ],
    serie_id=[
        8
    ],
    slug=[
        "i6"
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
search=SearchOverDota2ShortTournaments(
    name="minim tempor de",
    prizepool="Duis laborum ",
    slug="8xfo7sds7",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.dota2_tournaments.get_dota2_tournaments(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_dota2_tournaments_past

List past Dota 2 tournaments

- HTTP Method: `GET`
- Endpoint: `/dota2/tournaments/past`

**Parameters**

| Name     | Type                                                                            | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverDota2ShortTournaments](../models/FilterOverDota2ShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverDota2ShortTournaments](../models/RangeOverDota2ShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                       | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverDota2ShortTournaments](../models/SearchOverDota2ShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                       | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                             | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverDota2ShortTournaments, RangeOverDota2ShortTournaments, SearchOverDota2ShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverDota2ShortTournaments(
    begin_at=[
        "elit laboris"
    ],
    detailed_stats=False,
    end_at=[
        "anim sunt"
    ],
    has_bracket=False,
    id_=[
        10
    ],
    live_supported=True,
    modified_at=[
        "lab"
    ],
    name=[
        "ea sunt pro"
    ],
    prizepool=[
        "incidid"
    ],
    serie_id=[
        10
    ],
    slug=[
        "sh2x1_ti7"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        3
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverDota2ShortTournaments(
    begin_at=[
        "dolor en"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "quis amet an"
    ],
    has_bracket=[
        True
    ],
    id_=[
        4
    ],
    modified_at=[
        "in "
    ],
    name=[
        "aute qui"
    ],
    prizepool=[
        "mollit et"
    ],
    serie_id=[
        8
    ],
    slug=[
        "i6"
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
search=SearchOverDota2ShortTournaments(
    name="minim tempor de",
    prizepool="Duis laborum ",
    slug="8xfo7sds7",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.dota2_tournaments.get_dota2_tournaments_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_dota2_tournaments_running

List running Dota 2 tournaments

- HTTP Method: `GET`
- Endpoint: `/dota2/tournaments/running`

**Parameters**

| Name     | Type                                                                            | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverDota2ShortTournaments](../models/FilterOverDota2ShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverDota2ShortTournaments](../models/RangeOverDota2ShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                       | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverDota2ShortTournaments](../models/SearchOverDota2ShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                       | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                             | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverDota2ShortTournaments, RangeOverDota2ShortTournaments, SearchOverDota2ShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverDota2ShortTournaments(
    begin_at=[
        "elit laboris"
    ],
    detailed_stats=False,
    end_at=[
        "anim sunt"
    ],
    has_bracket=False,
    id_=[
        10
    ],
    live_supported=True,
    modified_at=[
        "lab"
    ],
    name=[
        "ea sunt pro"
    ],
    prizepool=[
        "incidid"
    ],
    serie_id=[
        10
    ],
    slug=[
        "sh2x1_ti7"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        3
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverDota2ShortTournaments(
    begin_at=[
        "dolor en"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "quis amet an"
    ],
    has_bracket=[
        True
    ],
    id_=[
        4
    ],
    modified_at=[
        "in "
    ],
    name=[
        "aute qui"
    ],
    prizepool=[
        "mollit et"
    ],
    serie_id=[
        8
    ],
    slug=[
        "i6"
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
search=SearchOverDota2ShortTournaments(
    name="minim tempor de",
    prizepool="Duis laborum ",
    slug="8xfo7sds7",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.dota2_tournaments.get_dota2_tournaments_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_dota2_tournaments_upcoming

List upcoming Dota 2 tournaments

- HTTP Method: `GET`
- Endpoint: `/dota2/tournaments/upcoming`

**Parameters**

| Name     | Type                                                                            | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverDota2ShortTournaments](../models/FilterOverDota2ShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverDota2ShortTournaments](../models/RangeOverDota2ShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                       | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverDota2ShortTournaments](../models/SearchOverDota2ShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                       | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                             | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverDota2ShortTournaments, RangeOverDota2ShortTournaments, SearchOverDota2ShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverDota2ShortTournaments(
    begin_at=[
        "elit laboris"
    ],
    detailed_stats=False,
    end_at=[
        "anim sunt"
    ],
    has_bracket=False,
    id_=[
        10
    ],
    live_supported=True,
    modified_at=[
        "lab"
    ],
    name=[
        "ea sunt pro"
    ],
    prizepool=[
        "incidid"
    ],
    serie_id=[
        10
    ],
    slug=[
        "sh2x1_ti7"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        3
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverDota2ShortTournaments(
    begin_at=[
        "dolor en"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "quis amet an"
    ],
    has_bracket=[
        True
    ],
    id_=[
        4
    ],
    modified_at=[
        "in "
    ],
    name=[
        "aute qui"
    ],
    prizepool=[
        "mollit et"
    ],
    serie_id=[
        8
    ],
    slug=[
        "i6"
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
search=SearchOverDota2ShortTournaments(
    name="minim tempor de",
    prizepool="Duis laborum ",
    slug="8xfo7sds7",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.dota2_tournaments.get_dota2_tournaments_upcoming(
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
