from typing import List, Union


class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: Union[float, int],
            clean_power: Union[float, int],
            average_rating: Union[float, int],
            count_of_ratings: Union[int, float],
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> int:
        washing_price_all_car = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                washing_price_all_car += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return washing_price_all_car

    def calculate_washing_price(self, car: Car) -> Union[int, float]:
        washing_price = round(
            car.comfort_class
            * (self.clean_power
               - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center,
            1
        )
        return washing_price

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings
                                     + rating)
                                    / (self.count_of_ratings
                                       + 1),
                                    1)
        self.count_of_ratings += 1
