# IncidentsService

A list of all methods in the `IncidentsService` service. Click on the method name to view detailed information about that method.

| Methods                         | Description                                                                                                                                                   |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [get_additions](#get_additions) | Get the latest additions. <br/> <br/>This endpoint only shows unchanged objects.                                                                              |
| [get_changes](#get_changes)     | Get the latest updates. <br/> <br/>This endpoint only provides the latest change for an object. It does not keep track of previous changes.                   |
| [get_deletions](#get_deletions) | Get the latest deleted documents                                                                                                                              |
| [get_incidents](#get_incidents) | Get the latest updates and additions. <br/> <br/>This endpoint only provides the latest incident for an object. It does not keep track of previous incidents. |

## get_additions

Get the latest additions. <br/> <br/>This endpoint only shows unchanged objects.

- HTTP Method: `GET`
- Endpoint: `/additions`

**Parameters**

| Name      | Type                                                                    | Required | Description                                                                                                                                         |
| :-------- | :---------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter    | [FilterOverAdditionIncidents](../models/FilterOverAdditionIncidents.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range     | [RangeOverAdditionIncidents](../models/RangeOverAdditionIncidents.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort      | List[any]                                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| page      | [Page](../models/Page.md)                                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page  | int                                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |
| type\_    | List[any]                                                               | ❌       | Filter by result type(s)                                                                                                                            |
| since     | str                                                                     | ❌       | Filter out older results                                                                                                                            |
| videogame | [List[VideogameIdOrSlug]](../models/VideogameIdOrSlug.md)               | ❌       | Filter by videogame(s)                                                                                                                              |

**Return Type**

`List[NonDeletionIncident]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverAdditionIncidents, RangeOverAdditionIncidents

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverAdditionIncidents(
    id_=[
        9
    ],
    modified_at=[
        "labore nul"
    ],
    opponents_filled=False
)
range=RangeOverAdditionIncidents(
    id_=[
        9
    ],
    modified_at=[
        "id a"
    ]
)
sort=[
    ""
]
page=1
type_=[
    ""
]
videogame=[
    1
]

result = sdk.incidents.get_additions(
    filter=filter,
    range=range,
    sort=sort,
    page=page,
    per_page=50,
    type_=type_,
    since="mollit magna no",
    videogame=videogame
)

print(result)
```

## get_changes

Get the latest updates. <br/> <br/>This endpoint only provides the latest change for an object. It does not keep track of previous changes.

- HTTP Method: `GET`
- Endpoint: `/changes`

**Parameters**

| Name      | Type                                                                | Required | Description                                                                                                                                         |
| :-------- | :------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter    | [FilterOverChangeIncidents](../models/FilterOverChangeIncidents.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range     | [RangeOverChangeIncidents](../models/RangeOverChangeIncidents.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort      | List[any]                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| page      | [Page](../models/Page.md)                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page  | int                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |
| type\_    | List[any]                                                           | ❌       | Filter by result type(s)                                                                                                                            |
| since     | str                                                                 | ❌       | Filter out older results                                                                                                                            |
| videogame | [List[VideogameIdOrSlug]](../models/VideogameIdOrSlug.md)           | ❌       | Filter by videogame(s)                                                                                                                              |

**Return Type**

`List[Incident]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverChangeIncidents, RangeOverChangeIncidents

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverChangeIncidents(
    id_=[
        9
    ],
    modified_at=[
        "id eiusmod"
    ],
    opponents_filled=True
)
range=RangeOverChangeIncidents(
    id_=[
        9
    ],
    modified_at=[
        "adipisici"
    ]
)
sort=[
    ""
]
page=1
type_=[
    ""
]
videogame=[
    1
]

result = sdk.incidents.get_changes(
    filter=filter,
    range=range,
    sort=sort,
    page=page,
    per_page=50,
    type_=type_,
    since="labori",
    videogame=videogame
)

print(result)
```

## get_deletions

Get the latest deleted documents

- HTTP Method: `GET`
- Endpoint: `/deletions`

**Parameters**

| Name      | Type                                                                    | Required | Description                                                                                                                                         |
| :-------- | :---------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter    | [FilterOverDeletionIncidents](../models/FilterOverDeletionIncidents.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range     | [RangeOverDeletionIncidents](../models/RangeOverDeletionIncidents.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort      | List[any]                                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| page      | [Page](../models/Page.md)                                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page  | int                                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |
| type\_    | List[any]                                                               | ❌       | Filter by result type(s)                                                                                                                            |
| since     | str                                                                     | ❌       | Filter out older results                                                                                                                            |
| videogame | [List[VideogameIdOrSlug]](../models/VideogameIdOrSlug.md)               | ❌       | Filter by videogame(s)                                                                                                                              |

**Return Type**

`List[DeletionIncident]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverDeletionIncidents, RangeOverDeletionIncidents

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverDeletionIncidents(
    id_=[
        9
    ],
    modified_at=[
        "voluptate cu"
    ]
)
range=RangeOverDeletionIncidents(
    id_=[
        9
    ],
    modified_at=[
        "reprehenderit o"
    ]
)
sort=[
    ""
]
page=1
type_=[
    ""
]
videogame=[
    1
]

result = sdk.incidents.get_deletions(
    filter=filter,
    range=range,
    sort=sort,
    page=page,
    per_page=50,
    type_=type_,
    since="voluptat",
    videogame=videogame
)

print(result)
```

## get_incidents

Get the latest updates and additions. <br/> <br/>This endpoint only provides the latest incident for an object. It does not keep track of previous incidents.

- HTTP Method: `GET`
- Endpoint: `/incidents`

**Parameters**

| Name      | Type                                                      | Required | Description                                                                                                                                         |
| :-------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter    | [FilterOverIncidents](../models/FilterOverIncidents.md)   | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range     | [RangeOverIncidents](../models/RangeOverIncidents.md)     | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort      | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| page      | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page  | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |
| type\_    | List[any]                                                 | ❌       | Filter by result type(s)                                                                                                                            |
| since     | str                                                       | ❌       | Filter out older results                                                                                                                            |
| videogame | [List[VideogameIdOrSlug]](../models/VideogameIdOrSlug.md) | ❌       | Filter by videogame(s)                                                                                                                              |

**Return Type**

`List[Incident]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverIncidents, RangeOverIncidents

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverIncidents(
    id_=[
        9
    ],
    modified_at=[
        "eu"
    ],
    opponents_filled=True
)
range=RangeOverIncidents(
    id_=[
        9
    ],
    modified_at=[
        "id offici"
    ]
)
sort=[
    ""
]
page=1
type_=[
    ""
]
videogame=[
    1
]

result = sdk.incidents.get_incidents(
    filter=filter,
    range=range,
    sort=sort,
    page=page,
    per_page=50,
    type_=type_,
    since="dolore adip",
    videogame=videogame
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
