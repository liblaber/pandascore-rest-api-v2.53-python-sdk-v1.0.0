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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverDota2ShortTournaments, RangeOverDota2ShortTournaments, SearchOverDota2ShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverDota2ShortTournaments(
    begin_at=[
        "aliq"
    ],
    detailed_stats=True,
    end_at=[
        "a"
    ],
    has_bracket=False,
    id_=[
        9
    ],
    live_supported=True,
    modified_at=[
        "i"
    ],
    name=[
        "velit"
    ],
    prizepool=[
        "in dolore cupi"
    ],
    serie_id=[
        2
    ],
    slug=[
        "sminlpoh"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        9
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverDota2ShortTournaments(
    begin_at=[
        "amet ea"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "enim cillum ips"
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "si"
    ],
    name=[
        "ad nostr"
    ],
    prizepool=[
        "id laborum e"
    ],
    serie_id=[
        10
    ],
    slug=[
        "wrr2qymw"
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
search=SearchOverDota2ShortTournaments(
    name="magna",
    prizepool="magna",
    slug="oxs3j6",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverDota2ShortTournaments, RangeOverDota2ShortTournaments, SearchOverDota2ShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverDota2ShortTournaments(
    begin_at=[
        "aliq"
    ],
    detailed_stats=True,
    end_at=[
        "a"
    ],
    has_bracket=False,
    id_=[
        9
    ],
    live_supported=True,
    modified_at=[
        "i"
    ],
    name=[
        "velit"
    ],
    prizepool=[
        "in dolore cupi"
    ],
    serie_id=[
        2
    ],
    slug=[
        "sminlpoh"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        9
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverDota2ShortTournaments(
    begin_at=[
        "amet ea"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "enim cillum ips"
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "si"
    ],
    name=[
        "ad nostr"
    ],
    prizepool=[
        "id laborum e"
    ],
    serie_id=[
        10
    ],
    slug=[
        "wrr2qymw"
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
search=SearchOverDota2ShortTournaments(
    name="magna",
    prizepool="magna",
    slug="oxs3j6",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverDota2ShortTournaments, RangeOverDota2ShortTournaments, SearchOverDota2ShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverDota2ShortTournaments(
    begin_at=[
        "aliq"
    ],
    detailed_stats=True,
    end_at=[
        "a"
    ],
    has_bracket=False,
    id_=[
        9
    ],
    live_supported=True,
    modified_at=[
        "i"
    ],
    name=[
        "velit"
    ],
    prizepool=[
        "in dolore cupi"
    ],
    serie_id=[
        2
    ],
    slug=[
        "sminlpoh"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        9
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverDota2ShortTournaments(
    begin_at=[
        "amet ea"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "enim cillum ips"
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "si"
    ],
    name=[
        "ad nostr"
    ],
    prizepool=[
        "id laborum e"
    ],
    serie_id=[
        10
    ],
    slug=[
        "wrr2qymw"
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
search=SearchOverDota2ShortTournaments(
    name="magna",
    prizepool="magna",
    slug="oxs3j6",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverDota2ShortTournaments, RangeOverDota2ShortTournaments, SearchOverDota2ShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverDota2ShortTournaments(
    begin_at=[
        "aliq"
    ],
    detailed_stats=True,
    end_at=[
        "a"
    ],
    has_bracket=False,
    id_=[
        9
    ],
    live_supported=True,
    modified_at=[
        "i"
    ],
    name=[
        "velit"
    ],
    prizepool=[
        "in dolore cupi"
    ],
    serie_id=[
        2
    ],
    slug=[
        "sminlpoh"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        9
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverDota2ShortTournaments(
    begin_at=[
        "amet ea"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "enim cillum ips"
    ],
    has_bracket=[
        True
    ],
    id_=[
        3
    ],
    modified_at=[
        "si"
    ],
    name=[
        "ad nostr"
    ],
    prizepool=[
        "id laborum e"
    ],
    serie_id=[
        10
    ],
    slug=[
        "wrr2qymw"
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
search=SearchOverDota2ShortTournaments(
    name="magna",
    prizepool="magna",
    slug="oxs3j6",
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
