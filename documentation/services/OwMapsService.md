# OwMapsService

A list of all methods in the `OwMapsService` service. Click on the method name to view detailed information about that method.

| Methods                                                         | Description                       |
| :-------------------------------------------------------------- | :-------------------------------- |
| [get_ow_maps](#get_ow_maps)                                     | List maps                         |
| [get_ow_maps_ow_map_id_or_slug](#get_ow_maps_ow_map_id_or_slug) | Get a single map by ID or by slug |

## get_ow_maps

List maps

- HTTP Method: `GET`
- Endpoint: `/ow/maps`

**Parameters**

| Name     | Type                                              | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverOwMaps](../models/FilterOverOwMaps.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverOwMaps](../models/RangeOverOwMaps.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                         | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverOwMaps](../models/SearchOverOwMaps.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                         | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                               | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[OwMap]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverOwMaps, RangeOverOwMaps, SearchOverOwMaps

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverOwMaps(
    game_mode=[
        "Assault"
    ],
    id_=[
        3
    ],
    name=[
        "cillum ut dolo"
    ],
    slug=[
        "sfw8ly"
    ]
)
range=RangeOverOwMaps(
    game_mode=[
        "Assault"
    ],
    id_=[
        6
    ],
    name=[
        "ipsum "
    ],
    slug=[
        "2"
    ]
)
sort=[
    ""
]
search=SearchOverOwMaps(
    game_mode="Assault",
    name="aliquip ex",
    slug="-e"
)
page=1

result = sdk.ow_maps.get_ow_maps(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_ow_maps_ow_map_id_or_slug

Get a single map by ID or by slug

- HTTP Method: `GET`
- Endpoint: `/ow/maps/{ow_map_id_or_slug}`

**Parameters**

| Name              | Type                                        | Required | Description      |
| :---------------- | :------------------------------------------ | :------- | :--------------- |
| ow_map_id_or_slug | [OwMapIdOrSlug](../models/OwMapIdOrSlug.md) | ✅       | A map ID or slug |

**Return Type**

`OwMap`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
ow_map_id_or_slug=2

result = sdk.ow_maps.get_ow_maps_ow_map_id_or_slug(ow_map_id_or_slug=ow_map_id_or_slug)

print(result)
```
