# Dota2StatsService

A list of all methods in the `Dota2StatsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                                                                     | Description                                                              |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------- |
| [get_dota2_matches_match_id_or_slug_players_stats](#get_dota2_matches_match_id_or_slug_players_stats)                                                       | Get detailed statistics of Dota2 players for the given match             |
| [get_dota2_players_player_id_or_slug_stats](#get_dota2_players_player_id_or_slug_stats)                                                                     | Get detailed statistics of a given Dota2 player                          |
| [get_dota2_series_serie_id_or_slug_players_player_id_or_slug_stats](#get_dota2_series_serie_id_or_slug_players_player_id_or_slug_stats)                     | Get detailed statistics of a given Dota2 player for the given serie      |
| [get_dota2_series_serie_id_or_slug_teams_team_id_or_slug_stats](#get_dota2_series_serie_id_or_slug_teams_team_id_or_slug_stats)                             | Get detailed statistics of a given Dota2 team for the given serie        |
| [get_dota2_teams_team_id_or_slug_stats](#get_dota2_teams_team_id_or_slug_stats)                                                                             | Get detailed statistics of a given Dota2 team                            |
| [get_dota2_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats](#get_dota2_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats) | Get detailed statistics of a given Dota2 player for the given tournament |
| [get_dota2_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats](#get_dota2_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats)         | Get detailed statistics of a given Dota2 team for the given tournament   |

## get_dota2_matches_match_id_or_slug_players_stats

Get detailed statistics of Dota2 players for the given match

- HTTP Method: `GET`
- Endpoint: `/dota2/matches/{match_id_or_slug}/players/stats`

**Parameters**

| Name             | Type                                        | Required | Description        |
| :--------------- | :------------------------------------------ | :------- | :----------------- |
| match_id_or_slug | [MatchIdOrSlug](../models/MatchIdOrSlug.md) | ✅       | A match ID or slug |

**Return Type**

`Dota2StatsForAllPlayersByMatch`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
match_id_or_slug=8

result = sdk.dota2_stats.get_dota2_matches_match_id_or_slug_players_stats(match_id_or_slug=match_id_or_slug)

print(result)
```

## get_dota2_players_player_id_or_slug_stats

Get detailed statistics of a given Dota2 player

- HTTP Method: `GET`
- Endpoint: `/dota2/players/{player_id_or_slug}/stats`

**Parameters**

| Name              | Type                                                                                          | Required | Description                                                                                                                                                    |
| :---------------- | :-------------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| player_id_or_slug | [PlayerIdOrSlug](../models/PlayerIdOrSlug.md)                                                 | ✅       | A player ID or slug                                                                                                                                            |
| games_count       | int                                                                                           | ❌       | The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/> |
| side              | [GetDota2PlayersPlayerIdOrSlugStatsSide](../models/GetDota2PlayersPlayerIdOrSlugStatsSide.md) | ❌       |                                                                                                                                                                |
| from\_            | str                                                                                           | ❌       | Filter out 'from' date                                                                                                                                         |
| to                | str                                                                                           | ❌       | Filter out 'to' date                                                                                                                                           |

**Return Type**

`Dota2StatsForPlayer`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import GetDota2PlayersPlayerIdOrSlugStatsSide

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
player_id_or_slug=4

result = sdk.dota2_stats.get_dota2_players_player_id_or_slug_stats(
    player_id_or_slug=player_id_or_slug,
    games_count=8,
    side="radiant",
    from_="2017-07-21",
    to="2017-07-21"
)

print(result)
```

## get_dota2_series_serie_id_or_slug_players_player_id_or_slug_stats

Get detailed statistics of a given Dota2 player for the given serie

- HTTP Method: `GET`
- Endpoint: `/dota2/series/{serie_id_or_slug}/players/{player_id_or_slug}/stats`

**Parameters**

| Name              | Type                                                                                          | Required | Description                                                                                                                                                    |
| :---------------- | :-------------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| serie_id_or_slug  | [SerieIdOrSlug](../models/SerieIdOrSlug.md)                                                   | ✅       | A serie ID or slug                                                                                                                                             |
| player_id_or_slug | [PlayerIdOrSlug](../models/PlayerIdOrSlug.md)                                                 | ✅       | A player ID or slug                                                                                                                                            |
| games_count       | int                                                                                           | ❌       | The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/> |
| side              | [GetDota2PlayersPlayerIdOrSlugStatsSide](../models/GetDota2PlayersPlayerIdOrSlugStatsSide.md) | ❌       |                                                                                                                                                                |

**Return Type**

`Dota2StatsForPlayerBySerie`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import GetDota2PlayersPlayerIdOrSlugStatsSide

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
serie_id_or_slug=3
player_id_or_slug=4

result = sdk.dota2_stats.get_dota2_series_serie_id_or_slug_players_player_id_or_slug_stats(
    serie_id_or_slug=serie_id_or_slug,
    player_id_or_slug=player_id_or_slug,
    games_count=1,
    side="radiant"
)

print(result)
```

## get_dota2_series_serie_id_or_slug_teams_team_id_or_slug_stats

Get detailed statistics of a given Dota2 team for the given serie

- HTTP Method: `GET`
- Endpoint: `/dota2/series/{serie_id_or_slug}/teams/{team_id_or_slug}/stats`

**Parameters**

