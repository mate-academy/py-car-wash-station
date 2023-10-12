"""
According to the task: "calculate_washing_price - method,
that calculates cost for a <<single car wash>>
    ...
        returns number <<rounded>> to 1 decimal;'"
so I suppose there is the obligatory need to round here


the next example in the task
------------
bmw = Car(3, 3, 'BMW')
audi = Car(4, 9, 'Audi')
mercedes = Car(7, 1, 'Mercedes')

ws = CarWashStation(6, 8, 3.9, 11)

income = ws.serve_cars([
    bmw,
    audi,
    mercedes
])

income == 41.7
-------------
without using Decimal gives result of income as 41.6
cause
print((ws.calculate_washing_price(bmw)))  ->9.8
print((ws.calculate_washing_price(audi)))  ->
print((ws.calculate_washing_price(mercedes)))  ->39.8
(31.849999999999997868371792719699442386627197265625 rounded to 1 decimal)

"""

from decimal import Decimal


class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: float) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        cost = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                cost += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return cost

    def calculate_washing_price(self, car: Car) -> float:
        if self.clean_power <= car.clean_mark:
            return 0

        price = round(float(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * Decimal(str(self.average_rating))
            / Decimal(str(self.distance_from_city_center))
        ), 1)

        # without Decimal what I find not to be precise
        # price = round(
        #     car.comfort_class * (self.clean_power - car.clean_mark)
        #     * self.average_rating
        #     / self.distance_from_city_center, 1)
        return price

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1), 1
        )
        self.count_of_ratings += 1
