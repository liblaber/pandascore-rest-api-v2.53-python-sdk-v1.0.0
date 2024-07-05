# Dota2ItemsService

A list of all methods in the `Dota2ItemsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                         | Description                        |
| :------------------------------------------------------------------------------ | :--------------------------------- |
| [get_dota2_items](#get_dota2_items)                                             | List items                         |
| [get_dota2_items_dota2_item_id_or_slug](#get_dota2_items_dota2_item_id_or_slug) | Get a single item by ID or by slug |

## get_dota2_items

List items

- HTTP Method: `GET`
- Endpoint: `/dota2/items`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverDota2Items](../models/FilterOverDota2Items.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverDota2Items](../models/RangeOverDota2Items.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverDota2Items](../models/SearchOverDota2Items.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Dota2Item]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverDota2Items, RangeOverDota2Items, SearchOverDota2Items

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverDota2Items(
    id_=[
        4
    ],
    name=[
        "ol3"
    ]
)
range=RangeOverDota2Items(
    id_=[
        7
    ],
    name=[
        "hu7efqb5"
    ]
)
sort=[
    ""
]
search=SearchOverDota2Items(
    name="a"
)
page=1

result = sdk.dota2_items.get_dota2_items(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_dota2_items_dota2_item_id_or_slug

Get a single item by ID or by slug

- HTTP Method: `GET`
- Endpoint: `/dota2/items/{dota2_item_id_or_slug}`

**Parameters**

| Name                  | Type                                                | Required | Description        |
| :-------------------- | :-------------------------------------------------- | :------- | :----------------- |
| dota2_item_id_or_slug | [Dota2ItemIdOrSlug](../models/Dota2ItemIdOrSlug.md) | ✅       | An item ID or slug |

**Return Type**

`Dota2Item`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
dota2_item_id_or_slug=10

result = sdk.dota2_items.get_dota2_items_dota2_item_id_or_slug(dota2_item_id_or_slug=dota2_item_id_or_slug)

print(result)
```
