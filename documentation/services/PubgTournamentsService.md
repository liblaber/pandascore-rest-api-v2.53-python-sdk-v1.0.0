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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverPubgShortTournaments, RangeOverPubgShortTournaments, SearchOverPubgShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverPubgShortTournaments(
    begin_at=[
        "velit ad"
    ],
    detailed_stats=True,
    end_at=[
        "aute"
    ],
    has_bracket=True,
    id_=[
        2
    ],
    live_supported=False,
    modified_at=[
        "commodo Duis"
    ],
    name=[
        "ipsum in"
    ],
    prizepool=[
        "dolor"
    ],
    serie_id=[
        2
    ],
    slug=[
        "3yb3sgap"
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
range=RangeOverPubgShortTournaments(
    begin_at=[
        "exercitat"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "eni"
    ],
    has_bracket=[
        False
    ],
    id_=[
        9
    ],
    modified_at=[
        "mini"
    ],
    name=[
        "non cupidata"
    ],
    prizepool=[
        "voluptate"
    ],
    serie_id=[
        10
    ],
    slug=[
        "3u"
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
search=SearchOverPubgShortTournaments(
    name="esseproiden",
    prizepool="proident ",
    slug="9qflxpoj",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverPubgShortTournaments, RangeOverPubgShortTournaments, SearchOverPubgShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverPubgShortTournaments(
    begin_at=[
        "velit ad"
    ],
    detailed_stats=True,
    end_at=[
        "aute"
    ],
    has_bracket=True,
    id_=[
        2
    ],
    live_supported=False,
    modified_at=[
        "commodo Duis"
    ],
    name=[
        "ipsum in"
    ],
    prizepool=[
        "dolor"
    ],
    serie_id=[
        2
    ],
    slug=[
        "3yb3sgap"
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
range=RangeOverPubgShortTournaments(
    begin_at=[
        "exercitat"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "eni"
    ],
    has_bracket=[
        False
    ],
    id_=[
        9
    ],
    modified_at=[
        "mini"
    ],
    name=[
        "non cupidata"
    ],
    prizepool=[
        "voluptate"
    ],
    serie_id=[
        10
    ],
    slug=[
        "3u"
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
search=SearchOverPubgShortTournaments(
    name="esseproiden",
    prizepool="proident ",
    slug="9qflxpoj",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverPubgShortTournaments, RangeOverPubgShortTournaments, SearchOverPubgShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverPubgShortTournaments(
    begin_at=[
        "velit ad"
    ],
    detailed_stats=True,
    end_at=[
        "aute"
    ],
    has_bracket=True,
    id_=[
        2
    ],
    live_supported=False,
    modified_at=[
        "commodo Duis"
    ],
    name=[
        "ipsum in"
    ],
    prizepool=[
        "dolor"
    ],
    serie_id=[
        2
    ],
    slug=[
        "3yb3sgap"
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
range=RangeOverPubgShortTournaments(
    begin_at=[
        "exercitat"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "eni"
    ],
    has_bracket=[
        False
    ],
    id_=[
        9
    ],
    modified_at=[
        "mini"
    ],
    name=[
        "non cupidata"
    ],
    prizepool=[
        "voluptate"
    ],
    serie_id=[
        10
    ],
    slug=[
        "3u"
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
search=SearchOverPubgShortTournaments(
    name="esseproiden",
    prizepool="proident ",
    slug="9qflxpoj",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverPubgShortTournaments, RangeOverPubgShortTournaments, SearchOverPubgShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverPubgShortTournaments(
    begin_at=[
        "velit ad"
    ],
    detailed_stats=True,
    end_at=[
        "aute"
    ],
    has_bracket=True,
    id_=[
        2
    ],
    live_supported=False,
    modified_at=[
        "commodo Duis"
    ],
    name=[
        "ipsum in"
    ],
    prizepool=[
        "dolor"
    ],
    serie_id=[
        2
    ],
    slug=[
        "3yb3sgap"
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
range=RangeOverPubgShortTournaments(
    begin_at=[
        "exercitat"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "eni"
    ],
    has_bracket=[
        False
    ],
    id_=[
        9
    ],
    modified_at=[
        "mini"
    ],
    name=[
        "non cupidata"
    ],
    prizepool=[
        "voluptate"
    ],
    serie_id=[
        10
    ],
    slug=[
        "3u"
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
search=SearchOverPubgShortTournaments(
    name="esseproiden",
    prizepool="proident ",
    slug="9qflxpoj",
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

<!-- This file was generated by liblab | https://liblab.com/ -->
