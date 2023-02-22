class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
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
        dif_clean = self.clean_power - car.clean_mark
        numerator = car.comfort_class * dif_clean * self.average_rating
        price = numerator / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark >= self.clean_power:
            return
        car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark >= self.clean_power:
                continue

            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return income

    def rate_service(self, evaluation: float) -> None:
        sum_of_mk = self.average_rating * self.count_of_ratings + evaluation
        self.average_rating = round(sum_of_mk / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
