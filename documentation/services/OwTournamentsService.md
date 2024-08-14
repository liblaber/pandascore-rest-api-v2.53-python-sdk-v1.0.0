# OwTournamentsService

A list of all methods in the `OwTournamentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description                                  |
| :---------------------------------------------------------- | :------------------------------------------- |
| [get_ow_tournaments](#get_ow_tournaments)                   | List tournaments for the Overwatch videogame |
| [get_ow_tournaments_past](#get_ow_tournaments_past)         | List past Overwatch tournaments              |
| [get_ow_tournaments_running](#get_ow_tournaments_running)   | List running Overwatch tournaments           |
| [get_ow_tournaments_upcoming](#get_ow_tournaments_upcoming) | List upcoming Overwatch tournaments          |

## get_ow_tournaments

List tournaments for the Overwatch videogame

- HTTP Method: `GET`
- Endpoint: `/ow/tournaments`

**Parameters**

| Name     | Type                                                                      | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverOwShortTournaments](../models/FilterOverOwShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverOwShortTournaments](../models/RangeOverOwShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverOwShortTournaments](../models/SearchOverOwShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverOwShortTournaments, RangeOverOwShortTournaments, SearchOverOwShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverOwShortTournaments(
    begin_at=[
        "nulla adipi"
    ],
    detailed_stats=True,
    end_at=[
        "non "
    ],
    has_bracket=True,
    id_=[
        4
    ],
    live_supported=True,
    modified_at=[
        "nostrud"
    ],
    name=[
        "Excepteur "
    ],
    prizepool=[
        "ut in conse"
    ],
    serie_id=[
        6
    ],
    slug=[
        "whv5t1by8yq"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        7
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverOwShortTournaments(
    begin_at=[
        "e"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "est"
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "cupidatat "
    ],
    name=[
        "ullamco null"
    ],
    prizepool=[
        "consequ"
    ],
    serie_id=[
        7
    ],
    slug=[
        "9sb0udh"
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
search=SearchOverOwShortTournaments(
    name="elit ad velit i",
    prizepool="velit",
    slug="pd9o",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.ow_tournaments.get_ow_tournaments(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_ow_tournaments_past

List past Overwatch tournaments

- HTTP Method: `GET`
- Endpoint: `/ow/tournaments/past`

**Parameters**

| Name     | Type                                                                      | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverOwShortTournaments](../models/FilterOverOwShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverOwShortTournaments](../models/RangeOverOwShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverOwShortTournaments](../models/SearchOverOwShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverOwShortTournaments, RangeOverOwShortTournaments, SearchOverOwShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverOwShortTournaments(
    begin_at=[
        "nulla adipi"
    ],
    detailed_stats=True,
    end_at=[
        "non "
    ],
    has_bracket=True,
    id_=[
        4
    ],
    live_supported=True,
    modified_at=[
        "nostrud"
    ],
    name=[
        "Excepteur "
    ],
    prizepool=[
        "ut in conse"
    ],
    serie_id=[
        6
    ],
    slug=[
        "whv5t1by8yq"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        7
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverOwShortTournaments(
    begin_at=[
        "e"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "est"
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "cupidatat "
    ],
    name=[
        "ullamco null"
    ],
    prizepool=[
        "consequ"
    ],
    serie_id=[
        7
    ],
    slug=[
        "9sb0udh"
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
search=SearchOverOwShortTournaments(
    name="elit ad velit i",
    prizepool="velit",
    slug="pd9o",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.ow_tournaments.get_ow_tournaments_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_ow_tournaments_running

List running Overwatch tournaments

- HTTP Method: `GET`
- Endpoint: `/ow/tournaments/running`

**Parameters**

| Name     | Type                                                                      | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverOwShortTournaments](../models/FilterOverOwShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverOwShortTournaments](../models/RangeOverOwShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverOwShortTournaments](../models/SearchOverOwShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverOwShortTournaments, RangeOverOwShortTournaments, SearchOverOwShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverOwShortTournaments(
    begin_at=[
        "nulla adipi"
    ],
    detailed_stats=True,
    end_at=[
        "non "
    ],
    has_bracket=True,
    id_=[
        4
    ],
    live_supported=True,
    modified_at=[
        "nostrud"
    ],
    name=[
        "Excepteur "
    ],
    prizepool=[
        "ut in conse"
    ],
    serie_id=[
        6
    ],
    slug=[
        "whv5t1by8yq"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        7
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverOwShortTournaments(
    begin_at=[
        "e"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "est"
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "cupidatat "
    ],
    name=[
        "ullamco null"
    ],
    prizepool=[
        "consequ"
    ],
    serie_id=[
        7
    ],
    slug=[
        "9sb0udh"
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
search=SearchOverOwShortTournaments(
    name="elit ad velit i",
    prizepool="velit",
    slug="pd9o",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.ow_tournaments.get_ow_tournaments_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_ow_tournaments_upcoming

List upcoming Overwatch tournaments

- HTTP Method: `GET`
- Endpoint: `/ow/tournaments/upcoming`

**Parameters**

| Name     | Type                                                                      | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverOwShortTournaments](../models/FilterOverOwShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverOwShortTournaments](../models/RangeOverOwShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverOwShortTournaments](../models/SearchOverOwShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverOwShortTournaments, RangeOverOwShortTournaments, SearchOverOwShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverOwShortTournaments(
    begin_at=[
        "nulla adipi"
    ],
    detailed_stats=True,
    end_at=[
        "non "
    ],
    has_bracket=True,
    id_=[
        4
    ],
    live_supported=True,
    modified_at=[
        "nostrud"
    ],
    name=[
        "Excepteur "
    ],
    prizepool=[
        "ut in conse"
    ],
    serie_id=[
        6
    ],
    slug=[
        "whv5t1by8yq"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        7
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverOwShortTournaments(
    begin_at=[
        "e"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "est"
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "cupidatat "
    ],
    name=[
        "ullamco null"
    ],
    prizepool=[
        "consequ"
    ],
    serie_id=[
        7
    ],
    slug=[
        "9sb0udh"
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
search=SearchOverOwShortTournaments(
    name="elit ad velit i",
    prizepool="velit",
    slug="pd9o",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.ow_tournaments.get_ow_tournaments_upcoming(
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
