class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                old_clean_mark = car.clean_mark
                car.clean_mark = min(self.clean_power, 10)
                price_washing_station = (car.comfort_class
                                         * (self.clean_power - old_clean_mark)
                                         * (self.average_rating
                                            / self.distance_from_city_center))
                total_income += price_washing_station
        return round(total_income, 1)

    def rate_service(self, new_rating: float) -> None:
        total_rating = (self.average_rating
                        * self.count_of_ratings + new_rating)
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)


wash_station = CarWashStation(
    distance_from_city_center=6,
    clean_power=8,
    average_rating=3.9,
    count_of_ratings=11
)


print(wash_station.average_rating)  # 3.9
print(wash_station.count_of_ratings)  # 11


wash_station.rate_service(5)


print(wash_station.average_rating)  # 4.0
print(wash_station.count_of_ratings)  # 12


bmw = Car(comfort_class=3, clean_mark=3, brand="BMW")
audi = Car(comfort_class=4, clean_mark=9, brand="Audi")


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
