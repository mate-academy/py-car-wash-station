from typing import List


class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = min(self.clean_power, 10)

    def calculate_washing_price(self, car: Car) -> float:
        old_clean_mark = car.clean_mark
        price = (car.comfort_class * (self.clean_power - old_clean_mark)
                 * (self.average_rating / self.distance_from_city_center))
        return round(price, 1)

    def serve_cars(self, cars: List[Car]) -> float:
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                car_income = self.calculate_washing_price(car)
                total_income += car_income
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, new_rating: float) -> None:
        total_rating = self.average_rating * self.count_of_ratings + new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)


bmw = Car(comfort_class=3, clean_mark=3, brand="BMW")
audi = Car(comfort_class=4, clean_mark=9, brand="Audi")

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6
)


income = wash_station.serve_cars([bmw, audi])


print(income)  # 6.3
print(bmw.clean_mark)  # 6
