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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverAdditionIncidents, RangeOverAdditionIncidents

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverAdditionIncidents(
    id_=[
        7
    ],
    modified_at=[
        "dolor adipi"
    ],
    opponents_filled=True
)
range=RangeOverAdditionIncidents(
    id_=[
        7
    ],
    modified_at=[
        "exer"
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
    since="labore dolore",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverChangeIncidents, RangeOverChangeIncidents

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverChangeIncidents(
    id_=[
        7
    ],
    modified_at=[
        "a"
    ],
    opponents_filled=True
)
range=RangeOverChangeIncidents(
    id_=[
        7
    ],
    modified_at=[
        "sun"
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
    since="commodo ei",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverDeletionIncidents, RangeOverDeletionIncidents

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverDeletionIncidents(
    id_=[
        7
    ],
    modified_at=[
        "proid"
    ]
)
range=RangeOverDeletionIncidents(
    id_=[
        7
    ],
    modified_at=[
        "id"
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
    since="Ut ullamc",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverIncidents, RangeOverIncidents

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverIncidents(
    id_=[
        7
    ],
    modified_at=[
        "in culpa magna"
    ],
    opponents_filled=True
)
range=RangeOverIncidents(
    id_=[
        7
    ],
    modified_at=[
        "in ad veniam"
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
    since="ad sed ",
    videogame=videogame
)

print(result)
```
