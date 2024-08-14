# Dota2GamesService

A list of all methods in the `Dota2GamesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                               | Description                                 |
| :------------------------------------------------------------------------------------ | :------------------------------------------ |
| [get_dota2_games_dota2_game_id](#get_dota2_games_dota2_game_id)                       | Get a single Dota 2 game by ID              |
| [get_dota2_games_dota2_game_id_frames](#get_dota2_games_dota2_game_id_frames)         | List frames for a given Dota 2 game         |
| [get_dota2_matches_match_id_or_slug_games](#get_dota2_matches_match_id_or_slug_games) | List games for a given Dota 2 match         |
| [get_dota2_teams_team_id_or_slug_games](#get_dota2_teams_team_id_or_slug_games)       | List finished games for a given Dota 2 team |

## get_dota2_games_dota2_game_id

Get a single Dota 2 game by ID

- HTTP Method: `GET`
- Endpoint: `/dota2/games/{dota2_game_id}`

**Parameters**

| Name          | Type | Required | Description |
| :------------ | :--- | :------- | :---------- |
| dota2_game_id | int  | ✅       | A game ID   |

**Return Type**

`Dota2Game`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.dota2_games.get_dota2_games_dota2_game_id(dota2_game_id=7)

print(result)
```

## get_dota2_games_dota2_game_id_frames

List frames for a given Dota 2 game

- HTTP Method: `GET`
- Endpoint: `/dota2/games/{dota2_game_id}/frames`

**Parameters**

| Name          | Type                      | Required | Description                                                          |
| :------------ | :------------------------ | :------- | :------------------------------------------------------------------- |
| dota2_game_id | int                       | ✅       | A game ID                                                            |
| page          | [Page](../models/Page.md) | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2` |
| per_page      | int                       | ❌       | Equivalent to `page[size]`                                           |

**Return Type**

`List[Dota2Frame]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
page=1

result = sdk.dota2_games.get_dota2_games_dota2_game_id_frames(
    dota2_game_id=5,
    page=page,
    per_page=50
)

print(result)
```

## get_dota2_matches_match_id_or_slug_games

List games for a given Dota 2 match

- HTTP Method: `GET`
- Endpoint: `/dota2/matches/{match_id_or_slug}/games`

**Parameters**

| Name             | Type                                                      | Required | Description                                                                                                                                         |
| :--------------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| match_id_or_slug | [MatchIdOrSlug](../models/MatchIdOrSlug.md)               | ✅       | A match ID or slug                                                                                                                                  |
| filter           | [FilterOverDota2Games](../models/FilterOverDota2Games.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range            | [RangeOverDota2Games](../models/RangeOverDota2Games.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort             | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search           | [SearchOverDota2Games](../models/SearchOverDota2Games.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page             | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page         | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Dota2Game]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverDota2Games, RangeOverDota2Games, SearchOverDota2Games

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
match_id_or_slug=5
filter=FilterOverDota2Games(
    begin_at=[
        "ad"
    ],
    complete=False,
    detailed_stats=False,
    end_at=[
        "laboris "
    ],
    finished=True,
    first_blood=[
        7
    ],
    forfeit=False,
    id_=[
        5
    ],
    length=[
        2
    ],
    match_id=[
        10
    ],
    position=[
        2
    ],
    status=[
        "finished"
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverDota2Games(
    begin_at=[
        "Ut"
    ],
    complete=[
        True
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "cillum"
    ],
    finished=[
        False
    ],
    first_blood=[
        6
    ],
    forfeit=[
        False
    ],
    id_=[
        4
    ],
    length=[
        9
    ],
    match_id=[
        2
    ],
    position=[
        1
    ],
    status=[
        "finished"
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverDota2Games(
    status="finished",
    winner_type="Player"
)
page=1

result = sdk.dota2_games.get_dota2_matches_match_id_or_slug_games(
    match_id_or_slug=match_id_or_slug,
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_dota2_teams_team_id_or_slug_games

List finished games for a given Dota 2 team

- HTTP Method: `GET`
- Endpoint: `/dota2/teams/{team_id_or_slug}/games`

**Parameters**

| Name            | Type                                      | Required | Description                                                          |
| :-------------- | :---------------------------------------- | :------- | :------------------------------------------------------------------- |
| team_id_or_slug | [TeamIdOrSlug](../models/TeamIdOrSlug.md) | ✅       | A team ID or slug                                                    |
| page            | [Page](../models/Page.md)                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2` |
| per_page        | int                                       | ❌       | Equivalent to `page[size]`                                           |

**Return Type**

`List[BaseDota2Game]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
team_id_or_slug=10
page=1

result = sdk.dota2_games.get_dota2_teams_team_id_or_slug_games(
    team_id_or_slug=team_id_or_slug,
    page=page,
    per_page=50
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
