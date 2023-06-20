class Car:

    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

    def set_clean_mark(self, clean_mark: int) -> None:
        self.clean_mark = clean_mark


class CarWashStation:

    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:

        income = 0

        for car in cars:
            if self.can_wash_car(car):
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return income

    def calculate_washing_price(self, car: Car) -> float:

        difference_power_mark = self.clean_power - car.clean_mark
        div_rating = self.average_rating / self.distance_from_city_center
        income = car.comfort_class * difference_power_mark * div_rating

        return round(income, 1)

    def can_wash_car(self, car: Car) -> bool:

        return self.clean_power > car.clean_mark

    def wash_single_car(self, car: Car) -> None:

        if self.can_wash_car(car):
            car.set_clean_mark(self.clean_power)

    def rate_service(self, grade: int) -> None:

        new_count_of_ratings = self.count_of_ratings + 1

        all_grades = self.average_rating * self.count_of_ratings + grade
        new_average_rating = all_grades / new_count_of_ratings

        self.count_of_ratings = new_count_of_ratings
        self.average_rating = round(new_average_rating, 1)
