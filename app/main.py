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
        self.distance_from_city_center = max(1.0, distance_from_city_center)
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            washing_cost = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return washing_cost
        return 0.0

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0.0
        for car in cars:
            income = self.wash_single_car(car)
            total_income += income
        return round(total_income, 1)

    def rate_service(self, new_rating: float) -> None:
        self.count_of_ratings += 1
        total_rating = self.average_rating * (self.count_of_ratings - 1) + new_rating
        self.average_rating = round(
            total_rating / self.count_of_ratings, 1
        )


bmw = Car(comfort_class=3, clean_mark=3, brand="BMW")
audi = Car(comfort_class=4, clean_mark=9, brand="Audi")
wash_station = CarWashStation(
    distance_from_city_center=5, clean_power=6, average_rating=3.5, count_of_ratings=6
)

income = wash_station.serve_cars([bmw, audi])
print(income)  # 6.3
print(bmw.clean_mark)  # 6
print(audi.clean_mark)  # 9 (not washed)

wash_station.rate_service(5)
print(wash_station.average_rating)  # 3.7
print(wash_station.count_of_ratings)  # 7
