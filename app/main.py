class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class  # 1 to 7
        self.clean_mark = clean_mark  # 1 to 10
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating  # 1.0 to 5.0
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """Calculates cost for a single car wash"""
        return round(car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    def serve_cars(self, cars: list) -> float:
        """Returns income of CarWashStation for serving list of Car's"""
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def wash_single_car(self, car: Car) -> None:
        """Returns new clean_mark of car"""
        car.clean_mark = self.clean_power

    def rate_service(self, mark: int) -> None:
        rating = round((self.average_rating * self.count_of_ratings + mark)
                       / (self.count_of_ratings + 1), 1)
        self.average_rating = rating
        self.count_of_ratings += 1
