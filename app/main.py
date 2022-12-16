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
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list) -> float:
        income = 0
        for car in list_of_cars:
            print(car.brand)
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        washing_price = \
            car.comfort_class * (self.clean_power - car.clean_mark) * \
            self.average_rating / self.distance_from_city_center
        return round(washing_price, 1)

    def wash_single_car(self, car: Car):
        if wash_station.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power


    def rate_service(self):
        pass


bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
audi = Car(comfort_class=4, clean_mark=9, brand='Audi')

print(f"bmv clean mark: {bmw.clean_mark}")  # 3

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6
)
print(wash_station.distance_from_city_center)
# income = wash_station.serve_cars([bmw, audi])
#
# print(income)  # 6.3
print(audi.clean_mark)  # 6




