class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str,
    ) -> None:
        self.comfort_class = max(1, min(7, comfort_class))
        self.clean_mark = max(1, min(10, clean_mark))
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: float,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = max(
            1.0, min(11.0, distance_from_city_center)
        )
        self.clean_power = max(1.0, min(10.0, clean_power))
        self.average_rating = round(max(1.0, min(5.0, average_rating)), 1)
        self.count_of_ratings = max(0, count_of_ratings)

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark >= self.clean_power:
            return 0.0

        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, car_list: list[Car]) -> float:
        total_income = 0.0

        for car in car_list:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
            self.wash_single_car(car)

        return round(total_income, 1)

    def rate_service(self, rate: float) -> None:
        total_rating = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(
            total_rating / self.count_of_ratings, 1
        )
