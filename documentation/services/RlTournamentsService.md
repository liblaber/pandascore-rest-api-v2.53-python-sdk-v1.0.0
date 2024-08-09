# RlTournamentsService

A list of all methods in the `RlTournamentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description                                      |
| :---------------------------------------------------------- | :----------------------------------------------- |
| [get_rl_tournaments](#get_rl_tournaments)                   | List tournaments for the Rocket League videogame |
| [get_rl_tournaments_past](#get_rl_tournaments_past)         | List past Rocket League tournaments              |
| [get_rl_tournaments_running](#get_rl_tournaments_running)   | List running Rocket League tournaments           |
| [get_rl_tournaments_upcoming](#get_rl_tournaments_upcoming) | List upcoming Rocket League tournaments          |

## get_rl_tournaments

List tournaments for the Rocket League videogame

- HTTP Method: `GET`
- Endpoint: `/rl/tournaments`

**Parameters**

| Name     | Type                                                                      | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverRlShortTournaments](../models/FilterOverRlShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverRlShortTournaments](../models/RangeOverRlShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverRlShortTournaments](../models/SearchOverRlShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverRlShortTournaments, RangeOverRlShortTournaments, SearchOverRlShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverRlShortTournaments(
    begin_at=[
        "proi"
    ],
    detailed_stats=True,
    end_at=[
        "Duis c"
    ],
    has_bracket=False,
    id_=[
        8
    ],
    live_supported=True,
    modified_at=[
        "ad a"
    ],
    name=[
        "et officia"
    ],
    prizepool=[
        "aliqua fugiat"
    ],
    serie_id=[
        8
    ],
    slug=[
        "l0"
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
range=RangeOverRlShortTournaments(
    begin_at=[
        "ea in"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "eiusmod"
    ],
    has_bracket=[
        False
    ],
    id_=[
        3
    ],
    modified_at=[
        "fugiat la"
    ],
    name=[
        "quis sit "
    ],
    prizepool=[
        "autelaborum "
    ],
    serie_id=[
        1
    ],
    slug=[
        "yozf-78_3ou"
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
search=SearchOverRlShortTournaments(
    name="eiusmod anim",
    prizepool="culpa ani",
    slug="q",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.rl_tournaments.get_rl_tournaments(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_rl_tournaments_past

List past Rocket League tournaments

- HTTP Method: `GET`
- Endpoint: `/rl/tournaments/past`

**Parameters**

| Name     | Type                                                                      | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverRlShortTournaments](../models/FilterOverRlShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverRlShortTournaments](../models/RangeOverRlShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverRlShortTournaments](../models/SearchOverRlShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverRlShortTournaments, RangeOverRlShortTournaments, SearchOverRlShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverRlShortTournaments(
    begin_at=[
        "proi"
    ],
    detailed_stats=True,
    end_at=[
        "Duis c"
    ],
    has_bracket=False,
    id_=[
        8
    ],
    live_supported=True,
    modified_at=[
        "ad a"
    ],
    name=[
        "et officia"
    ],
    prizepool=[
        "aliqua fugiat"
    ],
    serie_id=[
        8
    ],
    slug=[
        "l0"
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
range=RangeOverRlShortTournaments(
    begin_at=[
        "ea in"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "eiusmod"
    ],
    has_bracket=[
        False
    ],
    id_=[
        3
    ],
    modified_at=[
        "fugiat la"
    ],
    name=[
        "quis sit "
    ],
    prizepool=[
        "autelaborum "
    ],
    serie_id=[
        1
    ],
    slug=[
        "yozf-78_3ou"
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
search=SearchOverRlShortTournaments(
    name="eiusmod anim",
    prizepool="culpa ani",
    slug="q",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.rl_tournaments.get_rl_tournaments_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_rl_tournaments_running

List running Rocket League tournaments

- HTTP Method: `GET`
- Endpoint: `/rl/tournaments/running`

**Parameters**

| Name     | Type                                                                      | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverRlShortTournaments](../models/FilterOverRlShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverRlShortTournaments](../models/RangeOverRlShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverRlShortTournaments](../models/SearchOverRlShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverRlShortTournaments, RangeOverRlShortTournaments, SearchOverRlShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverRlShortTournaments(
    begin_at=[
        "proi"
    ],
    detailed_stats=True,
    end_at=[
        "Duis c"
    ],
    has_bracket=False,
    id_=[
        8
    ],
    live_supported=True,
    modified_at=[
        "ad a"
    ],
    name=[
        "et officia"
    ],
    prizepool=[
        "aliqua fugiat"
    ],
    serie_id=[
        8
    ],
    slug=[
        "l0"
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
range=RangeOverRlShortTournaments(
    begin_at=[
        "ea in"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "eiusmod"
    ],
    has_bracket=[
        False
    ],
    id_=[
        3
    ],
    modified_at=[
        "fugiat la"
    ],
    name=[
        "quis sit "
    ],
    prizepool=[
        "autelaborum "
    ],
    serie_id=[
        1
    ],
    slug=[
        "yozf-78_3ou"
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
search=SearchOverRlShortTournaments(
    name="eiusmod anim",
    prizepool="culpa ani",
    slug="q",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.rl_tournaments.get_rl_tournaments_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_rl_tournaments_upcoming

List upcoming Rocket League tournaments

- HTTP Method: `GET`
- Endpoint: `/rl/tournaments/upcoming`

**Parameters**

| Name     | Type                                                                      | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverRlShortTournaments](../models/FilterOverRlShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverRlShortTournaments](../models/RangeOverRlShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverRlShortTournaments](../models/SearchOverRlShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverRlShortTournaments, RangeOverRlShortTournaments, SearchOverRlShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverRlShortTournaments(
    begin_at=[
        "proi"
    ],
    detailed_stats=True,
    end_at=[
        "Duis c"
    ],
    has_bracket=False,
    id_=[
        8
    ],
    live_supported=True,
    modified_at=[
        "ad a"
    ],
    name=[
        "et officia"
    ],
    prizepool=[
        "aliqua fugiat"
    ],
    serie_id=[
        8
    ],
    slug=[
        "l0"
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
range=RangeOverRlShortTournaments(
    begin_at=[
        "ea in"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "eiusmod"
    ],
    has_bracket=[
        False
    ],
    id_=[
        3
    ],
    modified_at=[
        "fugiat la"
    ],
    name=[
        "quis sit "
    ],
    prizepool=[
        "autelaborum "
    ],
    serie_id=[
        1
    ],
    slug=[
        "yozf-78_3ou"
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
search=SearchOverRlShortTournaments(
    name="eiusmod anim",
    prizepool="culpa ani",
    slug="q",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.rl_tournaments.get_rl_tournaments_upcoming(
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
