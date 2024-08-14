# LoLStatsService

A list of all methods in the `LoLStatsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                                                                 | Description                                                                          |
| :------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------- |
| [get_lol_matches_match_id_or_slug_players_stats](#get_lol_matches_match_id_or_slug_players_stats)                                                       | Get detailed statistics of League-of-Legends players for the given match             |
| [get_lol_players_player_id_or_slug_stats](#get_lol_players_player_id_or_slug_stats)                                                                     | Get detailed statistics of a given League-of-Legends player                          |
| [get_lol_series_serie_id_or_slug_players_player_id_or_slug_stats](#get_lol_series_serie_id_or_slug_players_player_id_or_slug_stats)                     | Get detailed statistics of a given League-of-Legends player for the given serie      |
| [get_lol_series_serie_id_or_slug_teams_stats](#get_lol_series_serie_id_or_slug_teams_stats)                                                             | Get detailed statistics of the LoL teams for the given series                        |
| [get_lol_series_serie_id_or_slug_teams_team_id_or_slug_stats](#get_lol_series_serie_id_or_slug_teams_team_id_or_slug_stats)                             | Get detailed statistics of a given League-of-Legends team for the given serie        |
| [get_lol_teams_team_id_or_slug_stats](#get_lol_teams_team_id_or_slug_stats)                                                                             | Get detailed statistics of a given League-of-Legends team                            |
| [get_lol_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats](#get_lol_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats) | Get detailed statistics of a given League-of-Legends player for the given tournament |
| [get_lol_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats](#get_lol_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats)         | Get detailed statistics of a given League-of-Legends team for the given tournament   |

## get_lol_matches_match_id_or_slug_players_stats

Get detailed statistics of League-of-Legends players for the given match

- HTTP Method: `GET`
- Endpoint: `/lol/matches/{match_id_or_slug}/players/stats`

**Parameters**

| Name             | Type                                        | Required | Description        |
| :--------------- | :------------------------------------------ | :------- | :----------------- |
| match_id_or_slug | [MatchIdOrSlug](../models/MatchIdOrSlug.md) | ✅       | A match ID or slug |

**Return Type**

`LoLStatsForAllPlayersByMatch`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
match_id_or_slug=5

result = sdk.lo_l_stats.get_lol_matches_match_id_or_slug_players_stats(match_id_or_slug=match_id_or_slug)

print(result)
```

## get_lol_players_player_id_or_slug_stats

Get detailed statistics of a given League-of-Legends player

- HTTP Method: `GET`
- Endpoint: `/lol/players/{player_id_or_slug}/stats`

**Parameters**

| Name              | Type                                                                                      | Required | Description                                                                                                                                                    |
| :---------------- | :---------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| player_id_or_slug | [PlayerIdOrSlug](../models/PlayerIdOrSlug.md)                                             | ✅       | A player ID or slug                                                                                                                                            |
| games_count       | int                                                                                       | ❌       | The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/> |
| side              | [GetLolPlayersPlayerIdOrSlugStatsSide](../models/GetLolPlayersPlayerIdOrSlugStatsSide.md) | ❌       |                                                                                                                                                                |
| videogame_version | [VideogameVersionOrAll](../models/VideogameVersionOrAll.md)                               | ❌       |                                                                                                                                                                |
| from\_            | str                                                                                       | ❌       | Filter out 'from' date                                                                                                                                         |
| to                | str                                                                                       | ❌       | Filter out 'to' date                                                                                                                                           |

**Return Type**

`LoLStatsForPlayer`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import GetLolPlayersPlayerIdOrSlugStatsSide

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
player_id_or_slug=9
videogame_version="5.4970743709"

result = sdk.lo_l_stats.get_lol_players_player_id_or_slug_stats(
    player_id_or_slug=player_id_or_slug,
    games_count=4,
    side="blue",
    videogame_version=videogame_version,
    from_="2017-07-21",
    to="2017-07-21"
)

