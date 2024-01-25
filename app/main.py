class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int,
                 clean_power: int,
                 average_rating: int,
                 count_of_ratings: int) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> int | float:
        all_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income_subjunctive = round(
                    car.comfort_class * (self.clean_power - car.clean_mark)
                    * self.average_rating / self.distance_from_city_center, 1
                )
                all_income += income_subjunctive
            self.wash_single_car(car)
        return all_income

    def calculate_washing_price(self, car: Car) -> int | float:
        cost_single_car = round(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center, 1
        )

        return cost_single_car

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, other: float | int) -> None:
        new_rating = self.average_rating * self.count_of_ratings + other
        self.average_rating = round(
            new_rating / (self.count_of_ratings + 1), 1
        )
        self.count_of_ratings += 1
