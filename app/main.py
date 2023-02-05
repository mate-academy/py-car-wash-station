class Car:
    def __init__(self,
                 in_class: int,
                 in_mark: int,
                 in_brand: str) -> None:
        self.comfort_class = in_class
        self.clean_mark = in_mark
        self.brand = in_brand


class CarWashStation:
    def __init__(self,
                 in_distance: float,
                 in_power: int,
                 in_rating: float,
                 in_count: int) -> None:
        self.distance_from_city_center = in_distance
        self.clean_power = in_power
        self.average_rating = in_rating
        self.count_of_ratings = in_count

    def calculate_washing_price(self, in_car: Car) -> float:
        price = in_car.comfort_class                    \
            * (self.clean_power - in_car.clean_mark)    \
            * self.average_rating                       \
            / self.distance_from_city_center
        price = round(price, 1)
        return price

    def wash_single_car(self, in_car: Car) -> None:
        in_car.clean_mark = self.clean_power

    def serve_cars(self, cars_to_wash: list[Car]) -> float:
        income = 0
        for car in cars_to_wash:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        income = round(income, 1)
        return income

    def rate_service(self, feedback: int) -> None:
        new_rate = (self.average_rating * self.count_of_ratings + feedback) / \
                   (self.count_of_ratings + 1)
        self.count_of_ratings += 1
        self.average_rating = round(new_rate, 1)
