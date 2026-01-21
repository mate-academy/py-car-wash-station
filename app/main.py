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
                 distance_from_city_center: float,
                 clean_power: bool,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list[Car]) -> float:
        cost_for_job = 0
        for car in list_of_cars:
            if self.clean_power > car.clean_mark:
                cost_for_job += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return cost_for_job

    def calculate_washing_price(self, next_car: Car) -> float:
        return round(next_car.comfort_class
                     * (self.clean_power - next_car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, next_car: Car) -> None:
        next_car.clean_mark = self.clean_power

    def rate_service(self, new_rate: int) -> None:
        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings + new_rate)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
