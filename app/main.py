class Car:
    def __init__(
        self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: int,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:

        cars_to_wash = [
            car for car in cars if car.clean_mark < self.clean_power
        ]
        total_income = 0
        for car in cars_to_wash:
            total_income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return total_income

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center,
            1,
        )

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating_value: int) -> None:
        new_count = self.count_of_ratings + 1
        updated_average_rating = (
            (self.average_rating * self.count_of_ratings) + rating_value
        ) / new_count
        self.average_rating = round(updated_average_rating, 1)
        self.count_of_ratings = new_count


bmw = Car(comfort_class=3, clean_mark=3, brand="BMW")
audi = Car(comfort_class=4, clean_mark=9, brand="Audi")

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6
)

income = wash_station.serve_cars([bmw, audi])

wash_station_2 = CarWashStation(
    distance_from_city_center=6,
    clean_power=8,
    average_rating=3.9,
    count_of_ratings=11
)