print(result)
```

## get_lol_series_serie_id_or_slug_players_player_id_or_slug_stats

Get detailed statistics of a given League-of-Legends player for the given serie

- HTTP Method: `GET`
- Endpoint: `/lol/series/{serie_id_or_slug}/players/{player_id_or_slug}/stats`

**Parameters**

| Name              | Type                                                                                      | Required | Description                                                                                                                                                    |
| :---------------- | :---------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| serie_id_or_slug  | [SerieIdOrSlug](../models/SerieIdOrSlug.md)                                               | ✅       | A serie ID or slug                                                                                                                                             |
| player_id_or_slug | [PlayerIdOrSlug](../models/PlayerIdOrSlug.md)                                             | ✅       | A player ID or slug                                                                                                                                            |
| games_count       | int                                                                                       | ❌       | The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/> |
| side              | [GetLolPlayersPlayerIdOrSlugStatsSide](../models/GetLolPlayersPlayerIdOrSlugStatsSide.md) | ❌       |                                                                                                                                                                |
| videogame_version | [VideogameVersionOrAll](../models/VideogameVersionOrAll.md)                               | ❌       |                                                                                                                                                                |

**Return Type**

`LoLStatsForPlayerBySerie`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import GetLolPlayersPlayerIdOrSlugStatsSide

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
serie_id_or_slug=10
player_id_or_slug=9
videogame_version="5.4970743709"

result = sdk.lo_l_stats.get_lol_series_serie_id_or_slug_players_player_id_or_slug_stats(
    serie_id_or_slug=serie_id_or_slug,
    player_id_or_slug=player_id_or_slug,
    games_count=2,
    side="blue",
    videogame_version=videogame_version
)

print(result)
```

## get_lol_series_serie_id_or_slug_teams_stats

Get detailed statistics of the LoL teams for the given series

- HTTP Method: `GET`
- Endpoint: `/lol/series/{serie_id_or_slug}/teams/stats`

**Parameters**

| Name              | Type                                                                                      | Required | Description                                                                                                                                                    |
| :---------------- | :---------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| serie_id_or_slug  | [SerieIdOrSlug](../models/SerieIdOrSlug.md)                                               | ✅       | A serie ID or slug                                                                                                                                             |
| games_count       | int                                                                                       | ❌       | The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/> |
| side              | [GetLolPlayersPlayerIdOrSlugStatsSide](../models/GetLolPlayersPlayerIdOrSlugStatsSide.md) | ❌       |                                                                                                                                                                |
| videogame_version | [VideogameVersionOrAll](../models/VideogameVersionOrAll.md)                               | ❌       |                                                                                                                                                                |
| page              | [Page](../models/Page.md)                                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                           |
| per_page          | int                                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                                     |

**Return Type**

`List[LoLStatsForTeamBySerie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import GetLolPlayersPlayerIdOrSlugStatsSide

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
serie_id_or_slug=10
videogame_version="5.4970743709"
page=1

result = sdk.lo_l_stats.get_lol_series_serie_id_or_slug_teams_stats(
    serie_id_or_slug=serie_id_or_slug,
    games_count=3,
    side="blue",
    videogame_version=videogame_version,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_series_serie_id_or_slug_teams_team_id_or_slug_stats

Get detailed statistics of a given League-of-Legends team for the given serie

- HTTP Method: `GET`
- Endpoint: `/lol/series/{serie_id_or_slug}/teams/{team_id_or_slug}/stats`

**Parameters**

| Name              | Type                                                                                      | Required | Description                                                                                                                                                    |
| :---------------- | :---------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| serie_id_or_slug  | [SerieIdOrSlug](../models/SerieIdOrSlug.md)                                               | ✅       | A serie ID or slug                                                                                                                                             |
| team_id_or_slug   | [TeamIdOrSlug](../models/TeamIdOrSlug.md)                                                 | ✅       | A team ID or slug                                                                                                                                              |
| games_count       | int                                                                                       | ❌       | The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/> |
| side              | [GetLolPlayersPlayerIdOrSlugStatsSide](../models/GetLolPlayersPlayerIdOrSlugStatsSide.md) | ❌       |                                                                                                                                                                |
| videogame_version | [VideogameVersionOrAll](../models/VideogameVersionOrAll.md)                               | ❌       |                                                                                                                                                                |

**Return Type**

`LoLStatsForTeamBySerie`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import GetLolPlayersPlayerIdOrSlugStatsSide

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
serie_id_or_slug=10
team_id_or_slug=10
videogame_version="5.4970743709"

result = sdk.lo_l_stats.get_lol_series_serie_id_or_slug_teams_team_id_or_slug_stats(
    serie_id_or_slug=serie_id_or_slug,
    team_id_or_slug=team_id_or_slug,
    games_count=7,
    side="blue",
    videogame_version=videogame_version
)

print(result)
```

## get_lol_teams_team_id_or_slug_stats

Get detailed statistics of a given League-of-Legends team

- HTTP Method: `GET`
- Endpoint: `/lol/teams/{team_id_or_slug}/stats`

**Parameters**

