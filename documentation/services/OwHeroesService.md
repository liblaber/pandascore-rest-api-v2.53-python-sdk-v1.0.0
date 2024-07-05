# OwHeroesService

A list of all methods in the `OwHeroesService` service. Click on the method name to view detailed information about that method.

| Methods                                                               | Description                        |
| :-------------------------------------------------------------------- | :--------------------------------- |
| [get_ow_heroes](#get_ow_heroes)                                       | List heroes                        |
| [get_ow_heroes_ow_hero_id_or_slug](#get_ow_heroes_ow_hero_id_or_slug) | Get a single hero by ID or by slug |

## get_ow_heroes

List heroes

- HTTP Method: `GET`
- Endpoint: `/ow/heroes`

**Parameters**

| Name     | Type                                                  | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverOwHeroes](../models/FilterOverOwHeroes.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverOwHeroes](../models/RangeOverOwHeroes.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverOwHeroes](../models/SearchOverOwHeroes.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[OwHero]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverOwHeroes, RangeOverOwHeroes, SearchOverOwHeroes

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverOwHeroes(
    difficulty=[
        6
    ],
    id_=[
        8
    ],
    name=[
        "utExcepteur i"
    ],
    real_name=[
        "aute Ut"
    ],
    role=[
        "damage"
    ],
    slug=[
        "mbq"
    ]
)
range=RangeOverOwHeroes(
    difficulty=[
        4
    ],
    id_=[
        5
    ],
    name=[
        "qui officia"
    ],
    real_name=[
        "esseex"
    ],
    role=[
        "damage"
    ],
    slug=[
        "122p9"
    ]
)
sort=[
    ""
]
search=SearchOverOwHeroes(
    name="Utea et ir",
    real_name="amet ad eu moll",
    role="damage",
    slug="osxn-9qxvk"
)
page=1

result = sdk.ow_heroes.get_ow_heroes(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_ow_heroes_ow_hero_id_or_slug

Get a single hero by ID or by slug

- HTTP Method: `GET`
- Endpoint: `/ow/heroes/{ow_hero_id_or_slug}`

**Parameters**

| Name               | Type                                          | Required | Description       |
| :----------------- | :-------------------------------------------- | :------- | :---------------- |
| ow_hero_id_or_slug | [OwHeroIdOrSlug](../models/OwHeroIdOrSlug.md) | ✅       | A hero ID or slug |

**Return Type**

`OwHero`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
ow_hero_id_or_slug=8

result = sdk.ow_heroes.get_ow_heroes_ow_hero_id_or_slug(ow_hero_id_or_slug=ow_hero_id_or_slug)

print(result)
```
