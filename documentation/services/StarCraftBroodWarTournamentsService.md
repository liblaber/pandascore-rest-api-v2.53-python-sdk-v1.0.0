# StarCraftBroodWarTournamentsService

A list of all methods in the `StarCraftBroodWarTournamentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                       | Description                                            |
| :-------------------------------------------------------------------------------------------- | :----------------------------------------------------- |
| [get_starcraft_brood_war_tournaments](#get_starcraft_brood_war_tournaments)                   | List tournaments for the StarCraft Brood War videogame |
| [get_starcraft_brood_war_tournaments_past](#get_starcraft_brood_war_tournaments_past)         | List past StarCraft Brood War tournaments              |
| [get_starcraft_brood_war_tournaments_running](#get_starcraft_brood_war_tournaments_running)   | List running StarCraft Brood War tournaments           |
| [get_starcraft_brood_war_tournaments_upcoming](#get_starcraft_brood_war_tournaments_upcoming) | List upcoming StarCraft Brood War tournaments          |

## get_starcraft_brood_war_tournaments

List tournaments for the StarCraft Brood War videogame

- HTTP Method: `GET`
- Endpoint: `/starcraft-brood-war/tournaments`

**Parameters**

| Name     | Type                                                                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraftBroodWarShortTournaments](../models/FilterOverStarcraftBroodWarShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraftBroodWarShortTournaments](../models/RangeOverStarcraftBroodWarShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraftBroodWarShortTournaments](../models/SearchOverStarcraftBroodWarShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraftBroodWarShortTournaments, RangeOverStarcraftBroodWarShortTournaments, SearchOverStarcraftBroodWarShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraftBroodWarShortTournaments(
    begin_at=[
        "aute do"
    ],
    detailed_stats=False,
    end_at=[
        "veni"
    ],
    has_bracket=False,
    id_=[
        4
    ],
    live_supported=False,
    modified_at=[
        "elit labore i"
    ],
    name=[
        "laboris aliquip"
    ],
    prizepool=[
        "ametlabore"
    ],
    serie_id=[
        8
    ],
    slug=[
        "l94-5k"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        2
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraftBroodWarShortTournaments(
    begin_at=[
        "sint l"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "cupidata"
    ],
    has_bracket=[
        True
    ],
    id_=[
        4
    ],
    modified_at=[
        "aliquip ut l"
    ],
    name=[
        "aliquip"
    ],
    prizepool=[
        "incididu"
    ],
    serie_id=[
        10
    ],
    slug=[
        "gc_hr"
    ],
    tier=[
        "a"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverStarcraftBroodWarShortTournaments(
    name="quiad veniam",
    prizepool="non sint ",
    slug="9",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.star_craft_brood_war_tournaments.get_starcraft_brood_war_tournaments(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_brood_war_tournaments_past

List past StarCraft Brood War tournaments

- HTTP Method: `GET`
- Endpoint: `/starcraft-brood-war/tournaments/past`

**Parameters**

| Name     | Type                                                                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraftBroodWarShortTournaments](../models/FilterOverStarcraftBroodWarShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraftBroodWarShortTournaments](../models/RangeOverStarcraftBroodWarShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraftBroodWarShortTournaments](../models/SearchOverStarcraftBroodWarShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraftBroodWarShortTournaments, RangeOverStarcraftBroodWarShortTournaments, SearchOverStarcraftBroodWarShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraftBroodWarShortTournaments(
    begin_at=[
        "aute do"
    ],
    detailed_stats=False,
    end_at=[
        "veni"
    ],
    has_bracket=False,
    id_=[
        4
    ],
    live_supported=False,
    modified_at=[
        "elit labore i"
    ],
    name=[
        "laboris aliquip"
    ],
    prizepool=[
        "ametlabore"
    ],
    serie_id=[
        8
    ],
    slug=[
        "l94-5k"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        2
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraftBroodWarShortTournaments(
    begin_at=[
        "sint l"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "cupidata"
    ],
    has_bracket=[
        True
    ],
    id_=[
        4
    ],
    modified_at=[
        "aliquip ut l"
    ],
    name=[
        "aliquip"
    ],
    prizepool=[
        "incididu"
    ],
    serie_id=[
        10
    ],
    slug=[
        "gc_hr"
    ],
    tier=[
        "a"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverStarcraftBroodWarShortTournaments(
    name="quiad veniam",
    prizepool="non sint ",
    slug="9",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.star_craft_brood_war_tournaments.get_starcraft_brood_war_tournaments_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_brood_war_tournaments_running

List running StarCraft Brood War tournaments

- HTTP Method: `GET`
- Endpoint: `/starcraft-brood-war/tournaments/running`

**Parameters**

| Name     | Type                                                                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraftBroodWarShortTournaments](../models/FilterOverStarcraftBroodWarShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraftBroodWarShortTournaments](../models/RangeOverStarcraftBroodWarShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraftBroodWarShortTournaments](../models/SearchOverStarcraftBroodWarShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraftBroodWarShortTournaments, RangeOverStarcraftBroodWarShortTournaments, SearchOverStarcraftBroodWarShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraftBroodWarShortTournaments(
    begin_at=[
        "aute do"
    ],
    detailed_stats=False,
    end_at=[
        "veni"
    ],
    has_bracket=False,
    id_=[
        4
    ],
    live_supported=False,
    modified_at=[
        "elit labore i"
    ],
    name=[
        "laboris aliquip"
    ],
    prizepool=[
        "ametlabore"
    ],
    serie_id=[
        8
    ],
    slug=[
        "l94-5k"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        2
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraftBroodWarShortTournaments(
    begin_at=[
        "sint l"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "cupidata"
    ],
    has_bracket=[
        True
    ],
    id_=[
        4
    ],
    modified_at=[
        "aliquip ut l"
    ],
    name=[
        "aliquip"
    ],
    prizepool=[
        "incididu"
    ],
    serie_id=[
        10
    ],
    slug=[
        "gc_hr"
    ],
    tier=[
        "a"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverStarcraftBroodWarShortTournaments(
    name="quiad veniam",
    prizepool="non sint ",
    slug="9",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.star_craft_brood_war_tournaments.get_starcraft_brood_war_tournaments_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_brood_war_tournaments_upcoming

List upcoming StarCraft Brood War tournaments

- HTTP Method: `GET`
- Endpoint: `/starcraft-brood-war/tournaments/upcoming`

**Parameters**

| Name     | Type                                                                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraftBroodWarShortTournaments](../models/FilterOverStarcraftBroodWarShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraftBroodWarShortTournaments](../models/RangeOverStarcraftBroodWarShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraftBroodWarShortTournaments](../models/SearchOverStarcraftBroodWarShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraftBroodWarShortTournaments, RangeOverStarcraftBroodWarShortTournaments, SearchOverStarcraftBroodWarShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraftBroodWarShortTournaments(
    begin_at=[
        "aute do"
    ],
    detailed_stats=False,
    end_at=[
        "veni"
    ],
    has_bracket=False,
    id_=[
        4
    ],
    live_supported=False,
    modified_at=[
        "elit labore i"
    ],
    name=[
        "laboris aliquip"
    ],
    prizepool=[
        "ametlabore"
    ],
    serie_id=[
        8
    ],
    slug=[
        "l94-5k"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        2
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraftBroodWarShortTournaments(
    begin_at=[
        "sint l"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "cupidata"
    ],
    has_bracket=[
        True
    ],
    id_=[
        4
    ],
    modified_at=[
        "aliquip ut l"
    ],
    name=[
        "aliquip"
    ],
    prizepool=[
        "incididu"
    ],
    serie_id=[
        10
    ],
    slug=[
        "gc_hr"
    ],
    tier=[
        "a"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverStarcraftBroodWarShortTournaments(
    name="quiad veniam",
    prizepool="non sint ",
    slug="9",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.star_craft_brood_war_tournaments.get_starcraft_brood_war_tournaments_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
