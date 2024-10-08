# CounterStrikeMapsService

A list of all methods in the `CounterStrikeMapsService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                       |
| :------------------------------------------------------ | :-------------------------------- |
| [get_csgo_maps](#get_csgo_maps)                         | List maps                         |
| [get_csgo_maps_csgo_map_id](#get_csgo_maps_csgo_map_id) | Get a single map by ID or by slug |

## get_csgo_maps

List maps

- HTTP Method: `GET`
- Endpoint: `/csgo/maps`

**Parameters**

| Name     | Type                                                  | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCsgoMaps](../models/FilterOverCsgoMaps.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCsgoMaps](../models/RangeOverCsgoMaps.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCsgoMaps](../models/SearchOverCsgoMaps.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[CsgoMap]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCsgoMaps, RangeOverCsgoMaps, SearchOverCsgoMaps

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCsgoMaps(
    id_=[
        1
    ],
    name=[
        "quiminim in de"
    ],
    slug=[
        "l27p"
    ]
)
range=RangeOverCsgoMaps(
    id_=[
        9
    ],
    name=[
        "cupida"
    ],
    slug=[
        "k-4qt"
    ]
)
sort=[
    ""
]
search=SearchOverCsgoMaps(
    name="fugiat culpa",
    slug="sw_b"
)
page=1

result = sdk.counter_strike_maps.get_csgo_maps(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_csgo_maps_csgo_map_id

Get a single map by ID or by slug

- HTTP Method: `GET`
- Endpoint: `/csgo/maps/{csgo_map_id}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| csgo_map_id | int  | ✅       | A map ID    |

**Return Type**

`CsgoMap`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.counter_strike_maps.get_csgo_maps_csgo_map_id(csgo_map_id=2)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
