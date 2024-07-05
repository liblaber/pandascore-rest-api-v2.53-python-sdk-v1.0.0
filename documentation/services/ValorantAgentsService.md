# ValorantAgentsService

A list of all methods in the `ValorantAgentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                         | Description                    |
| :------------------------------------------------------------------------------ | :----------------------------- |
| [get_valorant_agents](#get_valorant_agents)                                     | List agents                    |
| [get_valorant_agents_valorant_agent_id](#get_valorant_agents_valorant_agent_id) | Get a Valorant agent by its ID |

## get_valorant_agents

List agents

- HTTP Method: `GET`
- Endpoint: `/valorant/agents`

**Parameters**

| Name     | Type                                                              | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantAgents](../models/FilterOverValorantAgents.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantAgents](../models/RangeOverValorantAgents.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                         | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantAgents](../models/SearchOverValorantAgents.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                         | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                               | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ValorantAgent]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverValorantAgents, RangeOverValorantAgents, SearchOverValorantAgents

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverValorantAgents(
    id_=[
        8
    ],
    name=[
        "commodo"
    ],
    videogame_version=""
)
range=RangeOverValorantAgents(
    id_=[
        10
    ],
    name=[
        "id sed ad"
    ]
)
sort=[
    ""
]
search=SearchOverValorantAgents(
    name="animin deseru"
)
page=1

result = sdk.valorant_agents.get_valorant_agents(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_valorant_agents_valorant_agent_id

Get a Valorant agent by its ID

- HTTP Method: `GET`
- Endpoint: `/valorant/agents/{valorant_agent_id}`

**Parameters**

| Name              | Type | Required | Description              |
| :---------------- | :--- | :------- | :----------------------- |
| valorant_agent_id | int  | ✅       | ID of the Valorant agent |

**Return Type**

`ValorantAgent`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.valorant_agents.get_valorant_agents_valorant_agent_id(valorant_agent_id=1)

print(result)
```
