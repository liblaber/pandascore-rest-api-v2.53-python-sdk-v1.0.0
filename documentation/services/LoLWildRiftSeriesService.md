# LoLWildRiftSeriesService

A list of all methods in the `LoLWildRiftSeriesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                                 |
| :---------------------------------------------------------------------- | :------------------------------------------ |
| [get_lol_wild_rift_series](#get_lol_wild_rift_series)                   | List series for the LoL Wild Rift videogame |
| [get_lol_wild_rift_series_past](#get_lol_wild_rift_series_past)         | List past LoL Wild Rift series              |
| [get_lol_wild_rift_series_running](#get_lol_wild_rift_series_running)   | List running LoL Wild Rift series           |
| [get_lol_wild_rift_series_upcoming](#get_lol_wild_rift_series_upcoming) | List upcoming LoL Wild Rift series          |

## get_lol_wild_rift_series

List series for the LoL Wild Rift videogame

- HTTP Method: `GET`
- Endpoint: `/lol-wild-rift/series`

**Parameters**

| Name     | Type                                                                    | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLolWildRiftSeries](../models/FilterOverLolWildRiftSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLolWildRiftSeries](../models/RangeOverLolWildRiftSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLolWildRiftSeries](../models/SearchOverLolWildRiftSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLolWildRiftSeries, RangeOverLolWildRiftSeries, SearchOverLolWildRiftSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLolWildRiftSeries(
    begin_at=[
        "labo"
    ],
    end_at=[
        "co"
    ],
    id_=[
        5
    ],
    league_id=[
        2
    ],
    modified_at=[
        "in labor"
    ],
    name=[
        "velit"
    ],
    season=[
        "fugiat "
    ],
    slug=[
        "hph-bv"
    ],
    videogame_title=[
        3
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ],
    year=[
        None
    ]
)
range=RangeOverLolWildRiftSeries(
    begin_at=[
        "ex"
    ],
    end_at=[
        "ad qui aut"
    ],
    id_=[
        3
    ],
    league_id=[
        5
    ],
    modified_at=[
        "ma"
    ],
    name=[
        "ut de"
    ],
    season=[
        "nostr"
    ],
    slug=[
        "6os7g3o0bh7"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ],
    year=[
        None
    ]
)
sort=[
    ""
]
search=SearchOverLolWildRiftSeries(
    name="ea nulla proi",
    season="culpa pariat",
    slug="_tw34do",
    winner_type="Player"
)
page=1

result = sdk.lo_l_wild_rift_series.get_lol_wild_rift_series(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_wild_rift_series_past

List past LoL Wild Rift series

- HTTP Method: `GET`
- Endpoint: `/lol-wild-rift/series/past`

**Parameters**

| Name     | Type                                                                    | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLolWildRiftSeries](../models/FilterOverLolWildRiftSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLolWildRiftSeries](../models/RangeOverLolWildRiftSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLolWildRiftSeries](../models/SearchOverLolWildRiftSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLolWildRiftSeries, RangeOverLolWildRiftSeries, SearchOverLolWildRiftSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLolWildRiftSeries(
    begin_at=[
        "labo"
    ],
    end_at=[
        "co"
    ],
    id_=[
        5
    ],
    league_id=[
        2
    ],
    modified_at=[
        "in labor"
    ],
    name=[
        "velit"
    ],
    season=[
        "fugiat "
    ],
    slug=[
        "hph-bv"
    ],
    videogame_title=[
        3
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ],
    year=[
        None
    ]
)
range=RangeOverLolWildRiftSeries(
    begin_at=[
        "ex"
    ],
    end_at=[
        "ad qui aut"
    ],
    id_=[
        3
    ],
    league_id=[
        5
    ],
    modified_at=[
        "ma"
    ],
    name=[
        "ut de"
    ],
    season=[
        "nostr"
    ],
    slug=[
        "6os7g3o0bh7"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ],
    year=[
        None
    ]
)
sort=[
    ""
]
search=SearchOverLolWildRiftSeries(
    name="ea nulla proi",
    season="culpa pariat",
    slug="_tw34do",
    winner_type="Player"
)
page=1

result = sdk.lo_l_wild_rift_series.get_lol_wild_rift_series_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_wild_rift_series_running

List running LoL Wild Rift series

- HTTP Method: `GET`
- Endpoint: `/lol-wild-rift/series/running`

**Parameters**

| Name     | Type                                                                    | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLolWildRiftSeries](../models/FilterOverLolWildRiftSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLolWildRiftSeries](../models/RangeOverLolWildRiftSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLolWildRiftSeries](../models/SearchOverLolWildRiftSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLolWildRiftSeries, RangeOverLolWildRiftSeries, SearchOverLolWildRiftSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLolWildRiftSeries(
    begin_at=[
        "labo"
    ],
    end_at=[
        "co"
    ],
    id_=[
        5
    ],
    league_id=[
        2
    ],
    modified_at=[
        "in labor"
    ],
    name=[
        "velit"
    ],
    season=[
        "fugiat "
    ],
    slug=[
        "hph-bv"
    ],
    videogame_title=[
        3
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ],
    year=[
        None
    ]
)
range=RangeOverLolWildRiftSeries(
    begin_at=[
        "ex"
    ],
    end_at=[
        "ad qui aut"
    ],
    id_=[
        3
    ],
    league_id=[
        5
    ],
    modified_at=[
        "ma"
    ],
    name=[
        "ut de"
    ],
    season=[
        "nostr"
    ],
    slug=[
        "6os7g3o0bh7"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ],
    year=[
        None
    ]
)
sort=[
    ""
]
search=SearchOverLolWildRiftSeries(
    name="ea nulla proi",
    season="culpa pariat",
    slug="_tw34do",
    winner_type="Player"
)
page=1

result = sdk.lo_l_wild_rift_series.get_lol_wild_rift_series_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_wild_rift_series_upcoming

List upcoming LoL Wild Rift series

- HTTP Method: `GET`
- Endpoint: `/lol-wild-rift/series/upcoming`

**Parameters**

| Name     | Type                                                                    | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLolWildRiftSeries](../models/FilterOverLolWildRiftSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLolWildRiftSeries](../models/RangeOverLolWildRiftSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLolWildRiftSeries](../models/SearchOverLolWildRiftSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLolWildRiftSeries, RangeOverLolWildRiftSeries, SearchOverLolWildRiftSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLolWildRiftSeries(
    begin_at=[
        "labo"
    ],
    end_at=[
        "co"
    ],
    id_=[
        5
    ],
    league_id=[
        2
    ],
    modified_at=[
        "in labor"
    ],
    name=[
        "velit"
    ],
    season=[
        "fugiat "
    ],
    slug=[
        "hph-bv"
    ],
    videogame_title=[
        3
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ],
    year=[
        None
    ]
)
range=RangeOverLolWildRiftSeries(
    begin_at=[
        "ex"
    ],
    end_at=[
        "ad qui aut"
    ],
    id_=[
        3
    ],
    league_id=[
        5
    ],
    modified_at=[
        "ma"
    ],
    name=[
        "ut de"
    ],
    season=[
        "nostr"
    ],
    slug=[
        "6os7g3o0bh7"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ],
    year=[
        None
    ]
)
sort=[
    ""
]
search=SearchOverLolWildRiftSeries(
    name="ea nulla proi",
    season="culpa pariat",
    slug="_tw34do",
    winner_type="Player"
)
page=1

result = sdk.lo_l_wild_rift_series.get_lol_wild_rift_series_upcoming(
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
