# LoLChampionsService

A list of all methods in the `LoLChampionsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                            |
| :---------------------------------------------------------------------- | :------------------------------------- |
| [get_lol_champions](#get_lol_champions)                                 | List champions                         |
| [get_lol_champions_lol_champion_id](#get_lol_champions_lol_champion_id) | Get a single champion by ID or by slug |

## get_lol_champions

List champions

- HTTP Method: `GET`
- Endpoint: `/lol/champions`

**Parameters**

| Name     | Type                                                          | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLChampions](../models/FilterOverLoLChampions.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLChampions](../models/RangeOverLoLChampions.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLChampions](../models/SearchOverLoLChampions.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[LoLChampion]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLoLChampions, RangeOverLoLChampions, SearchOverLoLChampions

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLoLChampions(
    armor=[
        7.68
    ],
    armorperlevel=[
        4.8
    ],
    attackdamage=[
        3.34
    ],
    attackdamageperlevel=[
        2.01
    ],
    attackrange=[
        0.89
    ],
    attackspeedoffset=[
        6.99
    ],
    attackspeedperlevel=[
        5.43
    ],
    crit=[
        0.52
    ],
    critperlevel=[
        4.92
    ],
    hp=[
        0.5
    ],
    hpperlevel=[
        6.91
    ],
    hpregen=[
        7.45
    ],
    hpregenperlevel=[
        7.11
    ],
    id_=[
        3
    ],
    movespeed=[
        3.83
    ],
    mp=[
        0.29
    ],
    mpperlevel=[
        1.28
    ],
    mpregen=[
        2.66
    ],
    mpregenperlevel=[
        3.8
    ],
    name=[
        "autein"
    ],
    spellblock=[
        7.64
    ],
    spellblockperlevel=[
        7.81
    ],
    videogame_version=""
)
range=RangeOverLoLChampions(
    armor=[
        8.54
    ],
    armorperlevel=[
        4.6
    ],
    attackdamage=[
        6.29
    ],
    attackdamageperlevel=[
        8.85
    ],
    attackrange=[
        1.62
    ],
    attackspeedoffset=[
        4.59
    ],
    attackspeedperlevel=[
        9.44
    ],
    crit=[
        8.99
    ],
    critperlevel=[
        7.67
    ],
    hp=[
        4.1
    ],
    hpperlevel=[
        5.62
    ],
    hpregen=[
        1.56
    ],
    hpregenperlevel=[
        2.93
    ],
    id_=[
        8
    ],
    movespeed=[
        6.73
    ],
    mp=[
        0.42
    ],
    mpperlevel=[
        1.02
    ],
    mpregen=[
        3.93
    ],
    mpregenperlevel=[
        1.14
    ],
    name=[
        "minim dolo"
    ],
    spellblock=[
        5.15
    ],
    spellblockperlevel=[
        2.78
    ]
)
sort=[
    ""
]
search=SearchOverLoLChampions(
    name="ex sint"
)
page=1

result = sdk.lo_l_champions.get_lol_champions(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_champions_lol_champion_id

Get a single champion by ID or by slug

- HTTP Method: `GET`
- Endpoint: `/lol/champions/{lol_champion_id}`

**Parameters**

| Name            | Type | Required | Description   |
| :-------------- | :--- | :------- | :------------ |
| lol_champion_id | int  | ✅       | A champion ID |

**Return Type**

`LoLChampion`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.lo_l_champions.get_lol_champions_lol_champion_id(lol_champion_id=7)

print(result)
```
