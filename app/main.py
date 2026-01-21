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
        count_of_ratings: int,
    ) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:

        price = 0.0

        for car in cars:

            if car.clean_mark < self.clean_power:

                car_income = self.calculate_washing_price(car)
                price += car_income
                car.clean_mark = self.wash_single_car()

        return round(price, 1)

    def calculate_washing_price(self, car: Car) -> float:

        clean_diff = self.clean_power - car.clean_mark
        car_income = (
            car.comfort_class * clean_diff * self.average_rating
        ) / self.distance_from_city_center
        return round(car_income, 1)

    def wash_single_car(self) -> int:

        return self.clean_power

    def rate_service(self, single_rate: float) -> None:

        new_rating = round(
            (self.average_rating * self.count_of_ratings + single_rate)
            / (self.count_of_ratings + 1),
            1,
        )
        self.count_of_ratings += 1
        self.average_rating = new_rating
