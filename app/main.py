class Car:
    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, dirty_cars: list[Car]) -> float | int:
        total_income = 0
        for dirty_car in dirty_cars:
            if dirty_car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(dirty_car)
                self.wash_single_car(dirty_car)
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        cleaning_power_difference = self.clean_power - car.clean_mark
        base_income = (car.comfort_class
                       * cleaning_power_difference * self.average_rating)
        income = base_income / self.distance_from_city_center
        rounded_income = round(income, 1)
        return rounded_income

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        self.count_of_ratings += 1
        total_ratings_sum = self.average_rating * (self.count_of_ratings - 1)
        new_total_ratings_sum = total_ratings_sum + rate
        self.average_rating = round(new_total_ratings_sum
                                    / self.count_of_ratings, 1)
