from typing import List


class Car:
    def __init__(
            self,
            comfort_class: float, clean_mark: float, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: int,
            clean_power: float,
            average_rating: float,
            count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, *args: Car) -> float:
        count_car_list: List[float] = []
        for car in args[0]:
            if car.clean_mark < self.clean_power:
                count_price = self.calculate_washing_price(car)
                self.wash_single_car(car)
                count_car_list.append(count_price)
        count_car = sum(count_car_list)
        print(count_car_list)
        return count_car

    def calculate_washing_price(self, car: Car) -> float:
        price = (
            car.comfort_class * (self.clean_power - car.clean_mark)
            * self.average_rating) / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> float:
        average = self.average_rating * self.count_of_ratings
        new_rating = (average + rating) / (self.count_of_ratings + 1)
        self.average_rating = round(new_rating, 1)
        self.count_of_ratings += 1
        return self.average_rating
