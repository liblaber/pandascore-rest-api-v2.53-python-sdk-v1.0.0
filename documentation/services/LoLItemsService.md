# LoLItemsService

A list of all methods in the `LoLItemsService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                        |
| :------------------------------------------------------ | :--------------------------------- |
| [get_lol_items](#get_lol_items)                         | List items                         |
| [get_lol_items_lol_item_id](#get_lol_items_lol_item_id) | Get a single item by ID or by slug |

## get_lol_items

List items

- HTTP Method: `GET`
- Endpoint: `/lol/items`

**Parameters**

| Name     | Type                                                  | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLItems](../models/FilterOverLoLItems.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLItems](../models/RangeOverLoLItems.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLItems](../models/SearchOverLoLItems.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[LoLItem]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLItems, RangeOverLoLItems, SearchOverLoLItems

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLoLItems(
    flat_armor_mod=[
        5
    ],
    flat_crit_chance_mod=[
        1
    ],
    flat_hp_pool_mod=[
        1
    ],
    flat_hp_regen_mod=[
        7
    ],
    flat_magic_damage_mod=[
        8
    ],
    flat_movement_speed_mod=[
        2
    ],
    flat_mp_pool_mod=[
        6
    ],
    flat_mp_regen_mod=[
        8
    ],
    flat_physical_damage_mod=[
        6
    ],
    flat_spell_block_mod=[
        3
    ],
    gold_base=[
        5
    ],
    gold_purchasable=False,
    gold_sell=[
        7
    ],
    gold_total=[
        4
    ],
    id_=[
        4
    ],
    name=[
        "eiusmod"
    ],
    percent_attack_speed_mod=[
        2
    ],
    percent_life_steal_mod=[
        9
    ],
    percent_movement_speed_mod=[
        10
    ],
    trinket=False,
    videogame_version=""
)
range=RangeOverLoLItems(
    flat_armor_mod=[
        8
    ],
    flat_crit_chance_mod=[
        10
    ],
    flat_hp_pool_mod=[
        10
    ],
    flat_hp_regen_mod=[
        8
    ],
    flat_magic_damage_mod=[
        10
    ],
    flat_movement_speed_mod=[
        3
    ],
    flat_mp_pool_mod=[
        9
    ],
    flat_mp_regen_mod=[
        2
    ],
    flat_physical_damage_mod=[
        10
    ],
    flat_spell_block_mod=[
        6
    ],
    gold_base=[
        10
    ],
    gold_purchasable=[
        False
    ],
    gold_sell=[
        3
    ],
    gold_total=[
        6
    ],
    id_=[
        5
    ],
    name=[
        "in aliquip"
    ],
    percent_attack_speed_mod=[
        8
    ],
    percent_life_steal_mod=[
        8
    ],
    percent_movement_speed_mod=[
        1
    ]
)
sort=[
    ""
]
search=SearchOverLoLItems(
    name="adipis"
)
page=1

result = sdk.lo_l_items.get_lol_items(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_items_lol_item_id

Get a single item by ID or by slug

- HTTP Method: `GET`
- Endpoint: `/lol/items/{lol_item_id}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| lol_item_id | int  | ✅       | An item ID  |

**Return Type**

`LoLItem`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.lo_l_items.get_lol_items_lol_item_id(lol_item_id=3)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
