# LeaguesService

A list of all methods in the `LeaguesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                           | Description                                         |
| :------------------------------------------------------------------------------------------------ | :-------------------------------------------------- |
| [get_leagues](#get_leagues)                                                                       | List leagues                                        |
| [get_leagues_league_id_or_slug](#get_leagues_league_id_or_slug)                                   | Get a single league by ID or by slug                |
| [get_leagues_league_id_or_slug_matches](#get_leagues_league_id_or_slug_matches)                   | List matches of the given league                    |
| [get_leagues_league_id_or_slug_matches_past](#get_leagues_league_id_or_slug_matches_past)         | List past matches for the given league              |
| [get_leagues_league_id_or_slug_matches_running](#get_leagues_league_id_or_slug_matches_running)   | List currently running matches for the given league |
| [get_leagues_league_id_or_slug_matches_upcoming](#get_leagues_league_id_or_slug_matches_upcoming) | List upcoming matches for the given league          |
| [get_leagues_league_id_or_slug_series](#get_leagues_league_id_or_slug_series)                     | List series for the given league                    |
| [get_leagues_league_id_or_slug_tournaments](#get_leagues_league_id_or_slug_tournaments)           | List tournaments of the given league                |

## get_leagues

List leagues

- HTTP Method: `GET`
- Endpoint: `/leagues`

**Parameters**

| Name     | Type                                                | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLeagues](../models/FilterOverLeagues.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLeagues](../models/RangeOverLeagues.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLeagues](../models/SearchOverLeagues.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[League]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLeagues, RangeOverLeagues, SearchOverLeagues

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLeagues(
    id_=[
        7
    ],
    modified_at=[
        "ut cillum eu"
    ],
    name=[
        "ad offici"
    ],
    slug=[
        "w"
    ],
    url=[
        "sunt eiusmod "
    ]
)
range=RangeOverLeagues(
    id_=[
        6
    ],
    modified_at=[
        "inci"
    ],
    name=[
        "quis "
    ],
    slug=[
        "jt4vj"
    ],
    url=[
        "Duisdo culpa ni"
    ]
)
sort=[
    ""
]
search=SearchOverLeagues(
    name="veniam",
    slug="7xkee40if",
    url="Excepteur ea"
)
page=1

result = sdk.leagues.get_leagues(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_leagues_league_id_or_slug

Get a single league by ID or by slug

- HTTP Method: `GET`
- Endpoint: `/leagues/{league_id_or_slug}`

**Parameters**

| Name              | Type                                          | Required | Description         |
| :---------------- | :-------------------------------------------- | :------- | :------------------ |
| league_id_or_slug | [LeagueIdOrSlug](../models/LeagueIdOrSlug.md) | ✅       | A league ID or slug |

**Return Type**

`League`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
league_id_or_slug=6

result = sdk.leagues.get_leagues_league_id_or_slug(league_id_or_slug=league_id_or_slug)

print(result)
```

## get_leagues_league_id_or_slug_matches

List matches of the given league

- HTTP Method: `GET`
- Endpoint: `/leagues/{league_id_or_slug}/matches`

**Parameters**

