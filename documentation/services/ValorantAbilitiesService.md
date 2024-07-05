# ValorantAbilitiesService

A list of all methods in the `ValorantAbilitiesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                   | Description                      |
| :---------------------------------------------------------------------------------------- | :------------------------------- |
| [get_valorant_abilities](#get_valorant_abilities)                                         | List abilities                   |
| [get_valorant_abilities_valorant_ability_id](#get_valorant_abilities_valorant_ability_id) | Get a Valorant ability by its ID |

## get_valorant_abilities

List abilities

- HTTP Method: `GET`
- Endpoint: `/valorant/abilities`

**Parameters**

| Name     | Type                                                                    | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantAbilities](../models/FilterOverValorantAbilities.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantAbilities](../models/RangeOverValorantAbilities.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantAbilities](../models/SearchOverValorantAbilities.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ValorantAbility]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverValorantAbilities, RangeOverValorantAbilities, SearchOverValorantAbilities

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverValorantAbilities(
    ability_type=[
        "ability_one"
    ],
    creds=[
        3.66
    ],
    id_=[
        6
    ],
    name=[
        "exercitatio"
    ],
    videogame_version=""
)
range=RangeOverValorantAbilities(
    ability_type=[
        "ability_one"
    ],
    creds=[
        4.4
    ],
    id_=[
        7
    ],
    name=[
        "Lorem id irure"
    ]
)
sort=[
    ""
]
search=SearchOverValorantAbilities(
    ability_type="ability_one",
    name="commodo ut dese"
)
page=1

result = sdk.valorant_abilities.get_valorant_abilities(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_valorant_abilities_valorant_ability_id

Get a Valorant ability by its ID

- HTTP Method: `GET`
- Endpoint: `/valorant/abilities/{valorant_ability_id}`

**Parameters**

| Name                | Type | Required | Description                |
| :------------------ | :--- | :------- | :------------------------- |
| valorant_ability_id | int  | ✅       | ID of the Valorant ability |

**Return Type**

`ValorantAbility`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.valorant_abilities.get_valorant_abilities_valorant_ability_id(valorant_ability_id=1)

print(result)
```
