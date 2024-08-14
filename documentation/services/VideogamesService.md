# VideogamesService

A list of all methods in the `VideogamesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                             | Description                                   |
| :-------------------------------------------------------------------------------------------------- | :-------------------------------------------- |
| [get_videogames](#get_videogames)                                                                   | List videogames                               |
| [get_videogames_videogame_id_or_slug](#get_videogames_videogame_id_or_slug)                         | Get a single videogame by ID or by slug       |
| [get_videogames_videogame_id_or_slug_leagues](#get_videogames_videogame_id_or_slug_leagues)         | List leagues for a given videogame            |
| [get_videogames_videogame_id_or_slug_series](#get_videogames_videogame_id_or_slug_series)           | List series for the given videogame           |
| [get_videogames_videogame_id_or_slug_titles](#get_videogames_videogame_id_or_slug_titles)           | List available titles for a given videogame   |
| [get_videogames_videogame_id_or_slug_tournaments](#get_videogames_videogame_id_or_slug_tournaments) | List tournaments of the given videogame       |
| [get_videogames_videogame_id_or_slug_versions](#get_videogames_videogame_id_or_slug_versions)       | List available versions for a given videogame |

## get_videogames

List videogames

- HTTP Method: `GET`
- Endpoint: `/videogames`

**Parameters**

| Name     | Type                      | Required | Description                                                          |
| :------- | :------------------------ | :------- | :------------------------------------------------------------------- |
| page     | [Page](../models/Page.md) | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2` |
| per_page | int                       | ❌       | Equivalent to `page[size]`                                           |

**Return Type**

`List[Videogame]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
page=1

result = sdk.videogames.get_videogames(
    page=page,
    per_page=50
)

print(result)
```

## get_videogames_videogame_id_or_slug

Get a single videogame by ID or by slug

- HTTP Method: `GET`
- Endpoint: `/videogames/{videogame_id_or_slug}`

**Parameters**

| Name                 | Type                                                | Required | Description            |
| :------------------- | :-------------------------------------------------- | :------- | :--------------------- |
| videogame_id_or_slug | [VideogameIdOrSlug](../models/VideogameIdOrSlug.md) | ✅       | A videogame ID or slug |

**Return Type**

`Videogame`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models.videogame_id_or_slug import VideogameId

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
videogame_id_or_slug=1

result = sdk.videogames.get_videogames_videogame_id_or_slug(videogame_id_or_slug=videogame_id_or_slug)

print(result)
```

## get_videogames_videogame_id_or_slug_leagues

List leagues for a given videogame

- HTTP Method: `GET`
- Endpoint: `/videogames/{videogame_id_or_slug}/leagues`

**Parameters**

| Name                 | Type                                                | Required | Description                                                                                                                                         |
| :------------------- | :-------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| videogame_id_or_slug | [VideogameIdOrSlug](../models/VideogameIdOrSlug.md) | ✅       | A videogame ID or slug                                                                                                                              |
| filter               | [FilterOverLeagues](../models/FilterOverLeagues.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range                | [RangeOverLeagues](../models/RangeOverLeagues.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort                 | List[any]                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search               | [SearchOverLeagues](../models/SearchOverLeagues.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page                 | [Page](../models/Page.md)                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page             | int                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[League]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLeagues, RangeOverLeagues, SearchOverLeagues
from pandascore_client.models.videogame_id_or_slug import VideogameId

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
videogame_id_or_slug=1
filter=FilterOverLeagues(
    id_=[
        7
    ],
    modified_at=[
        "offici"
    ],
    name=[
        "ad ut"
    ],
    slug=[
        "p_"
    ],
    url=[
        "esse aliqu"
    ]
)
range=RangeOverLeagues(
    id_=[
        10
    ],
    modified_at=[
        "ut nulla"
    ],
    name=[
        "ea mol"
    ],
    slug=[
        "pmjvmw-84d"
    ],
    url=[
        "ea aliquip"
    ]
)
sort=[
    ""
]
search=SearchOverLeagues(
    name="Duis dolo",
    slug="-teig",
    url="adipisicing"
)
page=1

result = sdk.videogames.get_videogames_videogame_id_or_slug_leagues(
    videogame_id_or_slug=videogame_id_or_slug,
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_videogames_videogame_id_or_slug_series

List series for the given videogame

- HTTP Method: `GET`
- Endpoint: `/videogames/{videogame_id_or_slug}/series`

**Parameters**

| Name                 | Type                                                | Required | Description                                                                                                                                         |
| :------------------- | :-------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| videogame_id_or_slug | [VideogameIdOrSlug](../models/VideogameIdOrSlug.md) | ✅       | A videogame ID or slug                                                                                                                              |
| filter               | [FilterOverSeries](../models/FilterOverSeries.md)   | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range                | [RangeOverSeries](../models/RangeOverSeries.md)     | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort                 | List[any]                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search               | [SearchOverSeries](../models/SearchOverSeries.md)   | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page                 | [Page](../models/Page.md)                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page             | int                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverSeries, RangeOverSeries, SearchOverSeries
from pandascore_client.models.videogame_id_or_slug import VideogameId

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
videogame_id_or_slug=1
filter=FilterOverSeries(
    begin_at=[
        "sunt cillum dol"
    ],
    end_at=[
        "dolor"
    ],
    id_=[
        5
    ],
    league_id=[
        7
    ],
    modified_at=[
        "deserunt"
    ],
    name=[
        "laboris"
    ],
    season=[
        "proident"
    ],
    slug=[
        "_9"
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
range=RangeOverSeries(
    begin_at=[
        "sint c"
    ],
    end_at=[
        "ex dolore tempo"
    ],
    id_=[
        6
    ],
    league_id=[
        6
    ],
    modified_at=[
        "lab"
    ],
    name=[
        "animea labore e"
    ],
    season=[
        "ipsum i"
    ],
    slug=[
        "8"
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
search=SearchOverSeries(
    name="fugia",
    season="aute al",
    slug="cc3u_",
    winner_type="Player"
)
page=1

result = sdk.videogames.get_videogames_videogame_id_or_slug_series(
    videogame_id_or_slug=videogame_id_or_slug,
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_videogames_videogame_id_or_slug_titles

List available titles for a given videogame

- HTTP Method: `GET`
- Endpoint: `/videogames/{videogame_id_or_slug}/titles`

**Parameters**

| Name                 | Type                                                | Required | Description                                                          |
| :------------------- | :-------------------------------------------------- | :------- | :------------------------------------------------------------------- |
| videogame_id_or_slug | [VideogameIdOrSlug](../models/VideogameIdOrSlug.md) | ✅       | A videogame ID or slug                                               |
| page                 | [Page](../models/Page.md)                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2` |
| per_page             | int                                                 | ❌       | Equivalent to `page[size]`                                           |

