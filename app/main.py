class Car:
    def __init__(
            self,
            comfort_class: int | float,
            clean_mark: int | float,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int | float,
            average_rating: int | float,
            count_of_rating: int
    ) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_rating

    def serve_cars(self, car_list: [Car]) -> float | int:
        income = 0
        for car in car_list:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float | int:
        price = round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center, 1)
        return price

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, mark: int) -> float:
        rate = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round((rate + mark) / self.count_of_ratings, 1)

        return self.average_rating
