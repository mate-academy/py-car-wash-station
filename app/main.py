from typing import Union


class Car:
    def __init__(self, comfort_class: Union[int, float],
                 clean_mark: Union[int, float], brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: Union[int, float],
                 clean_power: Union[int, float],
                 average_rating: Union[int, float],
                 count_of_ratings: Union[int, float]) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def rate_service(self, value: Union[int, float]) -> float:
        sum_rate = self.average_rating * self.count_of_ratings
        sum_rate += value
        self.count_of_ratings += 1
        self.average_rating = round(sum_rate / self.count_of_ratings, 1)

        return self.average_rating

    def calculate_washing_price(self, car: Car) -> float:
        price = (car.comfort_class * (self.clean_power - car.clean_mark)
                 * self.average_rating / self.distance_from_city_center)

        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0
        for item in cars:
            if self.clean_power > item.clean_mark:
                total_income += self.calculate_washing_price(item)
                self.wash_single_car(item)

        return round(total_income, 1)
