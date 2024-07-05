# ValorantMapsService

A list of all methods in the `ValorantMapsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                  |
| :---------------------------------------------------------------------- | :--------------------------- |
| [get_valorant_maps](#get_valorant_maps)                                 | List maps                    |
| [get_valorant_maps_valorant_map_id](#get_valorant_maps_valorant_map_id) | Get a Valorant map by its ID |

## get_valorant_maps

List maps

- HTTP Method: `GET`
- Endpoint: `/valorant/maps`

**Parameters**

| Name     | Type                                                          | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantMaps](../models/FilterOverValorantMaps.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantMaps](../models/RangeOverValorantMaps.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantMaps](../models/SearchOverValorantMaps.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ValorantMap]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverValorantMaps, RangeOverValorantMaps, SearchOverValorantMaps

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverValorantMaps(
    id_=[
        9
    ],
    name=[
        "Excepteur ip"
    ],
    slug=[
        "h"
    ],
    videogame_version=""
)
range=RangeOverValorantMaps(
    id_=[
        7
    ],
    name=[
        "nulla in ex es"
    ],
    slug=[
        "ljiiqk"
    ]
)
sort=[
    ""
]
search=SearchOverValorantMaps(
    name="et ut anim e",
    slug="u8rdc"
)
page=1

result = sdk.valorant_maps.get_valorant_maps(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_valorant_maps_valorant_map_id

Get a Valorant map by its ID

- HTTP Method: `GET`
- Endpoint: `/valorant/maps/{valorant_map_id}`

**Parameters**

| Name            | Type | Required | Description            |
| :-------------- | :--- | :------- | :--------------------- |
| valorant_map_id | int  | ✅       | ID of the Valorant map |

**Return Type**

`ValorantMap`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.valorant_maps.get_valorant_maps_valorant_map_id(valorant_map_id=7)

print(result)
```
