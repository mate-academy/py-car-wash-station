class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income = self.wash_single_car(car)
                total_income += income
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = ((self.clean_power - car.clean_mark) * self.average_rating
                 * car.comfort_class / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> float:
        if self.clean_power > car.clean_mark:
            cost = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return cost
        return 0.0

    def rate_service(self, rating: float) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
