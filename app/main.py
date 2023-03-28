class Car:

    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list[Car]) -> float:
        income = 0

        for car in car_list:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, vehicle: Car) -> float:
        price = (vehicle.comfort_class
                 * (self.clean_power
                    - vehicle.clean_mark)
                 * self.average_rating
                 / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, vehicle: Car) -> None:
        if self.clean_power > vehicle.clean_mark:
            vehicle.clean_mark = self.clean_power

    def rate_service(self, new_rate: int) -> None:
        self.average_rating = round(
            (self.average_rating
             * self.count_of_ratings
             + new_rate)
            / (self.count_of_ratings + 1), 1
        )
        self.count_of_ratings += 1
