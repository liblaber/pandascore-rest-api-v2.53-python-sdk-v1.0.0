# ValorantMap

An object that represents a Valorant map

**Properties**

| Name               | Type      | Required | Description                                                     |
| :----------------- | :-------- | :------- | :-------------------------------------------------------------- |
| id\_               | int       | ✅       | ID of the map                                                   |
| image_url          | str       | ✅       | URL to an image of the map                                      |
| name               | str       | ✅       | Name of the map                                                 |
| slug               | str       | ✅       | Human-readable identifier of the map                            |
| videogame_versions | List[str] | ✅       | Array of of video game versions (ie. patches) for this resource |
