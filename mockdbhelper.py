class MockDBHelper:

    def connect(self, database='crimemap'):
        pass

    def add_crime(self, category, date, latitude, longitude, description):
        pass

    def get_all_crimes(self):
        return [{
            'latitude': 49.5883,
            'longitude': 34.5514,
            'date': "2016-09-03",
            'category': "mugging",
            'description': "mock description"
        }]
