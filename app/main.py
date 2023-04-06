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
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list[Car]) -> float:
        sum_of_income = 0
        for car in list_of_cars:
            if car.clean_mark < self.clean_power:
                sum_of_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(sum_of_income, 1)

    def calculate_washing_price(self, info_car: Car) -> float:
        return round(info_car.comfort_class
                     * (self.clean_power - info_car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, info_car: Car) -> None:
        if info_car.clean_mark < self.clean_power:
            info_car.clean_mark = self.clean_power

    def rate_service(self, car_info_raiting: float) -> None:
        self.count_of_ratings += 1
        self.average_rating = round((self.average_rating
                                     * (self.count_of_ratings - 1)
                                     + car_info_raiting)
                                    / self.count_of_ratings, 1)
