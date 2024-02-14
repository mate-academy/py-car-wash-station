from typing import List


class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:

        self.distance_from_city = distance_from_city
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        income_counter = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income_counter += \
                    (car.comfort_class
                     * (self.clean_power - car.clean_mark)
                     * (self.average_rating / self.distance_from_city))
                car.clean_mark = self.clean_power
        return round(income_counter, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * (self.average_rating / self.distance_from_city),
            1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        self.count_of_ratings += 1
        total_ratings_sum = (self.average_rating
                             * (self.count_of_ratings - 1) + rate)
        self.average_rating = (
            round((total_ratings_sum / self.count_of_ratings), 1))


bmw = Car(3, 3, "BMW")
audi = Car(4, 9, "Audi")
mercedes = Car(7, 1, "Mercedes")

ws = CarWashStation(6, 8, 3.9, 11)

income = ws.serve_cars([
    bmw,
    audi,
    mercedes
])