**Return Type**

`List[ShortVideogameTitle]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models.videogame_id_or_slug import VideogameId

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
videogame_id_or_slug=1
page=1

result = sdk.videogames.get_videogames_videogame_id_or_slug_titles(
    videogame_id_or_slug=videogame_id_or_slug,
    page=page,
    per_page=50
)

print(result)
```

## get_videogames_videogame_id_or_slug_tournaments

List tournaments of the given videogame

- HTTP Method: `GET`
- Endpoint: `/videogames/{videogame_id_or_slug}/tournaments`

**Parameters**

| Name                 | Type                                                                  | Required | Description                                                                                                                                         |
| :------------------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| videogame_id_or_slug | [VideogameIdOrSlug](../models/VideogameIdOrSlug.md)                   | ✅       | A videogame ID or slug                                                                                                                              |
| filter               | [FilterOverShortTournaments](../models/FilterOverShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range                | [RangeOverShortTournaments](../models/RangeOverShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort                 | List[any]                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search               | [SearchOverShortTournaments](../models/SearchOverShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page                 | [Page](../models/Page.md)                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page             | int                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverShortTournaments, RangeOverShortTournaments, SearchOverShortTournaments
from pandascore_client.models.videogame_id_or_slug import VideogameId

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
videogame_id_or_slug=1
filter=FilterOverShortTournaments(
    begin_at=[
        "pariat"
    ],
    detailed_stats=True,
    end_at=[
        "eli"
    ],
    has_bracket=False,
    id_=[
        4
    ],
    live_supported=False,
    modified_at=[
        "cillu"
    ],
    name=[
        "Excepteur do"
    ],
    prizepool=[
        "in ut veniam "
    ],
    serie_id=[
        10
    ],
    slug=[
        "z160_"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        5
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverShortTournaments(
    begin_at=[
        "et"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "commo"
    ],
    has_bracket=[
        False
    ],
    id_=[
        1
    ],
    modified_at=[
        "nul"
    ],
    name=[
        "enim "
    ],
    prizepool=[
        "qui ull"
    ],
    serie_id=[
        3
    ],
    slug=[
        "vyokv"
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
search=SearchOverShortTournaments(
    name="sunt minim",
    prizepool="utid magna es",
    slug="50l9n",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.videogames.get_videogames_videogame_id_or_slug_tournaments(
    videogame_id_or_slug=videogame_id_or_slug,
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_videogames_videogame_id_or_slug_versions

List available versions for a given videogame

- HTTP Method: `GET`
- Endpoint: `/videogames/{videogame_id_or_slug}/versions`

**Parameters**

| Name                 | Type                                                | Required | Description                                                          |
| :------------------- | :-------------------------------------------------- | :------- | :------------------------------------------------------------------- |
| videogame_id_or_slug | [VideogameIdOrSlug](../models/VideogameIdOrSlug.md) | ✅       | A videogame ID or slug                                               |
| page                 | [Page](../models/Page.md)                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2` |
| per_page             | int                                                 | ❌       | Equivalent to `page[size]`                                           |

**Return Type**

`List[ShortVideogameVersion]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models.videogame_id_or_slug import VideogameId

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
videogame_id_or_slug=1
page=1

result = sdk.videogames.get_videogames_videogame_id_or_slug_versions(
    videogame_id_or_slug=videogame_id_or_slug,
    page=page,
    per_page=50
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
