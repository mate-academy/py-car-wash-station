class Car:
    # write your code here
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    # write your code here
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, Cars: list) -> float:
        income = 0
        for car in Cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power

        return income

    def calculate_washing_price(self, car: Car) -> float:

        cost = (car.comfort_class * (self.clean_power - car.clean_mark)
                * self.average_rating / self.distance_from_city_center)
        return cost

    def wash_single_car(self, car: Car) -> int:
        car.clean_mark = self.clean_power if self.clean_power > car.clean_mark else car.clean_mark
        return car.clean_mark

    def rate_service(self, single_rate: int) -> None:
        self.average_rating = (self.average_rating * self.count_of_ratings + single_rate) / (self.count_of_ratings + 1)
        self.count_of_ratings += 1

wash_station = CarWashStation(
    distance_from_city_center=6,
    clean_power=8,
    average_rating=3.9,
    count_of_ratings=11
)

print(wash_station.average_rating)    # 3.9
print(wash_station.count_of_ratings)  # 11

wash_station.rate_service(5)

print(wash_station.average_rating)    # 4.0
print(wash_station.count_of_ratings)  # 12





