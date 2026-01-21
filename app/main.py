class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                difference = self.clean_power - car.clean_mark
                self.wash_single_car(car)
                income += (car.comfort_class
                           * difference
                           * self.average_rating
                           / self.distance_from_city_center)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        difference = 0
        if car.clean_mark < self.clean_power:
            difference = self.clean_power - car.clean_mark
        wash_rating_distance = (self.average_rating
                                / self.distance_from_city_center)
        cost = round(car.comfort_class
                     * difference
                     * wash_rating_distance, 1)
        return cost

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        new_average = ((self.average_rating
                       * self.count_of_ratings + rate)
                       / (self.count_of_ratings + 1))
        self.count_of_ratings += 1
        self.average_rating = round(new_average, 1)
