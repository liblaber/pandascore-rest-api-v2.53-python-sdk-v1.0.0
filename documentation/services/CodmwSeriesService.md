# CodmwSeriesService

A list of all methods in the `CodmwSeriesService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                         |
| :------------------------------------------------------ | :---------------------------------- |
| [get_codmw_series](#get_codmw_series)                   | List series for the CODMW videogame |
| [get_codmw_series_past](#get_codmw_series_past)         | List past CODMW series              |
| [get_codmw_series_running](#get_codmw_series_running)   | List running CODMW series           |
| [get_codmw_series_upcoming](#get_codmw_series_upcoming) | List upcoming CODMW series          |

## get_codmw_series

List series for the CODMW videogame

- HTTP Method: `GET`
- Endpoint: `/codmw/series`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCodmwSeries](../models/FilterOverCodmwSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCodmwSeries](../models/RangeOverCodmwSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCodmwSeries](../models/SearchOverCodmwSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCodmwSeries, RangeOverCodmwSeries, SearchOverCodmwSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCodmwSeries(
    begin_at=[
        "aliquip minim d"
    ],
    end_at=[
        "aute ad ea"
    ],
    id_=[
        3
    ],
    league_id=[
        6
    ],
    modified_at=[
        "quis offi"
    ],
    name=[
        "labor"
    ],
    season=[
        "veniam qui cons"
    ],
    slug=[
        "hizoyph83_0"
    ],
    videogame_title=[
        1
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
range=RangeOverCodmwSeries(
    begin_at=[
        "aliq"
    ],
    end_at=[
        "est dolore eu"
    ],
    id_=[
        10
    ],
    league_id=[
        7
    ],
    modified_at=[
        "dolor pro"
    ],
    name=[
        "anim ex eli"
    ],
    season=[
        "pariatur "
    ],
    slug=[
        "ic16v7gnnll"
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
search=SearchOverCodmwSeries(
    name="qui ul",
    season="esse ullam",
    slug="c7",
    winner_type="Player"
)
page=1

result = sdk.codmw_series.get_codmw_series(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_codmw_series_past

List past CODMW series

- HTTP Method: `GET`
- Endpoint: `/codmw/series/past`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCodmwSeries](../models/FilterOverCodmwSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCodmwSeries](../models/RangeOverCodmwSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCodmwSeries](../models/SearchOverCodmwSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCodmwSeries, RangeOverCodmwSeries, SearchOverCodmwSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCodmwSeries(
    begin_at=[
        "aliquip minim d"
    ],
    end_at=[
        "aute ad ea"
    ],
    id_=[
        3
    ],
    league_id=[
        6
    ],
    modified_at=[
        "quis offi"
    ],
    name=[
        "labor"
    ],
    season=[
        "veniam qui cons"
    ],
    slug=[
        "hizoyph83_0"
    ],
    videogame_title=[
        1
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
range=RangeOverCodmwSeries(
    begin_at=[
        "aliq"
    ],
    end_at=[
        "est dolore eu"
    ],
    id_=[
        10
    ],
    league_id=[
        7
    ],
    modified_at=[
        "dolor pro"
    ],
    name=[
        "anim ex eli"
    ],
    season=[
        "pariatur "
    ],
    slug=[
        "ic16v7gnnll"
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
search=SearchOverCodmwSeries(
    name="qui ul",
    season="esse ullam",
    slug="c7",
    winner_type="Player"
)
page=1

result = sdk.codmw_series.get_codmw_series_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_codmw_series_running

List running CODMW series

- HTTP Method: `GET`
- Endpoint: `/codmw/series/running`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCodmwSeries](../models/FilterOverCodmwSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCodmwSeries](../models/RangeOverCodmwSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCodmwSeries](../models/SearchOverCodmwSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCodmwSeries, RangeOverCodmwSeries, SearchOverCodmwSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCodmwSeries(
    begin_at=[
        "aliquip minim d"
    ],
    end_at=[
        "aute ad ea"
    ],
    id_=[
        3
    ],
    league_id=[
        6
    ],
    modified_at=[
        "quis offi"
    ],
    name=[
        "labor"
    ],
    season=[
        "veniam qui cons"
    ],
    slug=[
        "hizoyph83_0"
    ],
    videogame_title=[
        1
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
range=RangeOverCodmwSeries(
    begin_at=[
        "aliq"
    ],
    end_at=[
        "est dolore eu"
    ],
    id_=[
        10
    ],
    league_id=[
        7
    ],
    modified_at=[
        "dolor pro"
    ],
    name=[
        "anim ex eli"
    ],
    season=[
        "pariatur "
    ],
    slug=[
        "ic16v7gnnll"
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
search=SearchOverCodmwSeries(
    name="qui ul",
    season="esse ullam",
    slug="c7",
    winner_type="Player"
)
page=1

result = sdk.codmw_series.get_codmw_series_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_codmw_series_upcoming

List upcoming CODMW series

- HTTP Method: `GET`
- Endpoint: `/codmw/series/upcoming`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCodmwSeries](../models/FilterOverCodmwSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCodmwSeries](../models/RangeOverCodmwSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCodmwSeries](../models/SearchOverCodmwSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCodmwSeries, RangeOverCodmwSeries, SearchOverCodmwSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCodmwSeries(
    begin_at=[
        "aliquip minim d"
    ],
    end_at=[
        "aute ad ea"
    ],
    id_=[
        3
    ],
    league_id=[
        6
    ],
    modified_at=[
        "quis offi"
    ],
    name=[
        "labor"
    ],
    season=[
        "veniam qui cons"
    ],
    slug=[
        "hizoyph83_0"
    ],
    videogame_title=[
        1
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
range=RangeOverCodmwSeries(
    begin_at=[
        "aliq"
    ],
    end_at=[
        "est dolore eu"
    ],
    id_=[
        10
    ],
    league_id=[
        7
    ],
    modified_at=[
        "dolor pro"
    ],
    name=[
        "anim ex eli"
    ],
    season=[
        "pariatur "
    ],
    slug=[
        "ic16v7gnnll"
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
search=SearchOverCodmwSeries(
    name="qui ul",
    season="esse ullam",
    slug="c7",
    winner_type="Player"
)
page=1

result = sdk.codmw_series.get_codmw_series_upcoming(
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
