from typing import List


class Car:
    def __init__(
        self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        if 1 <= comfort_class <= 7:
            self.comfort_class = comfort_class
        else:
            raise ValueError("comfort_class has to be between 1 and 7")
        if 1 <= clean_mark <= 10:
            self.clean_mark = clean_mark
        else:
            raise ValueError("clean_mark has to be between 1 and 10")
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        if 1.0 <= distance_from_city_center <= 10.0:
            self.distance_from_city_center = distance_from_city_center
        else:
            raise ValueError(
                "distance_from_city_center has to be between 1.0 and 10.0"
            )

        self.clean_power = clean_power

        if 1.0 <= average_rating <= 5.0:
            self.average_rating = round(average_rating, 1)
        else:
            raise ValueError("average_rating has to be between 1.0 and 5.0")

        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        result = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(result, 1)

    def wash_single_car(self, car_clean_mark: int) -> int:
        car_clean_mark = (
            self.clean_power
            if self.clean_power > car_clean_mark
            else car_clean_mark
        )
        return car_clean_mark

    def rate_service(self, rating: int) -> None:
        full_current_rating = (
            self.average_rating * self.count_of_ratings + rating
        )
        self.count_of_ratings += 1
        self.average_rating = round(
            full_current_rating / self.count_of_ratings, 1
        )

    def serve_cars(self, cars: List[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                car.clean_mark = self.wash_single_car(car.clean_mark)
        return income
