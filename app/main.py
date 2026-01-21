from typing import List


class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        if 1 <= comfort_class <= 7:
            self.comfort_class = comfort_class
        else:
            raise ValueError("Comfort class must be between 1 and 7")

        if 1 <= clean_mark <= 10:
            self.clean_mark = clean_mark
        else:
            raise ValueError("Clean mark must be between 1 and 10")

        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        if 1.0 <= distance_from_city_center <= 10.0:
            self.distance_from_city_center = distance_from_city_center
        else:
            raise ValueError("Distance must be between 1.0 and 10.0")

        self.clean_power = clean_power

        if 1.0 <= average_rating <= 5.0:
            self.average_rating = round(average_rating, 1)
        else:
            raise ValueError("Average rating must be between 1.0 and 5.0")

        if count_of_ratings >= 0:
            self.count_of_ratings = count_of_ratings
        else:
            raise ValueError("Count of ratings must be non-negative")

    def serve_cars(self, cars: List[Car]) -> int:
        result = 0
        for car in cars:
            if self.wash_single_car(car):
                result += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return result

    def calculate_washing_price(self, car: Car) -> float:
        price = round(
            (car.comfort_class * (self.clean_power - car.clean_mark)
             * self.average_rating / self.distance_from_city_center), 1)
        return price

    def wash_single_car(self, car: Car) -> bool:
        if self.clean_power >= car.clean_mark:
            return True
        return False

    def rate_service(self, rating: int) -> None:
        if 1 <= rating <= 5:
            total_marks = self.average_rating * self.count_of_ratings
            self.count_of_ratings += 1
            self.average_rating = round(
                (total_marks + rating) / self.count_of_ratings, 1)
        else:
            raise ValueError("Rating must be between 1.0 and 5.0")
