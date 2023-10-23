class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class  # (1 - 7)
        self.clean_mark = clean_mark  # (1 - 10)
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int, average_rating:
            float, count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        # how far station from the city center, from 1.0 to 10.0
        self.clean_power = clean_power
        # clean_mark to which this car wash station washes
        # (yes, not all stations can clean your car completely)
        self.average_rating = average_rating
        # average rating of the station, from 1.0 to 5.0, rounded to 1 decimal
        self.count_of_ratings = count_of_ratings
        # number of people who rated

    def can_be_washed(self, car: Car) -> bool:
        return True if self.clean_power > car.clean_mark else False

    def wash_single_car(self, car: Car) -> None:
        if self.can_be_washed(car):
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        if self.can_be_washed(car):
            result = (car.comfort_class * (self.clean_power - car.clean_mark)
                      * self.average_rating / self.distance_from_city_center)
            return round(result, 1)
        return 0.0

    def rate_service(self, rate: int) -> None:
        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings + rate)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

    def serve_cars(self, list_of_cars: list) -> float:
        income = 0
        for car in list_of_cars:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return income
