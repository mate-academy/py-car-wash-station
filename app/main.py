from typing import List


class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        total_income = 0.0
        for car in cars:
            if self.is_car_dirty(car):
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return total_income

    def calculate_washing_price(self, car: Car):
        price = (
                car.comfort_class *
                (self.clean_power - car.clean_mark) *
                (self.average_rating / self.distance_from_city_center)
        )

        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.is_car_dirty(car):
            car.clean_mark = self.clean_power

    def is_car_dirty(self, car: Car) -> bool:
        return car.clean_mark < self.clean_power

    def rate_service(self, rating: int):
        total_rating = self.average_rating * self.count_of_ratings + rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)


bmw = Car(3, 3, 'BMW')
audi = Car(4, 9, 'Audi')
mercedes = Car(7, 1, 'Mercedes')

ws = CarWashStation(6, 8, 3.9, 11)

income = ws.serve_cars([
    bmw,
    audi,
    mercedes
])

print(income)

print(bmw.clean_mark, audi.clean_mark, mercedes.clean_mark)

ford = Car(2, 1, 'Ford')
wash_cost = ws.calculate_washing_price(ford)

print(wash_cost)
print(ford.clean_mark)

ws.rate_service(5)

print(ws.count_of_ratings)
print(ws.average_rating)
