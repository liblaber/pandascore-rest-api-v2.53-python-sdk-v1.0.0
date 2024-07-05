# ValorantAbility

**Properties**

| Name               | Type        | Required | Description                                                     |
| :----------------- | :---------- | :------- | :-------------------------------------------------------------- |
| ability_type       | AbilityType | ✅       | Ability type                                                    |
| creds              | float       | ✅       | Credit cost of the ability                                      |
| id\_               | int         | ✅       | ID of the ability                                               |
| image_url          | str         | ✅       | URL to an image of the ability                                  |
| name               | str         | ✅       | Name of the ability                                             |
| videogame_versions | List[str]   | ✅       | Array of of video game versions (ie. patches) for this resource |

# AbilityType

Ability type

**Properties**

| Name             | Type | Required | Description        |
| :--------------- | :--- | :------- | :----------------- |
| ABILITY_ONE      | str  | ✅       | "ability_one"      |
| ABILITY_TWO      | str  | ✅       | "ability_two"      |
| GRENADE_ABILITY  | str  | ✅       | "grenade_ability"  |
| ULTIMATE_ABILITY | str  | ✅       | "ultimate_ability" |
