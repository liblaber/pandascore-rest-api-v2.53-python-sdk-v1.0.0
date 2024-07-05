# LoLGameEvent

**Properties**

| Name             | Type            | Required | Description                                  |
| :--------------- | :-------------- | :------- | :------------------------------------------- |
| game_id          | int             | ✅       | LoL game ID                                  |
| ingame_timestamp | int             | ✅       |                                              |
| is_first         | bool            | ✅       | Whether event is first of its kind to happen |
| match_id         | int             | ✅       |                                              |
| payload          | LoLEventPayload | ✅       |                                              |
| tournament_id    | int             | ✅       |                                              |
| type\_           | LoLEventType    | ✅       |                                              |
