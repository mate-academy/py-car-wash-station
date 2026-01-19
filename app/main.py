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
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        distance = 1 / self.distance_from_city_center
        needed_clean = self.clean_power - car.clean_mark
        return (
            distance
            * car.comfort_class
            * needed_clean
            * self.average_rating
        )

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
        return car.clean_mark

    def rate_service(self, new_rating: int) -> float:
        if new_rating >= 1 and new_rating <= 5:
            self.average_rating = round(
                (self.average_rating * self.count_of_ratings + new_rating)
                / (self.count_of_ratings + 1),
                1
            )
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
