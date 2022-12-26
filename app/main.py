class Car:
    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: int,
        clean_power: int, average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list[Car]) -> float:
        income_for_station = 0
        for car in car_list:
            if car.clean_mark < self.clean_power:
                income_for_station += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income_for_station

    def calculate_washing_price(self, car_to_wash: Car) -> float:
        washing_price = round(
            car_to_wash.comfort_class
            * (self.clean_power - car_to_wash.clean_mark)
            * self.average_rating / self.distance_from_city_center, 1)
        return washing_price

    def wash_single_car(self, car_to_wash: Car) -> None:
        car_to_wash.clean_mark = self.clean_power

    def rate_service(self, rate_point: float) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rate_point)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
