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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverDota2Series, RangeOverDota2Series, SearchOverDota2Series

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverDota2Series(
    begin_at=[
        "et"
    ],
    end_at=[
        "ut"
    ],
    id_=[
        3
    ],
    league_id=[
        7
    ],
    modified_at=[
        "nostrud"
    ],
    name=[
        "Utinip"
    ],
    season=[
        "innostrud i"
    ],
    slug=[
        "_fv34g5ds"
    ],
    videogame_title=[
        3
    ],
    winner_id=[
        9
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
        "culpa do"
    ],
    end_at=[
        "exercitation of"
    ],
    id_=[
        1
    ],
    league_id=[
        10
    ],
    modified_at=[
        "nostrud labo"
    ],
    name=[
        "nostrud se"
    ],
    season=[
        "Lorem id Ut "
    ],
    slug=[
        "fjj0_"
    ],
    winner_id=[
        9
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
    name="nulla",
    season="elitad c",
    slug="zhc",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverDota2Series, RangeOverDota2Series, SearchOverDota2Series

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverDota2Series(
    begin_at=[
        "et"
    ],
    end_at=[
        "ut"
    ],
    id_=[
        3
    ],
    league_id=[
        7
    ],
    modified_at=[
        "nostrud"
    ],
    name=[
        "Utinip"
    ],
    season=[
        "innostrud i"
    ],
    slug=[
        "_fv34g5ds"
    ],
    videogame_title=[
        3
    ],
    winner_id=[
        9
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
        "culpa do"
    ],
    end_at=[
        "exercitation of"
    ],
    id_=[
        1
    ],
    league_id=[
        10
    ],
    modified_at=[
        "nostrud labo"
    ],
    name=[
        "nostrud se"
    ],
    season=[
        "Lorem id Ut "
    ],
    slug=[
        "fjj0_"
    ],
    winner_id=[
        9
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
    name="nulla",
    season="elitad c",
    slug="zhc",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverDota2Series, RangeOverDota2Series, SearchOverDota2Series

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverDota2Series(
    begin_at=[
        "et"
    ],
    end_at=[
        "ut"
    ],
    id_=[
        3
    ],
    league_id=[
        7
    ],
    modified_at=[
        "nostrud"
    ],
    name=[
        "Utinip"
    ],
    season=[
        "innostrud i"
    ],
    slug=[
        "_fv34g5ds"
    ],
    videogame_title=[
        3
    ],
    winner_id=[
        9
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
        "culpa do"
    ],
    end_at=[
        "exercitation of"
    ],
    id_=[
        1
    ],
    league_id=[
        10
    ],
    modified_at=[
        "nostrud labo"
    ],
    name=[
        "nostrud se"
    ],
    season=[
        "Lorem id Ut "
    ],
    slug=[
        "fjj0_"
    ],
    winner_id=[
        9
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
    name="nulla",
    season="elitad c",
    slug="zhc",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverDota2Series, RangeOverDota2Series, SearchOverDota2Series

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverDota2Series(
    begin_at=[
        "et"
    ],
    end_at=[
        "ut"
    ],
    id_=[
        3
    ],
    league_id=[
        7
    ],
    modified_at=[
        "nostrud"
    ],
    name=[
        "Utinip"
    ],
    season=[
        "innostrud i"
    ],
    slug=[
        "_fv34g5ds"
    ],
    videogame_title=[
        3
    ],
    winner_id=[
        9
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
        "culpa do"
    ],
    end_at=[
        "exercitation of"
    ],
    id_=[
        1
    ],
    league_id=[
        10
    ],
    modified_at=[
        "nostrud labo"
    ],
    name=[
        "nostrud se"
    ],
    season=[
        "Lorem id Ut "
    ],
    slug=[
        "fjj0_"
    ],
    winner_id=[
        9
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
    name="nulla",
    season="elitad c",
    slug="zhc",
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
