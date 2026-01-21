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

    def serve_cars(self, cars: dict) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:

                income += (
                    (car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating)
                    / self.distance_from_city_center)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = (car.comfort_class * (self.clean_power - car.clean_mark)
                 * self.average_rating) / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        old_rate = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        new_rate = (old_rate + rate) / self.count_of_ratings
        self.average_rating = round(new_rate, 1)

# bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
# audi = Car(comfort_class=4, clean_mark=9, brand='Audi')

# print(bmw.clean_mark)  # 3
#
# wash_station = CarWashStation(
#     distance_from_city_center=5,
#     clean_power=6,
#     average_rating=3.5,
#     count_of_ratings=6
# )
#
# print(wash_station.serve_cars([audi, bmw]))


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

# ws = CarWashStation(6, 8, 3.9, 11)
#
# ford = Car(2, 1, 'Ford')
# wash_cost = ws.calculate_washing_price(ford)
# print((wash_cost))
