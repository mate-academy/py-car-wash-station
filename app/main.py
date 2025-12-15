class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        if not cars:
            return income

        for car in cars:
            if car.clean_mark >= self.clean_power:
                continue
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * (self.average_rating / self.distance_from_city_center),
            1
        )

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
        return

    def rate_service(self, new_rating: int) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)


"""
# Testing 1
print("Testing 1")
# Define wash station
ws = CarWashStation(6, 8, 3.9, 11)
# Define test car 1
ford = Car(2, 1, 'Ford')
# Calculate washing price for test car 1
wash_cost = ws.calculate_washing_price(ford)
# only calculating cost, not washing
print(wash_cost) #9.1
print(ford.clean_mark) #1

ws.rate_service(5)

print(ws.count_of_ratings) #12
print(ws.average_rating) #4.0

# Testing 2
print("Testing 2")
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
"""
