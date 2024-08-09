# KogSeriesService

A list of all methods in the `KogSeriesService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description                                 |
| :-------------------------------------------------- | :------------------------------------------ |
| [get_kog_series](#get_kog_series)                   | List series for the King of Glory videogame |
| [get_kog_series_past](#get_kog_series_past)         | List past King of Glory series              |
| [get_kog_series_running](#get_kog_series_running)   | List running King of Glory series           |
| [get_kog_series_upcoming](#get_kog_series_upcoming) | List upcoming King of Glory series          |

## get_kog_series

List series for the King of Glory videogame

- HTTP Method: `GET`
- Endpoint: `/kog/series`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverKogSeries](../models/FilterOverKogSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverKogSeries](../models/RangeOverKogSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverKogSeries](../models/SearchOverKogSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverKogSeries, RangeOverKogSeries, SearchOverKogSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverKogSeries(
    begin_at=[
        "ex"
    ],
    end_at=[
        "in sit no"
    ],
    id_=[
        8
    ],
    league_id=[
        9
    ],
    modified_at=[
        "veniam"
    ],
    name=[
        "aliquip eiu"
    ],
    season=[
        "nulla"
    ],
    slug=[
        "_p3_cuw5"
    ],
    videogame_title=[
        7
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
range=RangeOverKogSeries(
    begin_at=[
        "i"
    ],
    end_at=[
        "ut"
    ],
    id_=[
        2
    ],
    league_id=[
        4
    ],
    modified_at=[
        "minim id p"
    ],
    name=[
        "volupta"
    ],
    season=[
        "officia"
    ],
    slug=[
        "nl"
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
search=SearchOverKogSeries(
    name="aliqu",
    season="dolor ipsum ",
    slug="-n",
    winner_type="Player"
)
page=1

result = sdk.kog_series.get_kog_series(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_kog_series_past

List past King of Glory series

- HTTP Method: `GET`
- Endpoint: `/kog/series/past`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverKogSeries](../models/FilterOverKogSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverKogSeries](../models/RangeOverKogSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverKogSeries](../models/SearchOverKogSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverKogSeries, RangeOverKogSeries, SearchOverKogSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverKogSeries(
    begin_at=[
        "ex"
    ],
    end_at=[
        "in sit no"
    ],
    id_=[
        8
    ],
    league_id=[
        9
    ],
    modified_at=[
        "veniam"
    ],
    name=[
        "aliquip eiu"
    ],
    season=[
        "nulla"
    ],
    slug=[
        "_p3_cuw5"
    ],
    videogame_title=[
        7
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
range=RangeOverKogSeries(
    begin_at=[
        "i"
    ],
    end_at=[
        "ut"
    ],
    id_=[
        2
    ],
    league_id=[
        4
    ],
    modified_at=[
        "minim id p"
    ],
    name=[
        "volupta"
    ],
    season=[
        "officia"
    ],
    slug=[
        "nl"
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
search=SearchOverKogSeries(
    name="aliqu",
    season="dolor ipsum ",
    slug="-n",
    winner_type="Player"
)
page=1

result = sdk.kog_series.get_kog_series_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_kog_series_running

List running King of Glory series

- HTTP Method: `GET`
- Endpoint: `/kog/series/running`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverKogSeries](../models/FilterOverKogSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverKogSeries](../models/RangeOverKogSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverKogSeries](../models/SearchOverKogSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverKogSeries, RangeOverKogSeries, SearchOverKogSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverKogSeries(
    begin_at=[
        "ex"
    ],
    end_at=[
        "in sit no"
    ],
    id_=[
        8
    ],
    league_id=[
        9
    ],
    modified_at=[
        "veniam"
    ],
    name=[
        "aliquip eiu"
    ],
    season=[
        "nulla"
    ],
    slug=[
        "_p3_cuw5"
    ],
    videogame_title=[
        7
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
range=RangeOverKogSeries(
    begin_at=[
        "i"
    ],
    end_at=[
        "ut"
    ],
    id_=[
        2
    ],
    league_id=[
        4
    ],
    modified_at=[
        "minim id p"
    ],
    name=[
        "volupta"
    ],
    season=[
        "officia"
    ],
    slug=[
        "nl"
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
search=SearchOverKogSeries(
    name="aliqu",
    season="dolor ipsum ",
    slug="-n",
    winner_type="Player"
)
page=1

result = sdk.kog_series.get_kog_series_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_kog_series_upcoming

List upcoming King of Glory series

- HTTP Method: `GET`
- Endpoint: `/kog/series/upcoming`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverKogSeries](../models/FilterOverKogSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverKogSeries](../models/RangeOverKogSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverKogSeries](../models/SearchOverKogSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverKogSeries, RangeOverKogSeries, SearchOverKogSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverKogSeries(
    begin_at=[
        "ex"
    ],
    end_at=[
        "in sit no"
    ],
    id_=[
        8
    ],
    league_id=[
        9
    ],
    modified_at=[
        "veniam"
    ],
    name=[
        "aliquip eiu"
    ],
    season=[
        "nulla"
    ],
    slug=[
        "_p3_cuw5"
    ],
    videogame_title=[
        7
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
range=RangeOverKogSeries(
    begin_at=[
        "i"
    ],
    end_at=[
        "ut"
    ],
    id_=[
        2
    ],
    league_id=[
        4
    ],
    modified_at=[
        "minim id p"
    ],
    name=[
        "volupta"
    ],
    season=[
        "officia"
    ],
    slug=[
        "nl"
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
search=SearchOverKogSeries(
    name="aliqu",
    season="dolor ipsum ",
    slug="-n",
    winner_type="Player"
)
page=1

result = sdk.kog_series.get_kog_series_upcoming(
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
