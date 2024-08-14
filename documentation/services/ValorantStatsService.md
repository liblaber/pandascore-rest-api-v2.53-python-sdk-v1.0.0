# ValorantStatsService

A list of all methods in the `ValorantStatsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                                                                           | Description                                                       |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------- |
| [get_valorant_matches_match_id_or_slug_players_stats](#get_valorant_matches_match_id_or_slug_players_stats)                                                       | Get the aggregated statistics for all players in a Valorant match |
| [get_valorant_matches_match_id_or_slug_teams_team_id_or_slug_stats](#get_valorant_matches_match_id_or_slug_teams_team_id_or_slug_stats)                           | Get the aggregated team statistics for a Valorant match           |
| [get_valorant_players_player_id_or_slug_stats](#get_valorant_players_player_id_or_slug_stats)                                                                     | Get a Valorant player stats by ID or slug                         |
| [get_valorant_series_serie_id_or_slug_players_player_id_or_slug_stats](#get_valorant_series_serie_id_or_slug_players_player_id_or_slug_stats)                     | Get the aggregated player statistics for a Valorant series        |
| [get_valorant_series_serie_id_or_slug_teams_team_id_or_slug_stats](#get_valorant_series_serie_id_or_slug_teams_team_id_or_slug_stats)                             | Get the aggregated team statistics for a Valorant series          |
| [get_valorant_teams_team_id_or_slug_stats](#get_valorant_teams_team_id_or_slug_stats)                                                                             | Get a Valorant team stats by ID or slug                           |
| [get_valorant_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats](#get_valorant_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats) | Get the aggregated player statistics for a Valorant tournament    |
| [get_valorant_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats](#get_valorant_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats)         | Get the aggregated team statistics for a Valorant tournament      |

## get_valorant_matches_match_id_or_slug_players_stats

Get the aggregated statistics for all players in a Valorant match

- HTTP Method: `GET`
- Endpoint: `/valorant/matches/{match_id_or_slug}/players/stats`

**Parameters**

| Name             | Type                                        | Required | Description        |
| :--------------- | :------------------------------------------ | :------- | :----------------- |
| match_id_or_slug | [MatchIdOrSlug](../models/MatchIdOrSlug.md) | ✅       | A match ID or slug |

**Return Type**

`ValorantStatsForPlayersByMatch`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
match_id_or_slug=5

result = sdk.valorant_stats.get_valorant_matches_match_id_or_slug_players_stats(match_id_or_slug=match_id_or_slug)

print(result)
```

## get_valorant_matches_match_id_or_slug_teams_team_id_or_slug_stats

Get the aggregated team statistics for a Valorant match

- HTTP Method: `GET`
- Endpoint: `/valorant/matches/{match_id_or_slug}/teams/{team_id_or_slug}/stats`

**Parameters**

| Name             | Type                                        | Required | Description        |
| :--------------- | :------------------------------------------ | :------- | :----------------- |
| match_id_or_slug | [MatchIdOrSlug](../models/MatchIdOrSlug.md) | ✅       | A match ID or slug |
| team_id_or_slug  | [TeamIdOrSlug](../models/TeamIdOrSlug.md)   | ✅       | A team ID or slug  |

**Return Type**

`ValorantStatsForTeamByMatch`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
match_id_or_slug=5
team_id_or_slug=10

result = sdk.valorant_stats.get_valorant_matches_match_id_or_slug_teams_team_id_or_slug_stats(
    match_id_or_slug=match_id_or_slug,
    team_id_or_slug=team_id_or_slug
)

print(result)
```

## get_valorant_players_player_id_or_slug_stats

Get a Valorant player stats by ID or slug

- HTTP Method: `GET`
- Endpoint: `/valorant/players/{player_id_or_slug}/stats`

**Parameters**

| Name              | Type                                                        | Required | Description            |
| :---------------- | :---------------------------------------------------------- | :------- | :--------------------- |
| player_id_or_slug | [PlayerIdOrSlug](../models/PlayerIdOrSlug.md)               | ✅       | A player ID or slug    |
| videogame_version | [VideogameVersionOrAll](../models/VideogameVersionOrAll.md) | ❌       |                        |
| from\_            | str                                                         | ❌       | Filter out 'from' date |
| to                | str                                                         | ❌       | Filter out 'to' date   |

**Return Type**

`ValorantStatsForPlayer`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
player_id_or_slug=9
videogame_version="5.4970743709"

result = sdk.valorant_stats.get_valorant_players_player_id_or_slug_stats(
    player_id_or_slug=player_id_or_slug,
    videogame_version=videogame_version,
    from_="2017-07-21",
    to="2017-07-21"
)

print(result)
```

## get_valorant_series_serie_id_or_slug_players_player_id_or_slug_stats

Get the aggregated player statistics for a Valorant series

- HTTP Method: `GET`
- Endpoint: `/valorant/series/{serie_id_or_slug}/players/{player_id_or_slug}/stats`

**Parameters**

| Name              | Type                                                        | Required | Description         |
| :---------------- | :---------------------------------------------------------- | :------- | :------------------ |
| serie_id_or_slug  | [SerieIdOrSlug](../models/SerieIdOrSlug.md)                 | ✅       | A serie ID or slug  |
| player_id_or_slug | [PlayerIdOrSlug](../models/PlayerIdOrSlug.md)               | ✅       | A player ID or slug |
| videogame_version | [VideogameVersionOrAll](../models/VideogameVersionOrAll.md) | ❌       |                     |

