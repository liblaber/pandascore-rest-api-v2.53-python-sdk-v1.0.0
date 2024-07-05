# Dota2HeroesService

A list of all methods in the `Dota2HeroesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                           | Description                        |
| :-------------------------------------------------------------------------------- | :--------------------------------- |
| [get_dota2_heroes](#get_dota2_heroes)                                             | List heroes                        |
| [get_dota2_heroes_dota2_hero_id_or_slug](#get_dota2_heroes_dota2_hero_id_or_slug) | Get a single hero by ID or by slug |

## get_dota2_heroes

List heroes

- HTTP Method: `GET`
- Endpoint: `/dota2/heroes`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverDota2Heroes](../models/FilterOverDota2Heroes.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverDota2Heroes](../models/RangeOverDota2Heroes.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverDota2Heroes](../models/SearchOverDota2Heroes.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Dota2Hero]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverDota2Heroes, RangeOverDota2Heroes, SearchOverDota2Heroes

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverDota2Heroes(
    id_=[
        1
    ],
    localized_name=[
        "cillum repreh"
    ],
    name=[
        "wg97x2n"
    ]
)
range=RangeOverDota2Heroes(
    id_=[
        10
    ],
    localized_name=[
        "enima"
    ],
    name=[
        "ts-ls"
    ]
)
sort=[
    ""
]
search=SearchOverDota2Heroes(
    localized_name="incididunt eu",
    name="4"
)
page=1

result = sdk.dota2_heroes.get_dota2_heroes(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_dota2_heroes_dota2_hero_id_or_slug

Get a single hero by ID or by slug

- HTTP Method: `GET`
- Endpoint: `/dota2/heroes/{dota2_hero_id_or_slug}`

**Parameters**

| Name                  | Type                                                | Required | Description       |
| :-------------------- | :-------------------------------------------------- | :------- | :---------------- |
| dota2_hero_id_or_slug | [Dota2HeroIdOrSlug](../models/Dota2HeroIdOrSlug.md) | ✅       | A hero ID or slug |

**Return Type**

`Dota2Hero`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
dota2_hero_id_or_slug=5

result = sdk.dota2_heroes.get_dota2_heroes_dota2_hero_id_or_slug(dota2_hero_id_or_slug=dota2_hero_id_or_slug)

print(result)
```
