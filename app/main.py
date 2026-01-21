class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        if 1 <= comfort_class <= 7:
            self.comfort_class = comfort_class
        else:
            self.comfort_class = 1

        if 1 <= clean_mark <= 10:
            self.clean_mark = clean_mark
        else:
            self.clean_mark = 1

        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        if 1.0 <= distance_from_city_center <= 10.0:
            self.distance_from_city_center = distance_from_city_center
        else:
            self.distance_from_city_center = 1.0

        if 1.0 <= average_rating <= 5.0:
            self.average_rating = average_rating
        else:
            self.average_rating = 1.0

        self.clean_power = clean_power
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if self.can_station_wash_car(car):
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        difference_between_cleans = self.clean_power - car.clean_mark
        calculating_rating_with_distance = (self.average_rating
                                            / self.distance_from_city_center)
        return round((car.comfort_class * difference_between_cleans
                      * calculating_rating_with_distance), 1)

    def wash_single_car(self, car: Car) -> None:
        if self.can_station_wash_car(car):
            car.clean_mark = self.clean_power

    def can_station_wash_car(self, car: Car) -> bool:
        return car.clean_mark < self.clean_power

    def rate_service(self, rate: int) -> None:
        rating_in_general = self.average_rating * self.count_of_ratings
        new_rating_count = self.count_of_ratings + 1
        self.average_rating = round((rating_in_general + rate)
                                    / new_rating_count, 1)
        self.count_of_ratings = new_rating_count
