class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str,
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
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list[Car]) -> float:
        total_cost = 0
        allowed_car_list = [
            item for item in car_list if item.clean_mark < self.clean_power
        ]
        for car in allowed_car_list:
            total_cost += self.wash_single_car(car)
        return round(total_cost, 1)

    def calculate_washing_price(self, car: Car) -> float:
        cost_price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(cost_price, 1)

    def wash_single_car(self, car: Car) -> float:
        total_cost = 0
        if car.clean_mark < self.clean_power:
            total_cost = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
        return total_cost

    def rate_service(self, rate: int) -> None:
        total = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round((total + rate) / self.count_of_ratings, 1)


def main() -> None:
    bmw = Car(comfort_class=3, clean_mark=3, brand="BMW")
    audi = Car(comfort_class=4, clean_mark=9, brand="Audi")

    print(bmw.clean_mark)  # 3

    wash_station = CarWashStation(
        distance_from_city_center=5,
        clean_power=6,
        average_rating=3.5,
        count_of_ratings=6,
    )

    income = wash_station.serve_cars([bmw, audi])

    print(income)  # 6.3
    print(bmw.clean_mark)  # 6


if __name__ == "__main__":
    main()
