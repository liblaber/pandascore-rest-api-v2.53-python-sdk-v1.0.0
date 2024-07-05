# RlMatchesService

A list of all methods in the `RlMatchesService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description                                  |
| :-------------------------------------------------- | :------------------------------------------- |
| [get_rl_matches](#get_rl_matches)                   | List matches for the Rocket League videogame |
| [get_rl_matches_past](#get_rl_matches_past)         | List past Rocket League matches              |
| [get_rl_matches_running](#get_rl_matches_running)   | List running Rocket League matches           |
| [get_rl_matches_upcoming](#get_rl_matches_upcoming) | List upcoming Rocket League matches          |

## get_rl_matches

List matches for the Rocket League videogame

- HTTP Method: `GET`
- Endpoint: `/rl/matches`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverRlMatches](../models/FilterOverRlMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverRlMatches](../models/RangeOverRlMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverRlMatches](../models/SearchOverRlMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverRlMatches, RangeOverRlMatches, SearchOverRlMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverRlMatches(
    begin_at=[
        "in exer"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "elit "
    ],
    finished=False,
    forfeit=False,
    future=True,
    id_=[
        1
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "labo"
    ],
    name=[
        "sit in"
    ],
    not_started=False,
    number_of_games=[
        3
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=False,
    scheduled_at=[
        "in"
    ],
    serie_id=[
        2
    ],
    slug=[
        "7Z"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        1
    ],
    videogame_version=[
        "0.66864.31104119"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverRlMatches(
    begin_at=[
        "conse"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "voluptate "
    ],
    forfeit=[
        True
    ],
    id_=[
        10
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "si"
    ],
    name=[
        "occaecat"
    ],
    number_of_games=[
        4
    ],
    scheduled_at=[
        "E"
    ],
    slug=[
        "I-iXslS3c"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        8
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
search=SearchOverRlMatches(
    match_type="all_games_played",
    name="sint cupid",
    slug="hXiBh9rdf1",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.rl_matches.get_rl_matches(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_rl_matches_past

List past Rocket League matches

- HTTP Method: `GET`
- Endpoint: `/rl/matches/past`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverRlMatches](../models/FilterOverRlMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverRlMatches](../models/RangeOverRlMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverRlMatches](../models/SearchOverRlMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverRlMatches, RangeOverRlMatches, SearchOverRlMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverRlMatches(
    begin_at=[
        "in exer"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "elit "
    ],
    finished=False,
    forfeit=False,
    future=True,
    id_=[
        1
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "labo"
    ],
    name=[
        "sit in"
    ],
    not_started=False,
    number_of_games=[
        3
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=False,
    scheduled_at=[
        "in"
    ],
    serie_id=[
        2
    ],
    slug=[
        "7Z"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        1
    ],
    videogame_version=[
        "0.66864.31104119"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverRlMatches(
    begin_at=[
        "conse"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "voluptate "
    ],
    forfeit=[
        True
    ],
    id_=[
        10
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "si"
    ],
    name=[
        "occaecat"
    ],
    number_of_games=[
        4
    ],
    scheduled_at=[
        "E"
    ],
    slug=[
        "I-iXslS3c"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        8
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
search=SearchOverRlMatches(
    match_type="all_games_played",
    name="sint cupid",
    slug="hXiBh9rdf1",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.rl_matches.get_rl_matches_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_rl_matches_running

List running Rocket League matches

- HTTP Method: `GET`
- Endpoint: `/rl/matches/running`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverRlMatches](../models/FilterOverRlMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverRlMatches](../models/RangeOverRlMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverRlMatches](../models/SearchOverRlMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverRlMatches, RangeOverRlMatches, SearchOverRlMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverRlMatches(
    begin_at=[
        "in exer"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "elit "
    ],
    finished=False,
    forfeit=False,
    future=True,
    id_=[
        1
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "labo"
    ],
    name=[
        "sit in"
    ],
    not_started=False,
    number_of_games=[
        3
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=False,
    scheduled_at=[
        "in"
    ],
    serie_id=[
        2
    ],
    slug=[
        "7Z"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        1
    ],
    videogame_version=[
        "0.66864.31104119"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverRlMatches(
    begin_at=[
        "conse"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "voluptate "
    ],
    forfeit=[
        True
    ],
    id_=[
        10
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "si"
    ],
    name=[
        "occaecat"
    ],
    number_of_games=[
        4
    ],
    scheduled_at=[
        "E"
    ],
    slug=[
        "I-iXslS3c"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        8
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
search=SearchOverRlMatches(
    match_type="all_games_played",
    name="sint cupid",
    slug="hXiBh9rdf1",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.rl_matches.get_rl_matches_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_rl_matches_upcoming

List upcoming Rocket League matches

- HTTP Method: `GET`
- Endpoint: `/rl/matches/upcoming`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverRlMatches](../models/FilterOverRlMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverRlMatches](../models/RangeOverRlMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverRlMatches](../models/SearchOverRlMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverRlMatches, RangeOverRlMatches, SearchOverRlMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverRlMatches(
    begin_at=[
        "in exer"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "elit "
    ],
    finished=False,
    forfeit=False,
    future=True,
    id_=[
        1
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "labo"
    ],
    name=[
        "sit in"
    ],
    not_started=False,
    number_of_games=[
        3
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=False,
    scheduled_at=[
        "in"
    ],
    serie_id=[
        2
    ],
    slug=[
        "7Z"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        1
    ],
    videogame_version=[
        "0.66864.31104119"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverRlMatches(
    begin_at=[
        "conse"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "voluptate "
    ],
    forfeit=[
        True
    ],
    id_=[
        10
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "si"
    ],
    name=[
        "occaecat"
    ],
    number_of_games=[
        4
    ],
    scheduled_at=[
        "E"
    ],
    slug=[
        "I-iXslS3c"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        8
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
search=SearchOverRlMatches(
    match_type="all_games_played",
    name="sint cupid",
    slug="hXiBh9rdf1",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.rl_matches.get_rl_matches_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
