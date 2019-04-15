from datasources import tests

from ElevationTiles import ElevationTiles

class ElevationTilesTestCases(tests.BaseTestCases):

    def _setUp(self):

        self.datasource = ElevationTiles
        self.spatial = {
                    "type": "Polygon",
                    "coordinates": [
                      [
                        [
                          -101.28433227539062,
                          46.813218976041945
                        ],
                        [
                          -100.89431762695312,
                          46.813218976041945
                        ],
                        [
                          -100.89431762695312,
                          47.06450941441436
                        ],
                        [
                          -101.28433227539062,
                          47.06450941441436
                        ],
                        [
                          -101.28433227539062,
                          46.813218976041945
                        ]
                      ]
                    ]
                  }
        self.properties = {'eo:instrument': {'eq': 'srtm'}}
        self.limit = 10

    def test_temporal_search(self):
        # Datasource doesn't support temporal queries
        pass
