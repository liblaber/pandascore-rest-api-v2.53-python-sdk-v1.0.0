# TeamsService

A list of all methods in the `TeamsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                         | Description                                          |
| :------------------------------------------------------------------------------ | :--------------------------------------------------- |
| [get_teams](#get_teams)                                                         | List teams                                           |
| [get_teams_team_id_or_slug](#get_teams_team_id_or_slug)                         | Get a single team by ID or by slug                   |
| [get_teams_team_id_or_slug_leagues](#get_teams_team_id_or_slug_leagues)         | List leagues in which the given team was part of     |
| [get_teams_team_id_or_slug_matches](#get_teams_team_id_or_slug_matches)         | List matches for the given team                      |
| [get_teams_team_id_or_slug_series](#get_teams_team_id_or_slug_series)           | List series in which the given team was part of      |
| [get_teams_team_id_or_slug_tournaments](#get_teams_team_id_or_slug_tournaments) | List tournaments in which the given team was part of |

## get_teams

List teams

- HTTP Method: `GET`
- Endpoint: `/teams`

**Parameters**

| Name     | Type                                            | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverTeams](../models/FilterOverTeams.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverTeams](../models/RangeOverTeams.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                       | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverTeams](../models/SearchOverTeams.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                       | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                             | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverTeams, RangeOverTeams, SearchOverTeams

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverTeams(
    acronym=[
        "qui dolore"
    ],
    id_=[
        9
    ],
    location=[
        "in reprehende"
    ],
    modified_at=[
        "elit"
    ],
    name=[
        "deserunt conse"
    ],
    slug=[
        "_pbld"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverTeams(
    acronym=[
        "nulla adipis"
    ],
    id_=[
        6
    ],
    location=[
        "amet comm"
    ],
    modified_at=[
        "non"
    ],
    name=[
        "adipisicing"
    ],
    slug=[
        "b48hhqy"
    ]
)
sort=[
    ""
]
search=SearchOverTeams(
    acronym="exercit",
    location="est L",
    name="culpa Duis t",
    slug="f"
)
page=1

result = sdk.teams.get_teams(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_teams_team_id_or_slug

Get a single team by ID or by slug

- HTTP Method: `GET`
- Endpoint: `/teams/{team_id_or_slug}`

**Parameters**

| Name            | Type                                      | Required | Description       |
| :-------------- | :---------------------------------------- | :------- | :---------------- |
| team_id_or_slug | [TeamIdOrSlug](../models/TeamIdOrSlug.md) | ✅       | A team ID or slug |

**Return Type**

`Team`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
team_id_or_slug=10

result = sdk.teams.get_teams_team_id_or_slug(team_id_or_slug=team_id_or_slug)

print(result)
```

## get_teams_team_id_or_slug_leagues

List leagues in which the given team was part of

- HTTP Method: `GET`
- Endpoint: `/teams/{team_id_or_slug}/leagues`

**Parameters**

