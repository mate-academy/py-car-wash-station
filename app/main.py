class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError("distance_from_city_center must be between 1.0 and 10.0")
        if not (1.0 <= average_rating <= 5.0):
            raise ValueError("average_rating must be between 1.0 and 5.0")

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings
