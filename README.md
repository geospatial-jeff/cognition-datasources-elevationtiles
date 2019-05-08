[![CircleCI](https://circleci.com/gh/geospatial-jeff/cognition-datasources-elevationtiles.svg?style=svg)](https://circleci.com/gh/geospatial-jeff/cognition-datasources-elevationtiles)
## Elevation Tiles

 | Parameter | Status |
| ----------| ------ |
| Spatial | :heavy_check_mark: |
| Temporal | :x: |
| Properties | :heavy_check_mark: |
| **kwargs | [limit, zoom] |

 ##### Properties
| Property | Type | Example |
|--------------------------|-------|-------------|
| eo:gsd | float | 305.74 |
| eo:epsg | int | 3857 |
| eo:instrument | str | 'srtm' |
| legacy:x| int | 55 |
| legacy:y | int | 91 |
| legacy:z | int | 8 |

 ##### Notes
- The source API is a XYZ tiled elevation service.  The `zoom` kwarg changes the zoom level being queried.
- The source API doesn't support temporal data.  Can search with temporal but it is not honored.