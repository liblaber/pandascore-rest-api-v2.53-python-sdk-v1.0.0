# Dota2AbilitiesService

A list of all methods in the `Dota2AbilitiesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                       | Description                           |
| :-------------------------------------------------------------------------------------------- | :------------------------------------ |
| [get_dota2_abilities](#get_dota2_abilities)                                                   | List abilities                        |
| [get_dota2_abilities_dota2_ability_id_or_slug](#get_dota2_abilities_dota2_ability_id_or_slug) | Get a single ability by ID or by slug |

## get_dota2_abilities

List abilities

- HTTP Method: `GET`
- Endpoint: `/dota2/abilities`

**Parameters**

| Name     | Type                                                              | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverDota2Abilities](../models/FilterOverDota2Abilities.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverDota2Abilities](../models/RangeOverDota2Abilities.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                         | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverDota2Abilities](../models/SearchOverDota2Abilities.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                         | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                               | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Dota2Ability]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverDota2Abilities, RangeOverDota2Abilities, SearchOverDota2Abilities

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverDota2Abilities(
    id_=[
        3
    ],
    name=[
        "63bx_y-zh-"
    ]
)
range=RangeOverDota2Abilities(
    id_=[
        3
    ],
    name=[
        "k6a"
    ]
)
sort=[
    ""
]
search=SearchOverDota2Abilities(
    name="pqb1mi"
)
page=1

result = sdk.dota2_abilities.get_dota2_abilities(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_dota2_abilities_dota2_ability_id_or_slug

Get a single ability by ID or by slug

- HTTP Method: `GET`
- Endpoint: `/dota2/abilities/{dota2_ability_id_or_slug}`

**Parameters**

| Name                     | Type                                                      | Required | Description           |
| :----------------------- | :-------------------------------------------------------- | :------- | :-------------------- |
| dota2_ability_id_or_slug | [Dota2AbilityIdOrSlug](../models/Dota2AbilityIdOrSlug.md) | ✅       | An ability ID or slug |

**Return Type**

`Dota2Ability`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
dota2_ability_id_or_slug=8

result = sdk.dota2_abilities.get_dota2_abilities_dota2_ability_id_or_slug(dota2_ability_id_or_slug=dota2_ability_id_or_slug)

print(result)
```
