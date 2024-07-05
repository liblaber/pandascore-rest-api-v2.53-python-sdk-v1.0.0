# ValorantEventKiller

**Properties**

| Name      | Type              | Required | Description                     |
| :-------- | :---------------- | :------- | :------------------------------ |
| ability   | Ability           | ✅       |                                 |
| agent     | BaseValorantAgent | ✅       |                                 |
| id\_      | int               | ✅       | ID of the player                |
| name      | str               | ✅       | Professional name of the player |
| team_side | ValorantTeamSide  | ✅       | Team side in the round          |
| weapon    | Weapon            | ✅       |                                 |

# Ability

**Properties**

| Name      | Type | Required | Description                    |
| :-------- | :--- | :------- | :----------------------------- |
| id\_      | int  | ✅       | ID of the ability              |
| image_url | str  | ✅       | URL to an image of the ability |
| name      | str  | ✅       | Name of the ability            |

# Weapon

**Properties**

| Name      | Type | Required | Description                   |
| :-------- | :--- | :------- | :---------------------------- |
| id\_      | int  | ✅       | ID of the weapon              |
| image_url | str  | ✅       | URL to an image of the weapon |
| name      | str  | ✅       | Name of the weapon            |
