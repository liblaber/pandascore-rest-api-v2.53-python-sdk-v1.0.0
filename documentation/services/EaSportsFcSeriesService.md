# EaSportsFcSeriesService

A list of all methods in the `EaSportsFcSeriesService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                |
| :---------------------------------------------------- | :----------------------------------------- |
| [get_fifa_series](#get_fifa_series)                   | List series for the EA Sports FC videogame |
| [get_fifa_series_past](#get_fifa_series_past)         | List past EA Sports FC series              |
| [get_fifa_series_running](#get_fifa_series_running)   | List running EA Sports FC series           |
| [get_fifa_series_upcoming](#get_fifa_series_upcoming) | List upcoming EA Sports FC series          |

## get_fifa_series

List series for the EA Sports FC videogame

- HTTP Method: `GET`
- Endpoint: `/fifa/series`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverFifaSeries](../models/FilterOverFifaSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverFifaSeries](../models/RangeOverFifaSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverFifaSeries](../models/SearchOverFifaSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverFifaSeries, RangeOverFifaSeries, SearchOverFifaSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverFifaSeries(
    begin_at=[
        "pariat"
    ],
    end_at=[
        "n"
    ],
    id_=[
        7
    ],
    league_id=[
        3
    ],
    modified_at=[
        "elit "
    ],
    name=[
        "commo"
    ],
    season=[
        "cillum a"
    ],
    slug=[
        "mj-4az6h8u"
    ],
    videogame_title=[
        8
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
range=RangeOverFifaSeries(
    begin_at=[
        "qui nu"
    ],
    end_at=[
        "nulla elit "
    ],
    id_=[
        6
    ],
    league_id=[
        8
    ],
    modified_at=[
        "qui consequat"
    ],
    name=[
        "nulla"
    ],
    season=[
        "occaecat enim"
    ],
    slug=[
        "dw"
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
search=SearchOverFifaSeries(
    name="sed do",
    season="cillum d",
    slug="ou",
    winner_type="Player"
)
page=1

result = sdk.ea_sports_fc_series.get_fifa_series(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_fifa_series_past

List past EA Sports FC series

- HTTP Method: `GET`
- Endpoint: `/fifa/series/past`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverFifaSeries](../models/FilterOverFifaSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverFifaSeries](../models/RangeOverFifaSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverFifaSeries](../models/SearchOverFifaSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverFifaSeries, RangeOverFifaSeries, SearchOverFifaSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverFifaSeries(
    begin_at=[
        "pariat"
    ],
    end_at=[
        "n"
    ],
    id_=[
        7
    ],
    league_id=[
        3
    ],
    modified_at=[
        "elit "
    ],
    name=[
        "commo"
    ],
    season=[
        "cillum a"
    ],
    slug=[
        "mj-4az6h8u"
    ],
    videogame_title=[
        8
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
range=RangeOverFifaSeries(
    begin_at=[
        "qui nu"
    ],
    end_at=[
        "nulla elit "
    ],
    id_=[
        6
    ],
    league_id=[
        8
    ],
    modified_at=[
        "qui consequat"
    ],
    name=[
        "nulla"
    ],
    season=[
        "occaecat enim"
    ],
    slug=[
        "dw"
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
search=SearchOverFifaSeries(
    name="sed do",
    season="cillum d",
    slug="ou",
    winner_type="Player"
)
page=1

result = sdk.ea_sports_fc_series.get_fifa_series_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_fifa_series_running

List running EA Sports FC series

- HTTP Method: `GET`
- Endpoint: `/fifa/series/running`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverFifaSeries](../models/FilterOverFifaSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverFifaSeries](../models/RangeOverFifaSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverFifaSeries](../models/SearchOverFifaSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverFifaSeries, RangeOverFifaSeries, SearchOverFifaSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverFifaSeries(
    begin_at=[
        "pariat"
    ],
    end_at=[
        "n"
    ],
    id_=[
        7
    ],
    league_id=[
        3
    ],
    modified_at=[
        "elit "
    ],
    name=[
        "commo"
    ],
    season=[
        "cillum a"
    ],
    slug=[
        "mj-4az6h8u"
    ],
    videogame_title=[
        8
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
range=RangeOverFifaSeries(
    begin_at=[
        "qui nu"
    ],
    end_at=[
        "nulla elit "
    ],
    id_=[
        6
    ],
    league_id=[
        8
    ],
    modified_at=[
        "qui consequat"
    ],
    name=[
        "nulla"
    ],
    season=[
        "occaecat enim"
    ],
    slug=[
        "dw"
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
search=SearchOverFifaSeries(
    name="sed do",
    season="cillum d",
    slug="ou",
    winner_type="Player"
)
page=1

result = sdk.ea_sports_fc_series.get_fifa_series_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_fifa_series_upcoming

List upcoming EA Sports FC series

- HTTP Method: `GET`
- Endpoint: `/fifa/series/upcoming`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverFifaSeries](../models/FilterOverFifaSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverFifaSeries](../models/RangeOverFifaSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverFifaSeries](../models/SearchOverFifaSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverFifaSeries, RangeOverFifaSeries, SearchOverFifaSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverFifaSeries(
    begin_at=[
        "pariat"
    ],
    end_at=[
        "n"
    ],
    id_=[
        7
    ],
    league_id=[
        3
    ],
    modified_at=[
        "elit "
    ],
    name=[
        "commo"
    ],
    season=[
        "cillum a"
    ],
    slug=[
        "mj-4az6h8u"
    ],
    videogame_title=[
        8
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
range=RangeOverFifaSeries(
    begin_at=[
        "qui nu"
    ],
    end_at=[
        "nulla elit "
    ],
    id_=[
        6
    ],
    league_id=[
        8
    ],
    modified_at=[
        "qui consequat"
    ],
    name=[
        "nulla"
    ],
    season=[
        "occaecat enim"
    ],
    slug=[
        "dw"
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
search=SearchOverFifaSeries(
    name="sed do",
    season="cillum d",
    slug="ou",
    winner_type="Player"
)
page=1

result = sdk.ea_sports_fc_series.get_fifa_series_upcoming(
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
