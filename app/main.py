class CarWashStation:
    def __init__(self, station_id, location_id, avg_rating, num_ratings):
        self.station_id = station_id
        self.location_id = location_id
        self.avg_rating = avg_rating
        self.num_ratings = num_ratings

    def rate_service(self, mark):
        # Обновляем среднюю оценку и количество оценок
        total_rating = self.avg_rating * self.num_ratings
        self.num_ratings += 1
        total_rating += mark
        self.avg_rating = total_rating / self.num_ratings