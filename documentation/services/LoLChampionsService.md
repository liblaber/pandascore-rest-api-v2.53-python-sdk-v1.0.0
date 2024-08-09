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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLChampions, RangeOverLoLChampions, SearchOverLoLChampions

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLoLChampions(
    armor=[
        5.35
    ],
    armorperlevel=[
        2.85
    ],
    attackdamage=[
        4.76
    ],
    attackdamageperlevel=[
        9.24
    ],
    attackrange=[
        3.35
    ],
    attackspeedoffset=[
        5.17
    ],
    attackspeedperlevel=[
        9.6
    ],
    crit=[
        6.73
    ],
    critperlevel=[
        3.81
    ],
    hp=[
        5.6
    ],
    hpperlevel=[
        7.71
    ],
    hpregen=[
        0.96
    ],
    hpregenperlevel=[
        6.1
    ],
    id_=[
        8
    ],
    movespeed=[
        7.47
    ],
    mp=[
        5.77
    ],
    mpperlevel=[
        8.02
    ],
    mpregen=[
        9.83
    ],
    mpregenperlevel=[
        0.84
    ],
    name=[
        "et labore"
    ],
    spellblock=[
        1.91
    ],
    spellblockperlevel=[
        6.83
    ],
    videogame_version=""
)
range=RangeOverLoLChampions(
    armor=[
        6.96
    ],
    armorperlevel=[
        9.76
    ],
    attackdamage=[
        7.04
    ],
    attackdamageperlevel=[
        1.33
    ],
    attackrange=[
        3.27
    ],
    attackspeedoffset=[
        2.7
    ],
    attackspeedperlevel=[
        6.48
    ],
    crit=[
        2.64
    ],
    critperlevel=[
        3.83
    ],
    hp=[
        2.77
    ],
    hpperlevel=[
        5.48
    ],
    hpregen=[
        2.16
    ],
    hpregenperlevel=[
        4.44
    ],
    id_=[
        7
    ],
    movespeed=[
        9.89
    ],
    mp=[
        6.32
    ],
    mpperlevel=[
        0.37
    ],
    mpregen=[
        0.64
    ],
    mpregenperlevel=[
        2.8
    ],
    name=[
        "sit ipsum nostr"
    ],
    spellblock=[
        5.29
    ],
    spellblockperlevel=[
        4.75
    ]
)
sort=[
    ""
]
search=SearchOverLoLChampions(
    name="eu ex"
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
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.lo_l_champions.get_lol_champions_lol_champion_id(lol_champion_id=5)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
