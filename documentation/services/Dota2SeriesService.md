# Dota2SeriesService

A list of all methods in the `Dota2SeriesService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                          |
| :------------------------------------------------------ | :----------------------------------- |
| [get_dota2_series](#get_dota2_series)                   | List series for the Dota 2 videogame |
| [get_dota2_series_past](#get_dota2_series_past)         | List past Dota 2 series              |
| [get_dota2_series_running](#get_dota2_series_running)   | List running Dota 2 series           |
| [get_dota2_series_upcoming](#get_dota2_series_upcoming) | List upcoming Dota 2 series          |

## get_dota2_series

List series for the Dota 2 videogame

- HTTP Method: `GET`
- Endpoint: `/dota2/series`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverDota2Series](../models/FilterOverDota2Series.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverDota2Series](../models/RangeOverDota2Series.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverDota2Series](../models/SearchOverDota2Series.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverDota2Series, RangeOverDota2Series, SearchOverDota2Series

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverDota2Series(
    begin_at=[
        "cillum d"
    ],
    end_at=[
        "laboris"
    ],
    id_=[
        5
    ],
    league_id=[
        3
    ],
    modified_at=[
        "null"
    ],
    name=[
        "dolore"
    ],
    season=[
        "ut qui "
    ],
    slug=[
        "e7cx9f3y"
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
range=RangeOverDota2Series(
    begin_at=[
        "exercitation"
    ],
    end_at=[
        "ex"
    ],
    id_=[
        4
    ],
    league_id=[
        10
    ],
    modified_at=[
        "incididunt "
    ],
    name=[
        "dolor elit co"
    ],
    season=[
        "exercitat"
    ],
    slug=[
        "6wkd46"
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
search=SearchOverDota2Series(
    name="dolore ut en",
    season="autesed",
    slug="1jo-8",
    winner_type="Player"
)
page=1

result = sdk.dota2_series.get_dota2_series(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_dota2_series_past

List past Dota 2 series

- HTTP Method: `GET`
- Endpoint: `/dota2/series/past`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverDota2Series](../models/FilterOverDota2Series.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverDota2Series](../models/RangeOverDota2Series.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverDota2Series](../models/SearchOverDota2Series.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverDota2Series, RangeOverDota2Series, SearchOverDota2Series

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverDota2Series(
    begin_at=[
        "cillum d"
    ],
    end_at=[
        "laboris"
    ],
    id_=[
        5
    ],
    league_id=[
        3
    ],
    modified_at=[
        "null"
    ],
    name=[
        "dolore"
    ],
    season=[
        "ut qui "
    ],
    slug=[
        "e7cx9f3y"
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
range=RangeOverDota2Series(
    begin_at=[
        "exercitation"
    ],
    end_at=[
        "ex"
    ],
    id_=[
        4
    ],
    league_id=[
        10
    ],
    modified_at=[
        "incididunt "
    ],
    name=[
        "dolor elit co"
    ],
    season=[
        "exercitat"
    ],
    slug=[
        "6wkd46"
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
search=SearchOverDota2Series(
    name="dolore ut en",
    season="autesed",
    slug="1jo-8",
    winner_type="Player"
)
page=1

result = sdk.dota2_series.get_dota2_series_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_dota2_series_running

List running Dota 2 series

- HTTP Method: `GET`
- Endpoint: `/dota2/series/running`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverDota2Series](../models/FilterOverDota2Series.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverDota2Series](../models/RangeOverDota2Series.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverDota2Series](../models/SearchOverDota2Series.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverDota2Series, RangeOverDota2Series, SearchOverDota2Series

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverDota2Series(
    begin_at=[
        "cillum d"
    ],
    end_at=[
        "laboris"
    ],
    id_=[
        5
    ],
    league_id=[
        3
    ],
    modified_at=[
        "null"
    ],
    name=[
        "dolore"
    ],
    season=[
        "ut qui "
    ],
    slug=[
        "e7cx9f3y"
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
range=RangeOverDota2Series(
    begin_at=[
        "exercitation"
    ],
    end_at=[
        "ex"
    ],
    id_=[
        4
    ],
    league_id=[
        10
    ],
    modified_at=[
        "incididunt "
    ],
    name=[
        "dolor elit co"
    ],
    season=[
        "exercitat"
    ],
    slug=[
        "6wkd46"
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
search=SearchOverDota2Series(
    name="dolore ut en",
    season="autesed",
    slug="1jo-8",
    winner_type="Player"
)
page=1

result = sdk.dota2_series.get_dota2_series_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_dota2_series_upcoming

List upcoming Dota 2 series

- HTTP Method: `GET`
- Endpoint: `/dota2/series/upcoming`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverDota2Series](../models/FilterOverDota2Series.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverDota2Series](../models/RangeOverDota2Series.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverDota2Series](../models/SearchOverDota2Series.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverDota2Series, RangeOverDota2Series, SearchOverDota2Series

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverDota2Series(
    begin_at=[
        "cillum d"
    ],
    end_at=[
        "laboris"
    ],
    id_=[
        5
    ],
    league_id=[
        3
    ],
    modified_at=[
        "null"
    ],
    name=[
        "dolore"
    ],
    season=[
        "ut qui "
    ],
    slug=[
        "e7cx9f3y"
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
range=RangeOverDota2Series(
    begin_at=[
        "exercitation"
    ],
    end_at=[
        "ex"
    ],
    id_=[
        4
    ],
    league_id=[
        10
    ],
    modified_at=[
        "incididunt "
    ],
    name=[
        "dolor elit co"
    ],
    season=[
        "exercitat"
    ],
    slug=[
        "6wkd46"
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
search=SearchOverDota2Series(
    name="dolore ut en",
    season="autesed",
    slug="1jo-8",
    winner_type="Player"
)
page=1

result = sdk.dota2_series.get_dota2_series_upcoming(
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
