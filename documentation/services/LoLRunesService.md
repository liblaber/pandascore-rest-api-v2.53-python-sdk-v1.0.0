# LoLRunesService

A list of all methods in the `LoLRunesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                         | Description                                                                       |
| :---------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| [get_lol_runes_reforged](#get_lol_runes_reforged)                                               | List the latest version of League of Legends (reforged) runes                     |
| [get_lol_runes_reforged_paths](#get_lol_runes_reforged_paths)                                   | List the latest version of League of Legends (reforged) rune paths                |
| [get_lol_runes_reforged_paths_lol_rune_path_id](#get_lol_runes_reforged_paths_lol_rune_path_id) | Retrieve the latest version of a League of Legends (reforged) rune path by its ID |
| [get_lol_runes_reforged_lol_rune_reforged_id](#get_lol_runes_reforged_lol_rune_reforged_id)     | Retrieve the latest version of a League of Legends (reforged) rune by its ID      |

## get_lol_runes_reforged

List the latest version of League of Legends (reforged) runes

- HTTP Method: `GET`
- Endpoint: `/lol/runes-reforged`

**Parameters**

| Name     | Type                                                                  | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLRunesReforged](../models/FilterOverLoLRunesReforged.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLRunesReforged](../models/RangeOverLoLRunesReforged.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLRunesReforged](../models/SearchOverLoLRunesReforged.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[LoLRuneReforged]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLRunesReforged, RangeOverLoLRunesReforged, SearchOverLoLRunesReforged

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLoLRunesReforged(
    id_=[
        9
    ],
    name=[
        "cillum sint"
    ]
)
range=RangeOverLoLRunesReforged(
    id_=[
        6
    ],
    name=[
        "cillum do"
    ]
)
sort=[
    ""
]
search=SearchOverLoLRunesReforged(
    name="do irure "
)
page=1

result = sdk.lo_l_runes.get_lol_runes_reforged(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_runes_reforged_paths

List the latest version of League of Legends (reforged) rune paths

- HTTP Method: `GET`
- Endpoint: `/lol/runes-reforged-paths`

**Parameters**

| Name     | Type                                                          | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLRunePaths](../models/FilterOverLoLRunePaths.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLRunePaths](../models/RangeOverLoLRunePaths.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLRunePaths](../models/SearchOverLoLRunePaths.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[LoLRunePath]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLRunePaths, RangeOverLoLRunePaths, SearchOverLoLRunePaths

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLoLRunePaths(
    id_=[
        5
    ],
    name=[
        "occaecat esse"
    ],
    videogame_version=""
)
range=RangeOverLoLRunePaths(
    id_=[
        6
    ],
    name=[
        "ipsum nul"
    ]
)
sort=[
    ""
]
search=SearchOverLoLRunePaths(
    name="tempor eli"
)
page=1

result = sdk.lo_l_runes.get_lol_runes_reforged_paths(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_runes_reforged_paths_lol_rune_path_id

Retrieve the latest version of a League of Legends (reforged) rune path by its ID

- HTTP Method: `GET`
- Endpoint: `/lol/runes-reforged-paths/{lol_rune_path_id}`

**Parameters**

| Name             | Type | Required | Description             |
| :--------------- | :--- | :------- | :---------------------- |
| lol_rune_path_id | int  | ✅       | ID of the LoL rune path |

**Return Type**

`LoLRunePath`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.lo_l_runes.get_lol_runes_reforged_paths_lol_rune_path_id(lol_rune_path_id=5)

print(result)
```

## get_lol_runes_reforged_lol_rune_reforged_id

Retrieve the latest version of a League of Legends (reforged) rune by its ID

- HTTP Method: `GET`
- Endpoint: `/lol/runes-reforged/{lol_rune_reforged_id}`

**Parameters**

| Name                 | Type | Required | Description        |
| :------------------- | :--- | :------- | :----------------- |
| lol_rune_reforged_id | int  | ✅       | ID of the LoL rune |

**Return Type**

`LoLRuneReforged`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.lo_l_runes.get_lol_runes_reforged_lol_rune_reforged_id(lol_rune_reforged_id=7)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
