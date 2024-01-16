class Car:

    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
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

    def serve_cars(self, cars: Car) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                cost = self.calculate_washing_price(car)
                income += cost
        self.wash_single_car(cars)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        cost = round(car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)
        return cost

    def wash_single_car(self, cars: Car) -> Car:
        for car in cars:
            if car.clean_mark < self.clean_power:
                car.clean_mark = self.clean_power
        return cars

    def rate_service(self, rate: int) -> Car:
        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings + rate)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
        return self.average_rating, self.count_of_ratings
