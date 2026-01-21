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

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0
        for car in cars:
            if self.clean_power >= car.clean_mark:
                cost = round(self.calculate_washing_price(car), 1)
                total_income += cost
                self.wash_single_car(car)
        return total_income

    def calculate_washing_price(self, cars: Car) -> float:
        diff = self.clean_power - cars.clean_mark
        wash_cost = (cars.comfort_class * diff * self.average_rating
                     / self.distance_from_city_center)
        return round(wash_cost, 1)

    def wash_single_car(self, cars: Car) -> None:
        if self.clean_power >= cars.clean_mark:
            cars.clean_mark = self.clean_power

    def rate_service(self, single_rate: int) -> None:
        amount_rates = (self.average_rating
                        * self.count_of_ratings)
        self.count_of_ratings += 1
        self.average_rating = round((amount_rates + single_rate)
                                    / self.count_of_ratings, 1)
