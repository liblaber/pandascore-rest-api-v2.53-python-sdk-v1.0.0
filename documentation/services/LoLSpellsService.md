# LoLSpellsService

A list of all methods in the `LoLSpellsService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description              |
| :---------------------------------------------------------- | :----------------------- |
| [get_lol_spells](#get_lol_spells)                           | List spells              |
| [get_lol_spells_lol_spell_id](#get_lol_spells_lol_spell_id) | Get a single spell by ID |

## get_lol_spells

List spells

- HTTP Method: `GET`
- Endpoint: `/lol/spells`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLSpells](../models/FilterOverLoLSpells.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLSpells](../models/RangeOverLoLSpells.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLSpells](../models/SearchOverLoLSpells.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[LoLSpell]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLoLSpells, RangeOverLoLSpells, SearchOverLoLSpells

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLoLSpells(
    id_=[
        1
    ],
    name=[
        "elit a"
    ],
    videogame_version=""
)
range=RangeOverLoLSpells(
    id_=[
        10
    ],
    name=[
        "reprehe"
    ]
)
sort=[
    ""
]
search=SearchOverLoLSpells(
    name="nulla"
)
page=1

result = sdk.lo_l_spells.get_lol_spells(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_spells_lol_spell_id

Get a single spell by ID

- HTTP Method: `GET`
- Endpoint: `/lol/spells/{lol_spell_id}`

**Parameters**

| Name         | Type | Required | Description |
| :----------- | :--- | :------- | :---------- |
| lol_spell_id | int  | ✅       | A spell ID  |

**Return Type**

`LoLSpell`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.lo_l_spells.get_lol_spells_lol_spell_id(lol_spell_id=6)

print(result)
```
