# OwSeriesService

A list of all methods in the `OwSeriesService` service. Click on the method name to view detailed information about that method.

| Methods                                           | Description                             |
| :------------------------------------------------ | :-------------------------------------- |
| [get_ow_series](#get_ow_series)                   | List series for the Overwatch videogame |
| [get_ow_series_past](#get_ow_series_past)         | List past Overwatch series              |
| [get_ow_series_running](#get_ow_series_running)   | List running Overwatch series           |
| [get_ow_series_upcoming](#get_ow_series_upcoming) | List upcoming Overwatch series          |

## get_ow_series

List series for the Overwatch videogame

- HTTP Method: `GET`
- Endpoint: `/ow/series`

**Parameters**

| Name     | Type                                                  | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverOwSeries](../models/FilterOverOwSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverOwSeries](../models/RangeOverOwSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverOwSeries](../models/SearchOverOwSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverOwSeries, RangeOverOwSeries, SearchOverOwSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverOwSeries(
    begin_at=[
        "deserunt"
    ],
    end_at=[
        "dolore"
    ],
    id_=[
        8
    ],
    league_id=[
        3
    ],
    modified_at=[
        "non in "
    ],
    name=[
        "ut consectetu"
    ],
    season=[
        "incidi"
    ],
    slug=[
        "0s_31dv1"
    ],
    videogame_title=[
        5
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
range=RangeOverOwSeries(
    begin_at=[
        "Exce"
    ],
    end_at=[
        "t"
    ],
    id_=[
        1
    ],
    league_id=[
        2
    ],
    modified_at=[
        "nostrud i"
    ],
    name=[
        "sed enim do"
    ],
    season=[
        "culpa laborum "
    ],
    slug=[
        "98"
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
search=SearchOverOwSeries(
    name="ut qui",
    season="eiusmod",
    slug="van0",
    winner_type="Player"
)
page=1

result = sdk.ow_series.get_ow_series(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_ow_series_past

List past Overwatch series

- HTTP Method: `GET`
- Endpoint: `/ow/series/past`

**Parameters**

| Name     | Type                                                  | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverOwSeries](../models/FilterOverOwSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverOwSeries](../models/RangeOverOwSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverOwSeries](../models/SearchOverOwSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverOwSeries, RangeOverOwSeries, SearchOverOwSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverOwSeries(
    begin_at=[
        "deserunt"
    ],
    end_at=[
        "dolore"
    ],
    id_=[
        8
    ],
    league_id=[
        3
    ],
    modified_at=[
        "non in "
    ],
    name=[
        "ut consectetu"
    ],
    season=[
        "incidi"
    ],
    slug=[
        "0s_31dv1"
    ],
    videogame_title=[
        5
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
range=RangeOverOwSeries(
    begin_at=[
        "Exce"
    ],
    end_at=[
        "t"
    ],
    id_=[
        1
    ],
    league_id=[
        2
    ],
    modified_at=[
        "nostrud i"
    ],
    name=[
        "sed enim do"
    ],
    season=[
        "culpa laborum "
    ],
    slug=[
        "98"
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
search=SearchOverOwSeries(
    name="ut qui",
    season="eiusmod",
    slug="van0",
    winner_type="Player"
)
page=1

result = sdk.ow_series.get_ow_series_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_ow_series_running

List running Overwatch series

- HTTP Method: `GET`
- Endpoint: `/ow/series/running`

**Parameters**

| Name     | Type                                                  | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverOwSeries](../models/FilterOverOwSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverOwSeries](../models/RangeOverOwSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverOwSeries](../models/SearchOverOwSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverOwSeries, RangeOverOwSeries, SearchOverOwSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverOwSeries(
    begin_at=[
        "deserunt"
    ],
    end_at=[
        "dolore"
    ],
    id_=[
        8
    ],
    league_id=[
        3
    ],
    modified_at=[
        "non in "
    ],
    name=[
        "ut consectetu"
    ],
    season=[
        "incidi"
    ],
    slug=[
        "0s_31dv1"
    ],
    videogame_title=[
        5
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
range=RangeOverOwSeries(
    begin_at=[
        "Exce"
    ],
    end_at=[
        "t"
    ],
    id_=[
        1
    ],
    league_id=[
        2
    ],
    modified_at=[
        "nostrud i"
    ],
    name=[
        "sed enim do"
    ],
    season=[
        "culpa laborum "
    ],
    slug=[
        "98"
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
search=SearchOverOwSeries(
    name="ut qui",
    season="eiusmod",
    slug="van0",
    winner_type="Player"
)
page=1

result = sdk.ow_series.get_ow_series_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_ow_series_upcoming

List upcoming Overwatch series

- HTTP Method: `GET`
- Endpoint: `/ow/series/upcoming`

**Parameters**

| Name     | Type                                                  | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverOwSeries](../models/FilterOverOwSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverOwSeries](../models/RangeOverOwSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverOwSeries](../models/SearchOverOwSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverOwSeries, RangeOverOwSeries, SearchOverOwSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverOwSeries(
    begin_at=[
        "deserunt"
    ],
    end_at=[
        "dolore"
    ],
    id_=[
        8
    ],
    league_id=[
        3
    ],
    modified_at=[
        "non in "
    ],
    name=[
        "ut consectetu"
    ],
    season=[
        "incidi"
    ],
    slug=[
        "0s_31dv1"
    ],
    videogame_title=[
        5
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
range=RangeOverOwSeries(
    begin_at=[
        "Exce"
    ],
    end_at=[
        "t"
    ],
    id_=[
        1
    ],
    league_id=[
        2
    ],
    modified_at=[
        "nostrud i"
    ],
    name=[
        "sed enim do"
    ],
    season=[
        "culpa laborum "
    ],
    slug=[
        "98"
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
search=SearchOverOwSeries(
    name="ut qui",
    season="eiusmod",
    slug="van0",
    winner_type="Player"
)
page=1

result = sdk.ow_series.get_ow_series_upcoming(
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
