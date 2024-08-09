# EaSportsFcTournamentsService

A list of all methods in the `EaSportsFcTournamentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                         | Description                                     |
| :-------------------------------------------------------------- | :---------------------------------------------- |
| [get_fifa_tournaments](#get_fifa_tournaments)                   | List tournaments for the EA Sports FC videogame |
| [get_fifa_tournaments_past](#get_fifa_tournaments_past)         | List past EA Sports FC tournaments              |
| [get_fifa_tournaments_running](#get_fifa_tournaments_running)   | List running EA Sports FC tournaments           |
| [get_fifa_tournaments_upcoming](#get_fifa_tournaments_upcoming) | List upcoming EA Sports FC tournaments          |

## get_fifa_tournaments

List tournaments for the EA Sports FC videogame

- HTTP Method: `GET`
- Endpoint: `/fifa/tournaments`

**Parameters**

| Name     | Type                                                                          | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverFifaShortTournaments](../models/FilterOverFifaShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverFifaShortTournaments](../models/RangeOverFifaShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverFifaShortTournaments](../models/SearchOverFifaShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverFifaShortTournaments, RangeOverFifaShortTournaments, SearchOverFifaShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverFifaShortTournaments(
    begin_at=[
        "cillum "
    ],
    detailed_stats=True,
    end_at=[
        "ad ullam"
    ],
    has_bracket=False,
    id_=[
        9
    ],
    live_supported=True,
    modified_at=[
        "s"
    ],
    name=[
        "nulla"
    ],
    prizepool=[
        "enim veniam"
    ],
    serie_id=[
        6
    ],
    slug=[
        "-kk"
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
range=RangeOverFifaShortTournaments(
    begin_at=[
        "tempor "
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "d"
    ],
    has_bracket=[
        True
    ],
    id_=[
        9
    ],
    modified_at=[
        "cillum Dui"
    ],
    name=[
        "veniam"
    ],
    prizepool=[
        "officia cons"
    ],
    serie_id=[
        1
    ],
    slug=[
        "3j"
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
search=SearchOverFifaShortTournaments(
    name="proident",
    prizepool="exaliq",
    slug="bffn",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.ea_sports_fc_tournaments.get_fifa_tournaments(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_fifa_tournaments_past

List past EA Sports FC tournaments

- HTTP Method: `GET`
- Endpoint: `/fifa/tournaments/past`

**Parameters**

| Name     | Type                                                                          | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverFifaShortTournaments](../models/FilterOverFifaShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverFifaShortTournaments](../models/RangeOverFifaShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverFifaShortTournaments](../models/SearchOverFifaShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverFifaShortTournaments, RangeOverFifaShortTournaments, SearchOverFifaShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverFifaShortTournaments(
    begin_at=[
        "cillum "
    ],
    detailed_stats=True,
    end_at=[
        "ad ullam"
    ],
    has_bracket=False,
    id_=[
        9
    ],
    live_supported=True,
    modified_at=[
        "s"
    ],
    name=[
        "nulla"
    ],
    prizepool=[
        "enim veniam"
    ],
    serie_id=[
        6
    ],
    slug=[
        "-kk"
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
range=RangeOverFifaShortTournaments(
    begin_at=[
        "tempor "
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "d"
    ],
    has_bracket=[
        True
    ],
    id_=[
        9
    ],
    modified_at=[
        "cillum Dui"
    ],
    name=[
        "veniam"
    ],
    prizepool=[
        "officia cons"
    ],
    serie_id=[
        1
    ],
    slug=[
        "3j"
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
search=SearchOverFifaShortTournaments(
    name="proident",
    prizepool="exaliq",
    slug="bffn",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.ea_sports_fc_tournaments.get_fifa_tournaments_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_fifa_tournaments_running

List running EA Sports FC tournaments

- HTTP Method: `GET`
- Endpoint: `/fifa/tournaments/running`

**Parameters**

| Name     | Type                                                                          | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverFifaShortTournaments](../models/FilterOverFifaShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverFifaShortTournaments](../models/RangeOverFifaShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverFifaShortTournaments](../models/SearchOverFifaShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverFifaShortTournaments, RangeOverFifaShortTournaments, SearchOverFifaShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverFifaShortTournaments(
    begin_at=[
        "cillum "
    ],
    detailed_stats=True,
    end_at=[
        "ad ullam"
    ],
    has_bracket=False,
    id_=[
        9
    ],
    live_supported=True,
    modified_at=[
        "s"
    ],
    name=[
        "nulla"
    ],
    prizepool=[
        "enim veniam"
    ],
    serie_id=[
        6
    ],
    slug=[
        "-kk"
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
range=RangeOverFifaShortTournaments(
    begin_at=[
        "tempor "
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "d"
    ],
    has_bracket=[
        True
    ],
    id_=[
        9
    ],
    modified_at=[
        "cillum Dui"
    ],
    name=[
        "veniam"
    ],
    prizepool=[
        "officia cons"
    ],
    serie_id=[
        1
    ],
    slug=[
        "3j"
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
search=SearchOverFifaShortTournaments(
    name="proident",
    prizepool="exaliq",
    slug="bffn",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.ea_sports_fc_tournaments.get_fifa_tournaments_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_fifa_tournaments_upcoming

List upcoming EA Sports FC tournaments

- HTTP Method: `GET`
- Endpoint: `/fifa/tournaments/upcoming`

**Parameters**

| Name     | Type                                                                          | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverFifaShortTournaments](../models/FilterOverFifaShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverFifaShortTournaments](../models/RangeOverFifaShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverFifaShortTournaments](../models/SearchOverFifaShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverFifaShortTournaments, RangeOverFifaShortTournaments, SearchOverFifaShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverFifaShortTournaments(
    begin_at=[
        "cillum "
    ],
    detailed_stats=True,
    end_at=[
        "ad ullam"
    ],
    has_bracket=False,
    id_=[
        9
    ],
    live_supported=True,
    modified_at=[
        "s"
    ],
    name=[
        "nulla"
    ],
    prizepool=[
        "enim veniam"
    ],
    serie_id=[
        6
    ],
    slug=[
        "-kk"
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
range=RangeOverFifaShortTournaments(
    begin_at=[
        "tempor "
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "d"
    ],
    has_bracket=[
        True
    ],
    id_=[
        9
    ],
    modified_at=[
        "cillum Dui"
    ],
    name=[
        "veniam"
    ],
    prizepool=[
        "officia cons"
    ],
    serie_id=[
        1
    ],
    slug=[
        "3j"
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
search=SearchOverFifaShortTournaments(
    name="proident",
    prizepool="exaliq",
    slug="bffn",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.ea_sports_fc_tournaments.get_fifa_tournaments_upcoming(
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
