# StarCraft2TournamentsService

A list of all methods in the `StarCraft2TournamentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                       | Description                                    |
| :---------------------------------------------------------------------------- | :--------------------------------------------- |
| [get_starcraft_2_tournaments](#get_starcraft_2_tournaments)                   | List tournaments for the StarCraft 2 videogame |
| [get_starcraft_2_tournaments_past](#get_starcraft_2_tournaments_past)         | List past StarCraft 2 tournaments              |
| [get_starcraft_2_tournaments_running](#get_starcraft_2_tournaments_running)   | List running StarCraft 2 tournaments           |
| [get_starcraft_2_tournaments_upcoming](#get_starcraft_2_tournaments_upcoming) | List upcoming StarCraft 2 tournaments          |

## get_starcraft_2_tournaments

List tournaments for the StarCraft 2 videogame

- HTTP Method: `GET`
- Endpoint: `/starcraft-2/tournaments`

**Parameters**

| Name     | Type                                                                                      | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraft2ShortTournaments](../models/FilterOverStarcraft2ShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraft2ShortTournaments](../models/RangeOverStarcraft2ShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraft2ShortTournaments](../models/SearchOverStarcraft2ShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraft2ShortTournaments, RangeOverStarcraft2ShortTournaments, SearchOverStarcraft2ShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraft2ShortTournaments(
    begin_at=[
        "labor"
    ],
    detailed_stats=True,
    end_at=[
        "incididunt "
    ],
    has_bracket=True,
    id_=[
        9
    ],
    live_supported=False,
    modified_at=[
        "sint"
    ],
    name=[
        "mollit Duis"
    ],
    prizepool=[
        "tempor"
    ],
    serie_id=[
        9
    ],
    slug=[
        "nsn"
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
range=RangeOverStarcraft2ShortTournaments(
    begin_at=[
        "incididunt "
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "mollit sit co"
    ],
    has_bracket=[
        False
    ],
    id_=[
        8
    ],
    modified_at=[
        "tempor"
    ],
    name=[
        "ex Ex"
    ],
    prizepool=[
        "magna"
    ],
    serie_id=[
        9
    ],
    slug=[
        "nui1sjb1"
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
search=SearchOverStarcraft2ShortTournaments(
    name="mollit ea",
    prizepool="proident dolore",
    slug="2fh161cl8e",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.star_craft_2_tournaments.get_starcraft_2_tournaments(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_2_tournaments_past

List past StarCraft 2 tournaments

- HTTP Method: `GET`
- Endpoint: `/starcraft-2/tournaments/past`

**Parameters**

| Name     | Type                                                                                      | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraft2ShortTournaments](../models/FilterOverStarcraft2ShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraft2ShortTournaments](../models/RangeOverStarcraft2ShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraft2ShortTournaments](../models/SearchOverStarcraft2ShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraft2ShortTournaments, RangeOverStarcraft2ShortTournaments, SearchOverStarcraft2ShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraft2ShortTournaments(
    begin_at=[
        "labor"
    ],
    detailed_stats=True,
    end_at=[
        "incididunt "
    ],
    has_bracket=True,
    id_=[
        9
    ],
    live_supported=False,
    modified_at=[
        "sint"
    ],
    name=[
        "mollit Duis"
    ],
    prizepool=[
        "tempor"
    ],
    serie_id=[
        9
    ],
    slug=[
        "nsn"
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
range=RangeOverStarcraft2ShortTournaments(
    begin_at=[
        "incididunt "
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "mollit sit co"
    ],
    has_bracket=[
        False
    ],
    id_=[
        8
    ],
    modified_at=[
        "tempor"
    ],
    name=[
        "ex Ex"
    ],
    prizepool=[
        "magna"
    ],
    serie_id=[
        9
    ],
    slug=[
        "nui1sjb1"
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
search=SearchOverStarcraft2ShortTournaments(
    name="mollit ea",
    prizepool="proident dolore",
    slug="2fh161cl8e",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.star_craft_2_tournaments.get_starcraft_2_tournaments_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_2_tournaments_running

List running StarCraft 2 tournaments

- HTTP Method: `GET`
- Endpoint: `/starcraft-2/tournaments/running`

**Parameters**

| Name     | Type                                                                                      | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraft2ShortTournaments](../models/FilterOverStarcraft2ShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraft2ShortTournaments](../models/RangeOverStarcraft2ShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraft2ShortTournaments](../models/SearchOverStarcraft2ShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraft2ShortTournaments, RangeOverStarcraft2ShortTournaments, SearchOverStarcraft2ShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraft2ShortTournaments(
    begin_at=[
        "labor"
    ],
    detailed_stats=True,
    end_at=[
        "incididunt "
    ],
    has_bracket=True,
    id_=[
        9
    ],
    live_supported=False,
    modified_at=[
        "sint"
    ],
    name=[
        "mollit Duis"
    ],
    prizepool=[
        "tempor"
    ],
    serie_id=[
        9
    ],
    slug=[
        "nsn"
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
range=RangeOverStarcraft2ShortTournaments(
    begin_at=[
        "incididunt "
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "mollit sit co"
    ],
    has_bracket=[
        False
    ],
    id_=[
        8
    ],
    modified_at=[
        "tempor"
    ],
    name=[
        "ex Ex"
    ],
    prizepool=[
        "magna"
    ],
    serie_id=[
        9
    ],
    slug=[
        "nui1sjb1"
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
search=SearchOverStarcraft2ShortTournaments(
    name="mollit ea",
    prizepool="proident dolore",
    slug="2fh161cl8e",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.star_craft_2_tournaments.get_starcraft_2_tournaments_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_2_tournaments_upcoming

List upcoming StarCraft 2 tournaments

- HTTP Method: `GET`
- Endpoint: `/starcraft-2/tournaments/upcoming`

**Parameters**

| Name     | Type                                                                                      | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraft2ShortTournaments](../models/FilterOverStarcraft2ShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraft2ShortTournaments](../models/RangeOverStarcraft2ShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraft2ShortTournaments](../models/SearchOverStarcraft2ShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraft2ShortTournaments, RangeOverStarcraft2ShortTournaments, SearchOverStarcraft2ShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraft2ShortTournaments(
    begin_at=[
        "labor"
    ],
    detailed_stats=True,
    end_at=[
        "incididunt "
    ],
    has_bracket=True,
    id_=[
        9
    ],
    live_supported=False,
    modified_at=[
        "sint"
    ],
    name=[
        "mollit Duis"
    ],
    prizepool=[
        "tempor"
    ],
    serie_id=[
        9
    ],
    slug=[
        "nsn"
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
range=RangeOverStarcraft2ShortTournaments(
    begin_at=[
        "incididunt "
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "mollit sit co"
    ],
    has_bracket=[
        False
    ],
    id_=[
        8
    ],
    modified_at=[
        "tempor"
    ],
    name=[
        "ex Ex"
    ],
    prizepool=[
        "magna"
    ],
    serie_id=[
        9
    ],
    slug=[
        "nui1sjb1"
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
search=SearchOverStarcraft2ShortTournaments(
    name="mollit ea",
    prizepool="proident dolore",
    slug="2fh161cl8e",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.star_craft_2_tournaments.get_starcraft_2_tournaments_upcoming(
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