| Name              | Type                                                                                      | Required | Description                                                                                                                                                    |
| :---------------- | :---------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| team_id_or_slug   | [TeamIdOrSlug](../models/TeamIdOrSlug.md)                                                 | ✅       | A team ID or slug                                                                                                                                              |
| games_count       | int                                                                                       | ❌       | The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/> |
| side              | [GetLolPlayersPlayerIdOrSlugStatsSide](../models/GetLolPlayersPlayerIdOrSlugStatsSide.md) | ❌       |                                                                                                                                                                |
| videogame_version | [VideogameVersionOrAll](../models/VideogameVersionOrAll.md)                               | ❌       |                                                                                                                                                                |
| from\_            | str                                                                                       | ❌       | Filter out 'from' date                                                                                                                                         |
| to                | str                                                                                       | ❌       | Filter out 'to' date                                                                                                                                           |

**Return Type**

`LoLStatsForTeam`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import GetLolPlayersPlayerIdOrSlugStatsSide

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
team_id_or_slug=10
videogame_version="5.4970743709"

result = sdk.lo_l_stats.get_lol_teams_team_id_or_slug_stats(
    team_id_or_slug=team_id_or_slug,
    games_count=8,
    side="blue",
    videogame_version=videogame_version,
    from_="2017-07-21",
    to="2017-07-21"
)

print(result)
```

## get_lol_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats

Get detailed statistics of a given League-of-Legends player for the given tournament

- HTTP Method: `GET`
- Endpoint: `/lol/tournaments/{tournament_id_or_slug}/players/{player_id_or_slug}/stats`

**Parameters**

| Name                  | Type                                                                                      | Required | Description                                                                                                                                                    |
| :-------------------- | :---------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| tournament_id_or_slug | [TournamentIdOrSlug](../models/TournamentIdOrSlug.md)                                     | ✅       | A tournament ID or slug                                                                                                                                        |
| player_id_or_slug     | [PlayerIdOrSlug](../models/PlayerIdOrSlug.md)                                             | ✅       | A player ID or slug                                                                                                                                            |
| games_count           | int                                                                                       | ❌       | The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/> |
| side                  | [GetLolPlayersPlayerIdOrSlugStatsSide](../models/GetLolPlayersPlayerIdOrSlugStatsSide.md) | ❌       |                                                                                                                                                                |
| videogame_version     | [VideogameVersionOrAll](../models/VideogameVersionOrAll.md)                               | ❌       |                                                                                                                                                                |

**Return Type**

`LoLStatsForPlayerByTournament`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import GetLolPlayersPlayerIdOrSlugStatsSide

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
tournament_id_or_slug=2
player_id_or_slug=9
videogame_version="5.4970743709"

result = sdk.lo_l_stats.get_lol_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats(
    tournament_id_or_slug=tournament_id_or_slug,
    player_id_or_slug=player_id_or_slug,
    games_count=8,
    side="blue",
    videogame_version=videogame_version
)

print(result)
```

## get_lol_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats

Get detailed statistics of a given League-of-Legends team for the given tournament

- HTTP Method: `GET`
- Endpoint: `/lol/tournaments/{tournament_id_or_slug}/teams/{team_id_or_slug}/stats`

**Parameters**

| Name                  | Type                                                                                      | Required | Description                                                                                                                                                    |
| :-------------------- | :---------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| tournament_id_or_slug | [TournamentIdOrSlug](../models/TournamentIdOrSlug.md)                                     | ✅       | A tournament ID or slug                                                                                                                                        |
| team_id_or_slug       | [TeamIdOrSlug](../models/TeamIdOrSlug.md)                                                 | ✅       | A team ID or slug                                                                                                                                              |
| games_count           | int                                                                                       | ❌       | The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/> |
| side                  | [GetLolPlayersPlayerIdOrSlugStatsSide](../models/GetLolPlayersPlayerIdOrSlugStatsSide.md) | ❌       |                                                                                                                                                                |
| videogame_version     | [VideogameVersionOrAll](../models/VideogameVersionOrAll.md)                               | ❌       |                                                                                                                                                                |

**Return Type**

`LoLStatsForTeamByTournament`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import GetLolPlayersPlayerIdOrSlugStatsSide

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
tournament_id_or_slug=2
team_id_or_slug=10
videogame_version="5.4970743709"

result = sdk.lo_l_stats.get_lol_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats(
    tournament_id_or_slug=tournament_id_or_slug,
    team_id_or_slug=team_id_or_slug,
    games_count=9,
    side="blue",
    videogame_version=videogame_version
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
