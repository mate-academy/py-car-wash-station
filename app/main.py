class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = (car.comfort_class * (self.clean_power - car.clean_mark)
                 * self.average_rating) / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        self.average_rating = round(((self.average_rating
                                    * self.count_of_ratings)
                                    + rating) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1


bmw = Car(comfort_class=3, clean_mark=3, brand="BMW")
audi = Car(comfort_class=4, clean_mark=2, brand="Audi")

print(bmw.clean_mark)  # 3

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6
)

income = wash_station.serve_cars([bmw, audi])

print(income)  # 6.3
print(bmw.clean_mark)  # 6
print(audi.clean_mark)  # 6

print("######")
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

print("######")
print("######")

bmw = Car(3, 3, "BMW")
audi = Car(4, 9, "Audi")
mercedes = Car(7, 1, "Mercedes")

ws = CarWashStation(6, 8, 3.9, 11)

income = ws.serve_cars([
    bmw,
    audi,
    mercedes
])

print(income)

print(bmw.clean_mark)
print(audi.clean_mark)
print(mercedes.clean_mark)
# audi wasn't washed
# all other cars are washed to '8'

ford = Car(2, 1, "Ford")
wash_cost = ws.calculate_washing_price(ford)
# only calculating cost, not washing
print(f"fords wash_cost: {wash_cost}")
print(f"ford.clean_mark: {ford.clean_mark}")

ws.rate_service(5)

print(f"ws.count_of_ratings: {ws.count_of_ratings}")
print(f"ws.average_rating: {ws.average_rating}")
