class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:

        if car.clean_mark < self.clean_power:
            washing_price = (car.comfort_class * (self.clean_power
                             - car.clean_mark) * self.average_rating
                             / self.distance_from_city_center)
            return round(washing_price, 1)

        return 0

    def wash_single_car(self, car: Car) -> bool:

        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
            return True

        return False

    def rate_service(self, rate: int) -> None:
        total = self.average_rating * self.count_of_ratings
        total += rate
        self.count_of_ratings += 1
        self.average_rating = round(total / self.count_of_ratings, 1)

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                total_income += price
                self.wash_single_car(car)

        return round(total_income, 1)
