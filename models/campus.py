class Campus:
    def __init__(self, id_campus, id_university, name, location, latitude, longitude, main, www, email):
        self.id_campus = id_campus
        self.id_university = id_university
        self.name = name
        self.location = location
        self.latitude = latitude
        self.longitude = longitude
        self.main = main
        self.www = www
        self.email = email

    def serialize(self):
        return {
            'id_campus': self.id_campus,
            'id_university': self.id_university,
            'name': self.name,
            'location': self.location,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'main': self.main,
            'www': self.www,
            'email': self.email,
        }