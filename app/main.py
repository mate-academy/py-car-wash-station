class Car:
    def __init__(self, _comfort_class: int,
                 _clean_mark: int,
                 _brand: str) -> None:
        if _comfort_class > 7:
            _comfort_class = 7
        elif _comfort_class < 1:
            _comfort_class = 1
        self.comfort_class = _comfort_class

        if _clean_mark > 10:
            _clean_mark = 10
        elif _clean_mark < 1:
            _clean_mark = 1
        self.clean_mark = _clean_mark

        self.brand = _brand


class CarWashStation:
    def __init__(self, _distance_from_city_center: float,
                 _clean_power: int,
                 _average_rating: float,
                 _count_of_ratings: int) -> None:
        if _distance_from_city_center > 10:
            _distance_from_city_center = 10.0
        elif _distance_from_city_center < 1:
            _distance_from_city_center = 1.0
        self.distance_from_city_center = round(_distance_from_city_center, 1)

        if _clean_power > 10:
            _clean_power = 10
        elif _clean_power < 1:
            _clean_power = 1
        self.clean_power = _clean_power

        if _average_rating > 5:
            _average_rating = 5.0
        elif _average_rating < 1:
            _average_rating = 1.0
        self.average_rating = _average_rating

        self.count_of_ratings = _count_of_ratings

    def serve_cars(self, cars: list) -> float:
        total_price = 0
        for car in cars:
            # вартість мийки
            total_price += self.calculate_washing_price(car)
            # Мийка
            self.wash_single_car(car)
        return total_price

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark >= self.clean_power:
            return 0
        return round(car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 2)

    def wash_single_car(self, car: Car) -> Car:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
        return car

    def rate_service(self, rate: int) -> float:
        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings
                                     + rate)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
        return self.average_rating

# ------------------------------------
# bmw = Car(3, 3, 'BMW')
# audi = Car(4, 2, 'Audi')
#
# print(bmw.clean_mark)  # 3
# print(audi.clean_mark) # 2
#
# wash_station = CarWashStation(
#     6,
#     8,
#     3.9,
#     11
# )

# income = wash_station.serve_cars([bmw, audi])
#
# print(income)  # 17.5
#
# print(bmw.clean_mark)  # 6
# print(audi.clean_mark) # 6
#
# print(wash_station.average_rating)    # 3.9
# print(wash_station.count_of_ratings)  # 11
#
# wash_station.rate_service(5)
#
# print(wash_station.average_rating)    # 4.0
# print(wash_station.count_of_ratings)  # 12
