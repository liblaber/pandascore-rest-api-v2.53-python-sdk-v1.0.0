# CounterStrikeWeaponsService

A list of all methods in the `CounterStrikeWeaponsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                             | Description                          |
| :---------------------------------------------------------------------------------- | :----------------------------------- |
| [get_csgo_weapons](#get_csgo_weapons)                                               | List weapons                         |
| [get_csgo_weapons_csgo_weapon_id_or_slug](#get_csgo_weapons_csgo_weapon_id_or_slug) | Get a single weapon by ID or by slug |

## get_csgo_weapons

List weapons

- HTTP Method: `GET`
- Endpoint: `/csgo/weapons`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCsgoWeapons](../models/FilterOverCsgoWeapons.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCsgoWeapons](../models/RangeOverCsgoWeapons.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCsgoWeapons](../models/SearchOverCsgoWeapons.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[CsgoWeapon]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCsgoWeapons, RangeOverCsgoWeapons, SearchOverCsgoWeapons

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCsgoWeapons(
    ammo_clip_max=[
        0
    ],
    ammo_max=[
        7
    ],
    cost=[
        10
    ],
    id_=[
        2
    ],
    kill_reward=[
        1
    ],
    kind=[
        "grenade"
    ],
    name=[
        "eanon cons"
    ],
    slug=[
        "wr1b"
    ]
)
range=RangeOverCsgoWeapons(
    ammo_clip_max=[
        4
    ],
    ammo_max=[
        8
    ],
    cost=[
        8
    ],
    id_=[
        10
    ],
    kill_reward=[
        8
    ],
    kind=[
        "grenade"
    ],
    name=[
        "enim sint"
    ],
    slug=[
        "y3-qnbp3n0"
    ]
)
sort=[
    ""
]
search=SearchOverCsgoWeapons(
    kind="grenade",
    name="amet nu",
    slug="4r2x1ntn5qv"
)
page=1

result = sdk.counter_strike_weapons.get_csgo_weapons(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_csgo_weapons_csgo_weapon_id_or_slug

Get a single weapon by ID or by slug

- HTTP Method: `GET`
- Endpoint: `/csgo/weapons/{csgo_weapon_id_or_slug}`

**Parameters**

| Name                   | Type                                                  | Required | Description         |
| :--------------------- | :---------------------------------------------------- | :------- | :------------------ |
| csgo_weapon_id_or_slug | [CsgoWeaponIdOrSlug](../models/CsgoWeaponIdOrSlug.md) | ✅       | A weapon ID or slug |

**Return Type**

`CsgoWeapon`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
csgo_weapon_id_or_slug=2

result = sdk.counter_strike_weapons.get_csgo_weapons_csgo_weapon_id_or_slug(csgo_weapon_id_or_slug=csgo_weapon_id_or_slug)

print(result)
```
