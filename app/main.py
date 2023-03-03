from typing import List


class Car():
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation():
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        final_result = 0
        for car in cars:
            if car.clean_mark <= self.clean_power:
                final_result += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return final_result

    def calculate_washing_price(self, cars: Car) -> float:
        cost_of_wash = cars.comfort_class * \
            (self.clean_power - cars.clean_mark) * \
            self.average_rating / self.distance_from_city_center
        return round(cost_of_wash, 1)

    def wash_single_car(self, cars: Car) -> None:
        cars.clean_mark = self.clean_power

    def rate_service(self, single_rate: int) -> None:
        self.average_rating = round((
            (self.average_rating
             * self.count_of_ratings + single_rate)
            / (self.count_of_ratings + 1)), 1)
        self.count_of_ratings += 1
