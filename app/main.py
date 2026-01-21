class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 average_rating: float, clean_power: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.average_rating = average_rating
        self.clean_power = clean_power
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        clean_difference = self.clean_power - car.clean_mark
        total = car.comfort_class * self.average_rating
        total_score = total * clean_difference
        return round((total_score / self.distance_from_city_center), 1)

    def rate_service(self, rate: float) -> None:
        new_count = self.count_of_ratings + 1
        total = self.count_of_ratings * self.average_rating + rate
        self.average_rating = total / new_count
        self.average_rating = round(self.average_rating, 1)
        self.count_of_ratings = new_count
