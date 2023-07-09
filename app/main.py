from typing import List


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
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: List[Car]) -> float:
        total_income = 0.0
        for car in car_list:
            if car.clean_mark < self.clean_power:
                wash_cost = self.calculate_washing_price(car)
                total_income += wash_cost
                self.wash_single_car(car)
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        original_clean_mark = car.clean_mark
        return round(
            car.comfort_class
            * (self.clean_power - original_clean_mark)
            * self.average_rating
            / self.distance_from_city_center,
            1,
        )

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rating)
            / (self.count_of_ratings + 1),
            1,
        )
        self.count_of_ratings += 1


bmw = Car(3, 3, "BMW")
audi = Car(4, 9, "Audi")
mercedes = Car(7, 1, "Mercedes")

wash_station = CarWashStation(5, 6, 3.5, 6)

income = wash_station.serve_cars([bmw, audi, mercedes])

wash_station.rate_service(5)

print(income)  # 22.4
print(bmw.clean_mark)  # 6
print(wash_station.average_rating)  # 4.0
print(wash_station.count_of_ratings)  # 7

