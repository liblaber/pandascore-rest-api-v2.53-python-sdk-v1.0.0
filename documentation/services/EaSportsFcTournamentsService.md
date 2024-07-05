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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverFifaShortTournaments, RangeOverFifaShortTournaments, SearchOverFifaShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverFifaShortTournaments(
    begin_at=[
        "quis id paria"
    ],
    detailed_stats=False,
    end_at=[
        "irure"
    ],
    has_bracket=True,
    id_=[
        5
    ],
    live_supported=True,
    modified_at=[
        "sint mollit ir"
    ],
    name=[
        "qui e"
    ],
    prizepool=[
        "sunt "
    ],
    serie_id=[
        7
    ],
    slug=[
        "08-0h3xaa"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        6
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverFifaShortTournaments(
    begin_at=[
        "in"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "laboris dolore "
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "dolo"
    ],
    name=[
        "ut ullam"
    ],
    prizepool=[
        "ea fugia"
    ],
    serie_id=[
        1
    ],
    slug=[
        "id"
    ],
    tier=[
        "a"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverFifaShortTournaments(
    name="voluptate am",
    prizepool="do adipisicing ",
    slug="x_6l",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverFifaShortTournaments, RangeOverFifaShortTournaments, SearchOverFifaShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverFifaShortTournaments(
    begin_at=[
        "quis id paria"
    ],
    detailed_stats=False,
    end_at=[
        "irure"
    ],
    has_bracket=True,
    id_=[
        5
    ],
    live_supported=True,
    modified_at=[
        "sint mollit ir"
    ],
    name=[
        "qui e"
    ],
    prizepool=[
        "sunt "
    ],
    serie_id=[
        7
    ],
    slug=[
        "08-0h3xaa"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        6
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverFifaShortTournaments(
    begin_at=[
        "in"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "laboris dolore "
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "dolo"
    ],
    name=[
        "ut ullam"
    ],
    prizepool=[
        "ea fugia"
    ],
    serie_id=[
        1
    ],
    slug=[
        "id"
    ],
    tier=[
        "a"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverFifaShortTournaments(
    name="voluptate am",
    prizepool="do adipisicing ",
    slug="x_6l",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverFifaShortTournaments, RangeOverFifaShortTournaments, SearchOverFifaShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverFifaShortTournaments(
    begin_at=[
        "quis id paria"
    ],
    detailed_stats=False,
    end_at=[
        "irure"
    ],
    has_bracket=True,
    id_=[
        5
    ],
    live_supported=True,
    modified_at=[
        "sint mollit ir"
    ],
    name=[
        "qui e"
    ],
    prizepool=[
        "sunt "
    ],
    serie_id=[
        7
    ],
    slug=[
        "08-0h3xaa"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        6
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverFifaShortTournaments(
    begin_at=[
        "in"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "laboris dolore "
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "dolo"
    ],
    name=[
        "ut ullam"
    ],
    prizepool=[
        "ea fugia"
    ],
    serie_id=[
        1
    ],
    slug=[
        "id"
    ],
    tier=[
        "a"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverFifaShortTournaments(
    name="voluptate am",
    prizepool="do adipisicing ",
    slug="x_6l",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverFifaShortTournaments, RangeOverFifaShortTournaments, SearchOverFifaShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverFifaShortTournaments(
    begin_at=[
        "quis id paria"
    ],
    detailed_stats=False,
    end_at=[
        "irure"
    ],
    has_bracket=True,
    id_=[
        5
    ],
    live_supported=True,
    modified_at=[
        "sint mollit ir"
    ],
    name=[
        "qui e"
    ],
    prizepool=[
        "sunt "
    ],
    serie_id=[
        7
    ],
    slug=[
        "08-0h3xaa"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        6
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverFifaShortTournaments(
    begin_at=[
        "in"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "laboris dolore "
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "dolo"
    ],
    name=[
        "ut ullam"
    ],
    prizepool=[
        "ea fugia"
    ],
    serie_id=[
        1
    ],
    slug=[
        "id"
    ],
    tier=[
        "a"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverFifaShortTournaments(
    name="voluptate am",
    prizepool="do adipisicing ",
    slug="x_6l",
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
