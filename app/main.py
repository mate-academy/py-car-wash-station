class Car:

    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for car in cars:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        income = round(income, 1)
        return income

    def calculate_washing_price(self, car: Car) -> float:

        clean_car = self.clean_power - car.clean_mark
        level_of_service = car.comfort_class * clean_car
        clean_price = level_of_service * self.average_rating

        number = clean_price / self.distance_from_city_center
        return number

    def wash_single_car(self, car: Car) -> None:

        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:

        self.count_of_ratings += 1
        rating_point = (self.average_rating * (self.count_of_ratings - 1))
        average_marks = (rating_point + rate) / self.count_of_ratings

        self.average_rating = round(average_marks, 1)