| Name            | Type                                                | Required | Description                                                                                                                                         |
| :-------------- | :-------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| team_id_or_slug | [TeamIdOrSlug](../models/TeamIdOrSlug.md)           | ✅       | A team ID or slug                                                                                                                                   |
| filter          | [FilterOverLeagues](../models/FilterOverLeagues.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range           | [RangeOverLeagues](../models/RangeOverLeagues.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort            | List[any]                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search          | [SearchOverLeagues](../models/SearchOverLeagues.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page            | [Page](../models/Page.md)                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page        | int                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[League]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLeagues, RangeOverLeagues, SearchOverLeagues

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
team_id_or_slug=10
filter=FilterOverLeagues(
    id_=[
        7
    ],
    modified_at=[
        "offici"
    ],
    name=[
        "ad ut"
    ],
    slug=[
        "p_"
    ],
    url=[
        "esse aliqu"
    ]
)
range=RangeOverLeagues(
    id_=[
        10
    ],
    modified_at=[
        "ut nulla"
    ],
    name=[
        "ea mol"
    ],
    slug=[
        "pmjvmw-84d"
    ],
    url=[
        "ea aliquip"
    ]
)
sort=[
    ""
]
search=SearchOverLeagues(
    name="Duis dolo",
    slug="-teig",
    url="adipisicing"
)
page=1

result = sdk.teams.get_teams_team_id_or_slug_leagues(
    team_id_or_slug=team_id_or_slug,
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_teams_team_id_or_slug_matches

List matches for the given team

- HTTP Method: `GET`
- Endpoint: `/teams/{team_id_or_slug}/matches`

**Parameters**

| Name            | Type                                                | Required | Description                                                                                                                                         |
| :-------------- | :-------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| team_id_or_slug | [TeamIdOrSlug](../models/TeamIdOrSlug.md)           | ✅       | A team ID or slug                                                                                                                                   |
| filter          | [FilterOverMatches](../models/FilterOverMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range           | [RangeOverMatches](../models/RangeOverMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort            | List[any]                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search          | [SearchOverMatches](../models/SearchOverMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page            | [Page](../models/Page.md)                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page        | int                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverMatches, RangeOverMatches, SearchOverMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
team_id_or_slug=10
filter=FilterOverMatches(
    begin_at=[
        "ani"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "ad ut com"
    ],
    finished=False,
    forfeit=False,
    future=True,
    id_=[
        3
    ],
    league_id=[
        9
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "aute sit"
    ],
    name=[
        "exercitation te"
    ],
    not_started=False,
    number_of_games=[
        8
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=False,
    running=True,
    scheduled_at=[
        "esse aute n"
    ],
    serie_id=[
        10
    ],
    slug=[
        "HiGqjR9"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        3
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        6
    ],
    videogame_version=[
        "1125897835.45"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverMatches(
    begin_at=[
        "al"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "do d"
    ],
    forfeit=[
        False
    ],
    id_=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "dolore ve"
    ],
    name=[
        "dolore "
    ],
    number_of_games=[
        10
    ],
    scheduled_at=[
        "nisi sed aut"
    ],
    slug=[
        "bAjOZ"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        3
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverMatches(
    match_type="all_games_played",
    name="nulla veniam ",
    slug="WfL1ZPQ",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.teams.get_teams_team_id_or_slug_matches(
    team_id_or_slug=team_id_or_slug,
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_teams_team_id_or_slug_series

List series in which the given team was part of

- HTTP Method: `GET`
- Endpoint: `/teams/{team_id_or_slug}/series`

**Parameters**

| Name            | Type                                              | Required | Description                                                                                                                                         |
| :-------------- | :------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| team_id_or_slug | [TeamIdOrSlug](../models/TeamIdOrSlug.md)         | ✅       | A team ID or slug                                                                                                                                   |
| filter          | [FilterOverSeries](../models/FilterOverSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range           | [RangeOverSeries](../models/RangeOverSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort            | List[any]                                         | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search          | [SearchOverSeries](../models/SearchOverSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page            | [Page](../models/Page.md)                         | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page        | int                                               | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverSeries, RangeOverSeries, SearchOverSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
team_id_or_slug=10
filter=FilterOverSeries(
    begin_at=[
        "sunt cillum dol"
    ],
    end_at=[
        "dolor"
    ],
    id_=[
        5
    ],
    league_id=[
        7
    ],
    modified_at=[
        "deserunt"
    ],
    name=[
        "laboris"
    ],
    season=[
        "proident"
    ],
    slug=[
        "_9"
    ],
    videogame_title=[
        7
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ],
    year=[
        None
    ]
)
range=RangeOverSeries(
    begin_at=[
        "sint c"
    ],
    end_at=[
        "ex dolore tempo"
    ],
    id_=[
        6
    ],
    league_id=[
        6
    ],
    modified_at=[
        "lab"
    ],
    name=[
        "animea labore e"
    ],
    season=[
        "ipsum i"
    ],
    slug=[
        "8"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ],
    year=[
        None
    ]
)
sort=[
    ""
]
search=SearchOverSeries(
    name="fugia",
    season="aute al",
    slug="cc3u_",
    winner_type="Player"
)
page=1

result = sdk.teams.get_teams_team_id_or_slug_series(
    team_id_or_slug=team_id_or_slug,
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_teams_team_id_or_slug_tournaments

List tournaments in which the given team was part of

- HTTP Method: `GET`
- Endpoint: `/teams/{team_id_or_slug}/tournaments`

**Parameters**

| Name            | Type                                                                  | Required | Description                                                                                                                                         |
| :-------------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| team_id_or_slug | [TeamIdOrSlug](../models/TeamIdOrSlug.md)                             | ✅       | A team ID or slug                                                                                                                                   |
| filter          | [FilterOverShortTournaments](../models/FilterOverShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range           | [RangeOverShortTournaments](../models/RangeOverShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort            | List[any]                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search          | [SearchOverShortTournaments](../models/SearchOverShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page            | [Page](../models/Page.md)                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page        | int                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverShortTournaments, RangeOverShortTournaments, SearchOverShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
team_id_or_slug=10
filter=FilterOverShortTournaments(
    begin_at=[
        "pariat"
    ],
    detailed_stats=True,
    end_at=[
        "eli"
    ],
    has_bracket=False,
    id_=[
        4
    ],
    live_supported=False,
    modified_at=[
        "cillu"
    ],
    name=[
        "Excepteur do"
    ],
    prizepool=[
        "in ut veniam "
    ],
    serie_id=[
        10
    ],
    slug=[
        "z160_"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        5
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverShortTournaments(
    begin_at=[
        "et"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "commo"
    ],
    has_bracket=[
        False
    ],
    id_=[
        1
    ],
    modified_at=[
        "nul"
    ],
    name=[
        "enim "
    ],
    prizepool=[
        "qui ull"
    ],
    serie_id=[
        3
    ],
    slug=[
        "vyokv"
    ],
    tier=[
        "a"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverShortTournaments(
    name="sunt minim",
    prizepool="utid magna es",
    slug="50l9n",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.teams.get_teams_team_id_or_slug_tournaments(
    team_id_or_slug=team_id_or_slug,
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
