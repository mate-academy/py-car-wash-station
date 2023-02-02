class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0

        if len(cars) == 1:
            income += self.calculate_washing_price(cars[0])
            self.wash_single_car(cars[0])

        else:
            for car in cars:
                if car.clean_mark < self.clean_power:
                    income += self.calculate_washing_price(car)
                    car.clean_mark = self.clean_power
        return income

    def calculate_washing_price(self, car: Car) -> float:
        diff = self.clean_power - car.clean_mark
        if diff < 0:
            return 0
        calc = round((car.comfort_class * diff * self.average_rating
                      / self.distance_from_city_center), 1)
        return calc

    def rate_service(self, mark: int) -> None:
        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings + mark)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
