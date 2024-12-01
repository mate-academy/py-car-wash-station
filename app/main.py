class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: Car) -> float:
        income = 0.0
        for i in range(len(cars)):
            if cars[i].clean_mark <= self.clean_power:
                income += self.calculate_washing_price(cars[i])
                self.wash_single_car(cars[i])
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        inc = car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center
        return inc

    def wash_single_car(self, car: Car) -> Car:
        car.clean_mark = self.clean_power
        return car

    def rate_service(self, number: int) -> None:
        new_rating = round((self.average_rating * self.count_of_ratings + number) / (self.count_of_ratings + 1), 1)
        self.average_rating = new_rating
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