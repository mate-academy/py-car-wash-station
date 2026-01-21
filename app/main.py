from math import floor


class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int, average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list) -> float:
        total_income = 0.0

        for car in car_list:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return round(total_income, 1)

    #car's comfort class * difference between wash station's clean power and car's clean mark * car wash station rating
    #/ car wash station distance to the center of the city
    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating
                        /self.distance_from_city_center, 1)
    #washes a single car, (clean_mark == clean_power) if (wash_station.clean_power < car.clean_mark)
    def wash_single_car(self, car: Car) -> None:
        """Washes a single car by updating its clean_mark if needed."""
        if car.clean_mark > self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, number: int) -> None:
        self.count_of_ratings += 1
        self.average_rating = round((self.average_rating * (self.count_of_ratings - 1) + number)/self.count_of_ratings, 1)



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

print(bmw.clean_mark)  # 3
print(audi.clean_mark) # 2

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6
)

income = wash_station.serve_cars([bmw, audi])

print(income)  # 17.5

print(bmw.clean_mark)  # 6
print(audi.clean_mark) # 6

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
