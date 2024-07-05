# PubgTournamentsService

A list of all methods in the `PubgTournamentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                         | Description                             |
| :-------------------------------------------------------------- | :-------------------------------------- |
| [get_pubg_tournaments](#get_pubg_tournaments)                   | List tournaments for the PUBG videogame |
| [get_pubg_tournaments_past](#get_pubg_tournaments_past)         | List past PUBG tournaments              |
| [get_pubg_tournaments_running](#get_pubg_tournaments_running)   | List running PUBG tournaments           |
| [get_pubg_tournaments_upcoming](#get_pubg_tournaments_upcoming) | List upcoming PUBG tournaments          |

## get_pubg_tournaments

List tournaments for the PUBG videogame

- HTTP Method: `GET`
- Endpoint: `/pubg/tournaments`

**Parameters**

| Name     | Type                                                                          | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverPubgShortTournaments](../models/FilterOverPubgShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverPubgShortTournaments](../models/RangeOverPubgShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverPubgShortTournaments](../models/SearchOverPubgShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverPubgShortTournaments, RangeOverPubgShortTournaments, SearchOverPubgShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverPubgShortTournaments(
    begin_at=[
        "au"
    ],
    detailed_stats=True,
    end_at=[
        "ut proident"
    ],
    has_bracket=True,
    id_=[
        2
    ],
    live_supported=False,
    modified_at=[
        "dolo"
    ],
    name=[
        "pariat"
    ],
    prizepool=[
        "id deseru"
    ],
    serie_id=[
        2
    ],
    slug=[
        "s3viqi"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        4
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverPubgShortTournaments(
    begin_at=[
        "consecte"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "veniam dolor"
    ],
    has_bracket=[
        True
    ],
    id_=[
        10
    ],
    modified_at=[
        "aliqua in"
    ],
    name=[
        "aute nostrud ni"
    ],
    prizepool=[
        "officia"
    ],
    serie_id=[
        7
    ],
    slug=[
        "88"
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
search=SearchOverPubgShortTournaments(
    name="enim mini",
    prizepool="dolore",
    slug="1",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.pubg_tournaments.get_pubg_tournaments(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_pubg_tournaments_past

List past PUBG tournaments

- HTTP Method: `GET`
- Endpoint: `/pubg/tournaments/past`

**Parameters**

| Name     | Type                                                                          | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverPubgShortTournaments](../models/FilterOverPubgShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverPubgShortTournaments](../models/RangeOverPubgShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverPubgShortTournaments](../models/SearchOverPubgShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverPubgShortTournaments, RangeOverPubgShortTournaments, SearchOverPubgShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverPubgShortTournaments(
    begin_at=[
        "au"
    ],
    detailed_stats=True,
    end_at=[
        "ut proident"
    ],
    has_bracket=True,
    id_=[
        2
    ],
    live_supported=False,
    modified_at=[
        "dolo"
    ],
    name=[
        "pariat"
    ],
    prizepool=[
        "id deseru"
    ],
    serie_id=[
        2
    ],
    slug=[
        "s3viqi"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        4
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverPubgShortTournaments(
    begin_at=[
        "consecte"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "veniam dolor"
    ],
    has_bracket=[
        True
    ],
    id_=[
        10
    ],
    modified_at=[
        "aliqua in"
    ],
    name=[
        "aute nostrud ni"
    ],
    prizepool=[
        "officia"
    ],
    serie_id=[
        7
    ],
    slug=[
        "88"
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
search=SearchOverPubgShortTournaments(
    name="enim mini",
    prizepool="dolore",
    slug="1",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.pubg_tournaments.get_pubg_tournaments_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_pubg_tournaments_running

List running PUBG tournaments

- HTTP Method: `GET`
- Endpoint: `/pubg/tournaments/running`

**Parameters**

| Name     | Type                                                                          | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverPubgShortTournaments](../models/FilterOverPubgShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverPubgShortTournaments](../models/RangeOverPubgShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverPubgShortTournaments](../models/SearchOverPubgShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverPubgShortTournaments, RangeOverPubgShortTournaments, SearchOverPubgShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverPubgShortTournaments(
    begin_at=[
        "au"
    ],
    detailed_stats=True,
    end_at=[
        "ut proident"
    ],
    has_bracket=True,
    id_=[
        2
    ],
    live_supported=False,
    modified_at=[
        "dolo"
    ],
    name=[
        "pariat"
    ],
    prizepool=[
        "id deseru"
    ],
    serie_id=[
        2
    ],
    slug=[
        "s3viqi"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        4
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverPubgShortTournaments(
    begin_at=[
        "consecte"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "veniam dolor"
    ],
    has_bracket=[
        True
    ],
    id_=[
        10
    ],
    modified_at=[
        "aliqua in"
    ],
    name=[
        "aute nostrud ni"
    ],
    prizepool=[
        "officia"
    ],
    serie_id=[
        7
    ],
    slug=[
        "88"
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
search=SearchOverPubgShortTournaments(
    name="enim mini",
    prizepool="dolore",
    slug="1",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.pubg_tournaments.get_pubg_tournaments_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_pubg_tournaments_upcoming

List upcoming PUBG tournaments

- HTTP Method: `GET`
- Endpoint: `/pubg/tournaments/upcoming`

**Parameters**

| Name     | Type                                                                          | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverPubgShortTournaments](../models/FilterOverPubgShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverPubgShortTournaments](../models/RangeOverPubgShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverPubgShortTournaments](../models/SearchOverPubgShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverPubgShortTournaments, RangeOverPubgShortTournaments, SearchOverPubgShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverPubgShortTournaments(
    begin_at=[
        "au"
    ],
    detailed_stats=True,
    end_at=[
        "ut proident"
    ],
    has_bracket=True,
    id_=[
        2
    ],
    live_supported=False,
    modified_at=[
        "dolo"
    ],
    name=[
        "pariat"
    ],
    prizepool=[
        "id deseru"
    ],
    serie_id=[
        2
    ],
    slug=[
        "s3viqi"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        4
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverPubgShortTournaments(
    begin_at=[
        "consecte"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "veniam dolor"
    ],
    has_bracket=[
        True
    ],
    id_=[
        10
    ],
    modified_at=[
        "aliqua in"
    ],
    name=[
        "aute nostrud ni"
    ],
    prizepool=[
        "officia"
    ],
    serie_id=[
        7
    ],
    slug=[
        "88"
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
search=SearchOverPubgShortTournaments(
    name="enim mini",
    prizepool="dolore",
    slug="1",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.pubg_tournaments.get_pubg_tournaments_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