| Name             | Type                                                                                          | Required | Description                                                                                                                                                    |
| :--------------- | :-------------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| serie_id_or_slug | [SerieIdOrSlug](../models/SerieIdOrSlug.md)                                                   | ✅       | A serie ID or slug                                                                                                                                             |
| team_id_or_slug  | [TeamIdOrSlug](../models/TeamIdOrSlug.md)                                                     | ✅       | A team ID or slug                                                                                                                                              |
| games_count      | int                                                                                           | ❌       | The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/> |
| side             | [GetDota2PlayersPlayerIdOrSlugStatsSide](../models/GetDota2PlayersPlayerIdOrSlugStatsSide.md) | ❌       |                                                                                                                                                                |

**Return Type**

`Dota2StatsForTeamBySerie`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import GetDota2PlayersPlayerIdOrSlugStatsSide

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
serie_id_or_slug=3
team_id_or_slug=7

result = sdk.dota2_stats.get_dota2_series_serie_id_or_slug_teams_team_id_or_slug_stats(
    serie_id_or_slug=serie_id_or_slug,
    team_id_or_slug=team_id_or_slug,
    games_count=2,
    side="radiant"
)

print(result)
```

## get_dota2_teams_team_id_or_slug_stats

Get detailed statistics of a given Dota2 team

- HTTP Method: `GET`
- Endpoint: `/dota2/teams/{team_id_or_slug}/stats`

**Parameters**

| Name            | Type                                                                                          | Required | Description                                                                                                                                                    |
| :-------------- | :-------------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| team_id_or_slug | [TeamIdOrSlug](../models/TeamIdOrSlug.md)                                                     | ✅       | A team ID or slug                                                                                                                                              |
| games_count     | int                                                                                           | ❌       | The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/> |
| side            | [GetDota2PlayersPlayerIdOrSlugStatsSide](../models/GetDota2PlayersPlayerIdOrSlugStatsSide.md) | ❌       |                                                                                                                                                                |
| from\_          | str                                                                                           | ❌       | Filter out 'from' date                                                                                                                                         |
| to              | str                                                                                           | ❌       | Filter out 'to' date                                                                                                                                           |

**Return Type**

`Dota2StatsForTeam`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import GetDota2PlayersPlayerIdOrSlugStatsSide

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
team_id_or_slug=7

result = sdk.dota2_stats.get_dota2_teams_team_id_or_slug_stats(
    team_id_or_slug=team_id_or_slug,
    games_count=3,
    side="radiant",
    from_="2017-07-21",
    to="2017-07-21"
)

print(result)
```

## get_dota2_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats

Get detailed statistics of a given Dota2 player for the given tournament

- HTTP Method: `GET`
- Endpoint: `/dota2/tournaments/{tournament_id_or_slug}/players/{player_id_or_slug}/stats`

**Parameters**

| Name                  | Type                                                                                          | Required | Description                                                                                                                                                    |
| :-------------------- | :-------------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| tournament_id_or_slug | [TournamentIdOrSlug](../models/TournamentIdOrSlug.md)                                         | ✅       | A tournament ID or slug                                                                                                                                        |
| player_id_or_slug     | [PlayerIdOrSlug](../models/PlayerIdOrSlug.md)                                                 | ✅       | A player ID or slug                                                                                                                                            |
| games_count           | int                                                                                           | ❌       | The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/> |
| side                  | [GetDota2PlayersPlayerIdOrSlugStatsSide](../models/GetDota2PlayersPlayerIdOrSlugStatsSide.md) | ❌       |                                                                                                                                                                |

**Return Type**

`Dota2StatsForPlayerByTournament`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import GetDota2PlayersPlayerIdOrSlugStatsSide

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
tournament_id_or_slug=7
player_id_or_slug=4

result = sdk.dota2_stats.get_dota2_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats(
    tournament_id_or_slug=tournament_id_or_slug,
    player_id_or_slug=player_id_or_slug,
    games_count=1,
    side="radiant"
)

print(result)
```

## get_dota2_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats

Get detailed statistics of a given Dota2 team for the given tournament

- HTTP Method: `GET`
- Endpoint: `/dota2/tournaments/{tournament_id_or_slug}/teams/{team_id_or_slug}/stats`

**Parameters**

| Name                  | Type                                                                                          | Required | Description                                                                                                                                                    |
| :-------------------- | :-------------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| tournament_id_or_slug | [TournamentIdOrSlug](../models/TournamentIdOrSlug.md)                                         | ✅       | A tournament ID or slug                                                                                                                                        |
| team_id_or_slug       | [TeamIdOrSlug](../models/TeamIdOrSlug.md)                                                     | ✅       | A team ID or slug                                                                                                                                              |
| games_count           | int                                                                                           | ❌       | The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/> |
| side                  | [GetDota2PlayersPlayerIdOrSlugStatsSide](../models/GetDota2PlayersPlayerIdOrSlugStatsSide.md) | ❌       |                                                                                                                                                                |

**Return Type**

`Dota2StatsForTeamByTournament`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import GetDota2PlayersPlayerIdOrSlugStatsSide

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
tournament_id_or_slug=7
team_id_or_slug=7

result = sdk.dota2_stats.get_dota2_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats(
    tournament_id_or_slug=tournament_id_or_slug,
    team_id_or_slug=team_id_or_slug,
    games_count=10,
    side="radiant"
)

print(result)
```
