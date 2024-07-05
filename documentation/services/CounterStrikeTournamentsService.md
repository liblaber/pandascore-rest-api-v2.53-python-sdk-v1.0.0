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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCsgoShortTournaments, RangeOverCsgoShortTournaments, SearchOverCsgoShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCsgoShortTournaments(
    begin_at=[
        "commodo"
    ],
    detailed_stats=False,
    end_at=[
        "deserunt cill"
    ],
    has_bracket=True,
    id_=[
        6
    ],
    live_supported=True,
    modified_at=[
        "Lorem"
    ],
    name=[
        "sint ad vol"
    ],
    prizepool=[
        "ea consequat "
    ],
    serie_id=[
        6
    ],
    slug=[
        "laiwl7lcb9"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        8
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCsgoShortTournaments(
    begin_at=[
        "enim eiusmod"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "incid"
    ],
    has_bracket=[
        False
    ],
    id_=[
        2
    ],
    modified_at=[
        "labo"
    ],
    name=[
        "adipisicing e"
    ],
    prizepool=[
        "enim nulla esse"
    ],
    serie_id=[
        6
    ],
    slug=[
        "a98eej9b1"
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
search=SearchOverCsgoShortTournaments(
    name="irure volup",
    prizepool="tempor mag",
    slug="906nbl9ncj7",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCsgoShortTournaments, RangeOverCsgoShortTournaments, SearchOverCsgoShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCsgoShortTournaments(
    begin_at=[
        "commodo"
    ],
    detailed_stats=False,
    end_at=[
        "deserunt cill"
    ],
    has_bracket=True,
    id_=[
        6
    ],
    live_supported=True,
    modified_at=[
        "Lorem"
    ],
    name=[
        "sint ad vol"
    ],
    prizepool=[
        "ea consequat "
    ],
    serie_id=[
        6
    ],
    slug=[
        "laiwl7lcb9"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        8
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCsgoShortTournaments(
    begin_at=[
        "enim eiusmod"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "incid"
    ],
    has_bracket=[
        False
    ],
    id_=[
        2
    ],
    modified_at=[
        "labo"
    ],
    name=[
        "adipisicing e"
    ],
    prizepool=[
        "enim nulla esse"
    ],
    serie_id=[
        6
    ],
    slug=[
        "a98eej9b1"
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
search=SearchOverCsgoShortTournaments(
    name="irure volup",
    prizepool="tempor mag",
    slug="906nbl9ncj7",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCsgoShortTournaments, RangeOverCsgoShortTournaments, SearchOverCsgoShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCsgoShortTournaments(
    begin_at=[
        "commodo"
    ],
    detailed_stats=False,
    end_at=[
        "deserunt cill"
    ],
    has_bracket=True,
    id_=[
        6
    ],
    live_supported=True,
    modified_at=[
        "Lorem"
    ],
    name=[
        "sint ad vol"
    ],
    prizepool=[
        "ea consequat "
    ],
    serie_id=[
        6
    ],
    slug=[
        "laiwl7lcb9"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        8
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCsgoShortTournaments(
    begin_at=[
        "enim eiusmod"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "incid"
    ],
    has_bracket=[
        False
    ],
    id_=[
        2
    ],
    modified_at=[
        "labo"
    ],
    name=[
        "adipisicing e"
    ],
    prizepool=[
        "enim nulla esse"
    ],
    serie_id=[
        6
    ],
    slug=[
        "a98eej9b1"
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
search=SearchOverCsgoShortTournaments(
    name="irure volup",
    prizepool="tempor mag",
    slug="906nbl9ncj7",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCsgoShortTournaments, RangeOverCsgoShortTournaments, SearchOverCsgoShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCsgoShortTournaments(
    begin_at=[
        "commodo"
    ],
    detailed_stats=False,
    end_at=[
        "deserunt cill"
    ],
    has_bracket=True,
    id_=[
        6
    ],
    live_supported=True,
    modified_at=[
        "Lorem"
    ],
    name=[
        "sint ad vol"
    ],
    prizepool=[
        "ea consequat "
    ],
    serie_id=[
        6
    ],
    slug=[
        "laiwl7lcb9"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        8
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCsgoShortTournaments(
    begin_at=[
        "enim eiusmod"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "incid"
    ],
    has_bracket=[
        False
    ],
    id_=[
        2
    ],
    modified_at=[
        "labo"
    ],
    name=[
        "adipisicing e"
    ],
    prizepool=[
        "enim nulla esse"
    ],
    serie_id=[
        6
    ],
    slug=[
        "a98eej9b1"
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
search=SearchOverCsgoShortTournaments(
    name="irure volup",
    prizepool="tempor mag",
    slug="906nbl9ncj7",
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
