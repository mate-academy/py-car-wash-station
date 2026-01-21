class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
    ) -> None:
        self.comfort_class = min(max(1, comfort_class), 7)
        self.clean_mark = min(max(1, clean_mark), 10)
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = min(
            max(1.0, distance_from_city_center), 10.0
        )
        self.clean_power = min(max(1, clean_power), 10)
        self.average_rating = round(
            min(max(1.0, average_rating), 5.0), 1
        )
        self.count_of_ratings = max(0, count_of_ratings)

    def calculate_washing_price(self, car: Car) -> float:
        diff = self.clean_power - car.clean_mark
        if diff <= 0:
            return 0.0
        price = (
            car.comfort_class
            * diff
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        total = 0.0
        for car in cars:
            price = self.calculate_washing_price(car)
            if price > 0:
                total += price
                self.wash_single_car(car)
        return round(total, 1)

    def rate_service(self, rate: float) -> None:
        total_sum = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round(
            (total_sum + rate) / self.count_of_ratings, 1
        )
