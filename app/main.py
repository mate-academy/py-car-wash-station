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
        total_income = 0
        for car in cars:
            price = self.wash_single_car(car)
            total_income += price
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = 0
        if car.clean_mark < self.clean_power:
            price = (
                (self.clean_power - car.clean_mark) * car.comfort_class
            ) * (self.average_rating / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price
        return 0.0

    def rate_service(self, rating: float) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rating)
            / (self.count_of_ratings + 1),
            1
        )
        self.count_of_ratings += 1


if __name__ == "__main__":
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
