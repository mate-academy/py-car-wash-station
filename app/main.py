class Car:

    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, single_rate: int) -> None:
        total_ratings = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round(
            (total_ratings + single_rate) / self.count_of_ratings, 1
        )

    def serve_cars(self, cars: list) -> float:
        total_income = 0.0
        for car in cars:
            if self.clean_power > car.clean_mark:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)


bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
audi = Car(comfort_class=4, clean_mark=9, brand='Audi')

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

bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
audi = Car(comfort_class=4, clean_mark=2, brand='Audi')


print(bmw.clean_mark)
print(audi.clean_mark)


wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6
)

income = wash_station.serve_cars([bmw, audi])

print(income)  # 17.5


print(bmw.clean_mark)
print(audi.clean_mark)


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

bmw.clean_mark == 8
audi.clean_mark == 9
mercedes.clean_mark == 8
# audi wasn't washed
# all other cars are washed to '8'

ford = Car(2, 1, 'Ford')
wash_cost = ws.calculate_washing_price(ford)
# only calculating cost, not washing
wash_cost == 9.1
ford.clean_mark == 1

ws.rate_service(5)

ws.count_of_ratings == 12
ws.average_rating == 4.0