| Name              | Type                                                | Required | Description                                                                                                                                         |
| :---------------- | :-------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| league_id_or_slug | [LeagueIdOrSlug](../models/LeagueIdOrSlug.md)       | ✅       | A league ID or slug                                                                                                                                 |
| filter            | [FilterOverMatches](../models/FilterOverMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range             | [RangeOverMatches](../models/RangeOverMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort              | List[any]                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search            | [SearchOverMatches](../models/SearchOverMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page              | [Page](../models/Page.md)                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page          | int                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverMatches, RangeOverMatches, SearchOverMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
league_id_or_slug=6
filter=FilterOverMatches(
    begin_at=[
        "esse enim in"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "fugiat offic"
    ],
    finished=True,
    forfeit=True,
    future=True,
    id_=[
        1
    ],
    league_id=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "occa"
    ],
    name=[
        "non sed"
    ],
    not_started=False,
    number_of_games=[
        9
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "es"
    ],
    serie_id=[
        4
    ],
    slug=[
        "ZBBpq-e"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "0065.71"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverMatches(
    begin_at=[
        "sed occ"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "aliq"
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
        "proident culpa"
    ],
    name=[
        "in ad"
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "oc"
    ],
    slug=[
        "8-ymAu4"
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
search=SearchOverMatches(
    match_type="all_games_played",
    name="Excepteu",
    slug="Ld3hli",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.leagues.get_leagues_league_id_or_slug_matches(
    league_id_or_slug=league_id_or_slug,
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_leagues_league_id_or_slug_matches_past

List past matches for the given league

- HTTP Method: `GET`
- Endpoint: `/leagues/{league_id_or_slug}/matches/past`

**Parameters**

| Name              | Type                                                | Required | Description                                                                                                                                         |
| :---------------- | :-------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| league_id_or_slug | [LeagueIdOrSlug](../models/LeagueIdOrSlug.md)       | ✅       | A league ID or slug                                                                                                                                 |
| filter            | [FilterOverMatches](../models/FilterOverMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range             | [RangeOverMatches](../models/RangeOverMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort              | List[any]                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search            | [SearchOverMatches](../models/SearchOverMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page              | [Page](../models/Page.md)                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page          | int                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverMatches, RangeOverMatches, SearchOverMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
league_id_or_slug=6
filter=FilterOverMatches(
    begin_at=[
        "esse enim in"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "fugiat offic"
    ],
    finished=True,
    forfeit=True,
    future=True,
    id_=[
        1
    ],
    league_id=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "occa"
    ],
    name=[
        "non sed"
    ],
    not_started=False,
    number_of_games=[
        9
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "es"
    ],
    serie_id=[
        4
    ],
    slug=[
        "ZBBpq-e"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "0065.71"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverMatches(
    begin_at=[
        "sed occ"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "aliq"
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
        "proident culpa"
    ],
    name=[
        "in ad"
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "oc"
    ],
    slug=[
        "8-ymAu4"
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
search=SearchOverMatches(
    match_type="all_games_played",
    name="Excepteu",
    slug="Ld3hli",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.leagues.get_leagues_league_id_or_slug_matches_past(
    league_id_or_slug=league_id_or_slug,
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_leagues_league_id_or_slug_matches_running

List currently running matches for the given league

- HTTP Method: `GET`
- Endpoint: `/leagues/{league_id_or_slug}/matches/running`

**Parameters**

| Name              | Type                                                | Required | Description                                                                                                                                         |
| :---------------- | :-------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| league_id_or_slug | [LeagueIdOrSlug](../models/LeagueIdOrSlug.md)       | ✅       | A league ID or slug                                                                                                                                 |
| filter            | [FilterOverMatches](../models/FilterOverMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range             | [RangeOverMatches](../models/RangeOverMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort              | List[any]                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search            | [SearchOverMatches](../models/SearchOverMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page              | [Page](../models/Page.md)                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page          | int                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverMatches, RangeOverMatches, SearchOverMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
league_id_or_slug=6
filter=FilterOverMatches(
    begin_at=[
        "esse enim in"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "fugiat offic"
    ],
    finished=True,
    forfeit=True,
    future=True,
    id_=[
        1
    ],
    league_id=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "occa"
    ],
    name=[
        "non sed"
    ],
    not_started=False,
    number_of_games=[
        9
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "es"
    ],
    serie_id=[
        4
    ],
    slug=[
        "ZBBpq-e"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "0065.71"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverMatches(
    begin_at=[
        "sed occ"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "aliq"
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
        "proident culpa"
    ],
    name=[
        "in ad"
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "oc"
    ],
    slug=[
        "8-ymAu4"
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
search=SearchOverMatches(
    match_type="all_games_played",
    name="Excepteu",
    slug="Ld3hli",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.leagues.get_leagues_league_id_or_slug_matches_running(
    league_id_or_slug=league_id_or_slug,
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_leagues_league_id_or_slug_matches_upcoming

List upcoming matches for the given league

- HTTP Method: `GET`
- Endpoint: `/leagues/{league_id_or_slug}/matches/upcoming`

**Parameters**

| Name              | Type                                                | Required | Description                                                                                                                                         |
| :---------------- | :-------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| league_id_or_slug | [LeagueIdOrSlug](../models/LeagueIdOrSlug.md)       | ✅       | A league ID or slug                                                                                                                                 |
| filter            | [FilterOverMatches](../models/FilterOverMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range             | [RangeOverMatches](../models/RangeOverMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort              | List[any]                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search            | [SearchOverMatches](../models/SearchOverMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page              | [Page](../models/Page.md)                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page          | int                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverMatches, RangeOverMatches, SearchOverMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
league_id_or_slug=6
filter=FilterOverMatches(
    begin_at=[
        "esse enim in"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "fugiat offic"
    ],
    finished=True,
    forfeit=True,
    future=True,
    id_=[
        1
    ],
    league_id=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "occa"
    ],
    name=[
        "non sed"
    ],
    not_started=False,
    number_of_games=[
        9
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "es"
    ],
    serie_id=[
        4
    ],
    slug=[
        "ZBBpq-e"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "0065.71"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverMatches(
    begin_at=[
        "sed occ"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "aliq"
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
        "proident culpa"
    ],
    name=[
        "in ad"
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "oc"
    ],
    slug=[
        "8-ymAu4"
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
search=SearchOverMatches(
    match_type="all_games_played",
    name="Excepteu",
    slug="Ld3hli",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.leagues.get_leagues_league_id_or_slug_matches_upcoming(
    league_id_or_slug=league_id_or_slug,
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_leagues_league_id_or_slug_series

List series for the given league

- HTTP Method: `GET`
- Endpoint: `/leagues/{league_id_or_slug}/series`

**Parameters**

| Name              | Type                                              | Required | Description                                                                                                                                         |
| :---------------- | :------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| league_id_or_slug | [LeagueIdOrSlug](../models/LeagueIdOrSlug.md)     | ✅       | A league ID or slug                                                                                                                                 |
| filter            | [FilterOverSeries](../models/FilterOverSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range             | [RangeOverSeries](../models/RangeOverSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort              | List[any]                                         | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search            | [SearchOverSeries](../models/SearchOverSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page              | [Page](../models/Page.md)                         | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page          | int                                               | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverSeries, RangeOverSeries, SearchOverSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
league_id_or_slug=6
filter=FilterOverSeries(
    begin_at=[
        "aute Exc"
    ],
    end_at=[
        "occaecat ut"
    ],
    id_=[
        1
    ],
    league_id=[
        5
    ],
    modified_at=[
        "ut"
    ],
    name=[
        "non D"
    ],
    season=[
        "idlaboris iru"
    ],
    slug=[
        "sshkoy8r"
    ],
    videogame_title=[
        5
    ],
    winner_id=[
        9
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
        "cillum"
    ],
    end_at=[
        "eiusmo"
    ],
    id_=[
        4
    ],
    league_id=[
        5
    ],
    modified_at=[
        "proident Ex"
    ],
    name=[
        "Lorem a"
    ],
    season=[
        "deserunt i"
    ],
    slug=[
        "yyk8h"
    ],
    winner_id=[
        9
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
    name="ad amet",
    season="Lorem",
    slug="1xa",
    winner_type="Player"
)
page=1

result = sdk.leagues.get_leagues_league_id_or_slug_series(
    league_id_or_slug=league_id_or_slug,
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_leagues_league_id_or_slug_tournaments

List tournaments of the given league

- HTTP Method: `GET`
- Endpoint: `/leagues/{league_id_or_slug}/tournaments`

**Parameters**

| Name              | Type                                                                  | Required | Description                                                                                                                                         |
| :---------------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| league_id_or_slug | [LeagueIdOrSlug](../models/LeagueIdOrSlug.md)                         | ✅       | A league ID or slug                                                                                                                                 |
| filter            | [FilterOverShortTournaments](../models/FilterOverShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range             | [RangeOverShortTournaments](../models/RangeOverShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort              | List[any]                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search            | [SearchOverShortTournaments](../models/SearchOverShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page              | [Page](../models/Page.md)                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page          | int                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverShortTournaments, RangeOverShortTournaments, SearchOverShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
league_id_or_slug=6
filter=FilterOverShortTournaments(
    begin_at=[
        "qui"
    ],
    detailed_stats=True,
    end_at=[
        "mollit"
    ],
    has_bracket=True,
    id_=[
        5
    ],
    live_supported=True,
    modified_at=[
        "laborum"
    ],
    name=[
        "estlaboris e"
    ],
    prizepool=[
        "labore"
    ],
    serie_id=[
        2
    ],
    slug=[
        "bw"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        10
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverShortTournaments(
    begin_at=[
        "do proident ve"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "adipisicin"
    ],
    has_bracket=[
        False
    ],
    id_=[
        2
    ],
    modified_at=[
        "of"
    ],
    name=[
        "occaec"
    ],
    prizepool=[
        "labori"
    ],
    serie_id=[
        9
    ],
    slug=[
        "jifeh"
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
search=SearchOverShortTournaments(
    name="in amet",
    prizepool="qui tempor",
    slug="g",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.leagues.get_leagues_league_id_or_slug_tournaments(
    league_id_or_slug=league_id_or_slug,
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
