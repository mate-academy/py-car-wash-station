class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class  # 1 to 7
        self.clean_mark = clean_mark  # 1 to 10
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for car in cars:
            if self.clean_power > car.clean_mark:
                income += round(((car.comfort_class
                                 * (self.clean_power - car.clean_mark))
                                 * self.average_rating
                                 / self.distance_from_city_center), 1)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            result = round((car.comfort_class
                           * (self.clean_power - car.clean_mark))
                           * self.average_rating
                           / self.distance_from_city_center, 1)
        else:
            return 0
        return result

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, grade: int) -> None:
        self.count_of_ratings += 1
        self.average_rating = round((self.average_rating
                                    * (self.count_of_ratings - 1) + grade)
                                    / self.count_of_ratings, 1)