**Return Type**

`ValorantStatsForPlayerBySerie`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
serie_id_or_slug=10
player_id_or_slug=9
videogame_version="5.4970743709"

result = sdk.valorant_stats.get_valorant_series_serie_id_or_slug_players_player_id_or_slug_stats(
    serie_id_or_slug=serie_id_or_slug,
    player_id_or_slug=player_id_or_slug,
    videogame_version=videogame_version
)

print(result)
```

## get_valorant_series_serie_id_or_slug_teams_team_id_or_slug_stats

Get the aggregated team statistics for a Valorant series

- HTTP Method: `GET`
- Endpoint: `/valorant/series/{serie_id_or_slug}/teams/{team_id_or_slug}/stats`

**Parameters**

| Name              | Type                                                        | Required | Description        |
| :---------------- | :---------------------------------------------------------- | :------- | :----------------- |
| serie_id_or_slug  | [SerieIdOrSlug](../models/SerieIdOrSlug.md)                 | ✅       | A serie ID or slug |
| team_id_or_slug   | [TeamIdOrSlug](../models/TeamIdOrSlug.md)                   | ✅       | A team ID or slug  |
| videogame_version | [VideogameVersionOrAll](../models/VideogameVersionOrAll.md) | ❌       |                    |

**Return Type**

`ValorantStatsForTeamBySerie`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
serie_id_or_slug=10
team_id_or_slug=10
videogame_version="5.4970743709"

result = sdk.valorant_stats.get_valorant_series_serie_id_or_slug_teams_team_id_or_slug_stats(
    serie_id_or_slug=serie_id_or_slug,
    team_id_or_slug=team_id_or_slug,
    videogame_version=videogame_version
)

print(result)
```

## get_valorant_teams_team_id_or_slug_stats

Get a Valorant team stats by ID or slug

- HTTP Method: `GET`
- Endpoint: `/valorant/teams/{team_id_or_slug}/stats`

**Parameters**

| Name              | Type                                                        | Required | Description            |
| :---------------- | :---------------------------------------------------------- | :------- | :--------------------- |
| team_id_or_slug   | [TeamIdOrSlug](../models/TeamIdOrSlug.md)                   | ✅       | A team ID or slug      |
| videogame_version | [VideogameVersionOrAll](../models/VideogameVersionOrAll.md) | ❌       |                        |
| from\_            | str                                                         | ❌       | Filter out 'from' date |
| to                | str                                                         | ❌       | Filter out 'to' date   |

**Return Type**

`ValorantStatsForTeam`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
team_id_or_slug=10
videogame_version="5.4970743709"

result = sdk.valorant_stats.get_valorant_teams_team_id_or_slug_stats(
    team_id_or_slug=team_id_or_slug,
    videogame_version=videogame_version,
    from_="2017-07-21",
    to="2017-07-21"
)

print(result)
```

## get_valorant_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats

Get the aggregated player statistics for a Valorant tournament

- HTTP Method: `GET`
- Endpoint: `/valorant/tournaments/{tournament_id_or_slug}/players/{player_id_or_slug}/stats`

**Parameters**

| Name                  | Type                                                        | Required | Description             |
| :-------------------- | :---------------------------------------------------------- | :------- | :---------------------- |
| tournament_id_or_slug | [TournamentIdOrSlug](../models/TournamentIdOrSlug.md)       | ✅       | A tournament ID or slug |
| player_id_or_slug     | [PlayerIdOrSlug](../models/PlayerIdOrSlug.md)               | ✅       | A player ID or slug     |
| videogame_version     | [VideogameVersionOrAll](../models/VideogameVersionOrAll.md) | ❌       |                         |

**Return Type**

`ValorantStatsForPlayerByTournament`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
tournament_id_or_slug=2
player_id_or_slug=9
videogame_version="5.4970743709"

result = sdk.valorant_stats.get_valorant_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats(
    tournament_id_or_slug=tournament_id_or_slug,
    player_id_or_slug=player_id_or_slug,
    videogame_version=videogame_version
)

print(result)
```

## get_valorant_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats

Get the aggregated team statistics for a Valorant tournament

- HTTP Method: `GET`
- Endpoint: `/valorant/tournaments/{tournament_id_or_slug}/teams/{team_id_or_slug}/stats`

**Parameters**

| Name                  | Type                                                        | Required | Description             |
| :-------------------- | :---------------------------------------------------------- | :------- | :---------------------- |
| tournament_id_or_slug | [TournamentIdOrSlug](../models/TournamentIdOrSlug.md)       | ✅       | A tournament ID or slug |
| team_id_or_slug       | [TeamIdOrSlug](../models/TeamIdOrSlug.md)                   | ✅       | A team ID or slug       |
| videogame_version     | [VideogameVersionOrAll](../models/VideogameVersionOrAll.md) | ❌       |                         |

**Return Type**

`ValorantStatsForTeamByTournament`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
tournament_id_or_slug=2
team_id_or_slug=10
videogame_version="5.4970743709"

result = sdk.valorant_stats.get_valorant_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats(
    tournament_id_or_slug=tournament_id_or_slug,
    team_id_or_slug=team_id_or_slug,
    videogame_version=videogame_version
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
