# LoLSeriesService

A list of all methods in the `LoLSeriesService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description                                     |
| :-------------------------------------------------- | :---------------------------------------------- |
| [get_lol_series](#get_lol_series)                   | List series for the League of Legends videogame |
| [get_lol_series_past](#get_lol_series_past)         | List past League of Legends series              |
| [get_lol_series_running](#get_lol_series_running)   | List running League of Legends series           |
| [get_lol_series_upcoming](#get_lol_series_upcoming) | List upcoming League of Legends series          |

## get_lol_series

List series for the League of Legends videogame

- HTTP Method: `GET`
- Endpoint: `/lol/series`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLSeries](../models/FilterOverLoLSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLSeries](../models/RangeOverLoLSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLSeries](../models/SearchOverLoLSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLSeries, RangeOverLoLSeries, SearchOverLoLSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLoLSeries(
    begin_at=[
        "nisi amet"
    ],
    end_at=[
        "reprehen"
    ],
    id_=[
        7
    ],
    league_id=[
        2
    ],
    modified_at=[
        "Ut "
    ],
    name=[
        "sintmoll"
    ],
    season=[
        "ad aliqua in"
    ],
    slug=[
        "1br98fc"
    ],
    videogame_title=[
        9
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
range=RangeOverLoLSeries(
    begin_at=[
        "sint co"
    ],
    end_at=[
        "tempor esse co"
    ],
    id_=[
        7
    ],
    league_id=[
        3
    ],
    modified_at=[
        "E"
    ],
    name=[
        "eliti"
    ],
    season=[
        "labore exercita"
    ],
    slug=[
        "93mxp18t"
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
search=SearchOverLoLSeries(
    name="mollit p",
    season="exerc",
    slug="wm55",
    winner_type="Player"
)
page=1

result = sdk.lo_l_series.get_lol_series(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_series_past

List past League of Legends series

- HTTP Method: `GET`
- Endpoint: `/lol/series/past`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLSeries](../models/FilterOverLoLSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLSeries](../models/RangeOverLoLSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLSeries](../models/SearchOverLoLSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLSeries, RangeOverLoLSeries, SearchOverLoLSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLoLSeries(
    begin_at=[
        "nisi amet"
    ],
    end_at=[
        "reprehen"
    ],
    id_=[
        7
    ],
    league_id=[
        2
    ],
    modified_at=[
        "Ut "
    ],
    name=[
        "sintmoll"
    ],
    season=[
        "ad aliqua in"
    ],
    slug=[
        "1br98fc"
    ],
    videogame_title=[
        9
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
range=RangeOverLoLSeries(
    begin_at=[
        "sint co"
    ],
    end_at=[
        "tempor esse co"
    ],
    id_=[
        7
    ],
    league_id=[
        3
    ],
    modified_at=[
        "E"
    ],
    name=[
        "eliti"
    ],
    season=[
        "labore exercita"
    ],
    slug=[
        "93mxp18t"
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
search=SearchOverLoLSeries(
    name="mollit p",
    season="exerc",
    slug="wm55",
    winner_type="Player"
)
page=1

result = sdk.lo_l_series.get_lol_series_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_series_running

List running League of Legends series

- HTTP Method: `GET`
- Endpoint: `/lol/series/running`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLSeries](../models/FilterOverLoLSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLSeries](../models/RangeOverLoLSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLSeries](../models/SearchOverLoLSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLSeries, RangeOverLoLSeries, SearchOverLoLSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLoLSeries(
    begin_at=[
        "nisi amet"
    ],
    end_at=[
        "reprehen"
    ],
    id_=[
        7
    ],
    league_id=[
        2
    ],
    modified_at=[
        "Ut "
    ],
    name=[
        "sintmoll"
    ],
    season=[
        "ad aliqua in"
    ],
    slug=[
        "1br98fc"
    ],
    videogame_title=[
        9
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
range=RangeOverLoLSeries(
    begin_at=[
        "sint co"
    ],
    end_at=[
        "tempor esse co"
    ],
    id_=[
        7
    ],
    league_id=[
        3
    ],
    modified_at=[
        "E"
    ],
    name=[
        "eliti"
    ],
    season=[
        "labore exercita"
    ],
    slug=[
        "93mxp18t"
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
search=SearchOverLoLSeries(
    name="mollit p",
    season="exerc",
    slug="wm55",
    winner_type="Player"
)
page=1

result = sdk.lo_l_series.get_lol_series_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_series_upcoming

List upcoming League of Legends series

- HTTP Method: `GET`
- Endpoint: `/lol/series/upcoming`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLSeries](../models/FilterOverLoLSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLSeries](../models/RangeOverLoLSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLSeries](../models/SearchOverLoLSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLSeries, RangeOverLoLSeries, SearchOverLoLSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLoLSeries(
    begin_at=[
        "nisi amet"
    ],
    end_at=[
        "reprehen"
    ],
    id_=[
        7
    ],
    league_id=[
        2
    ],
    modified_at=[
        "Ut "
    ],
    name=[
        "sintmoll"
    ],
    season=[
        "ad aliqua in"
    ],
    slug=[
        "1br98fc"
    ],
    videogame_title=[
        9
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
range=RangeOverLoLSeries(
    begin_at=[
        "sint co"
    ],
    end_at=[
        "tempor esse co"
    ],
    id_=[
        7
    ],
    league_id=[
        3
    ],
    modified_at=[
        "E"
    ],
    name=[
        "eliti"
    ],
    season=[
        "labore exercita"
    ],
    slug=[
        "93mxp18t"
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
search=SearchOverLoLSeries(
    name="mollit p",
    season="exerc",
    slug="wm55",
    winner_type="Player"
)
page=1

result = sdk.lo_l_series.get_lol_series_upcoming(
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
