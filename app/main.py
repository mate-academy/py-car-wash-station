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
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark >= self.clean_power:
            return 0.0

        cleanness_difference = self.clean_power - car.clean_mark
        raw_price = (
            car.comfort_class
            * cleanness_difference
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(raw_price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0.0

        for car in cars:
            if car.clean_mark < self.clean_power:
                cleanness_difference = self.clean_power - car.clean_mark
                car_wash_income = (
                    car.comfort_class
                    * cleanness_difference
                    * self.average_rating
                    / self.distance_from_city_center
                )
                total_income += car_wash_income
                self.wash_single_car(car)

        return round(total_income, 1)

    def rate_service(self, rating: int) -> None:
        current_total_rating = self.average_rating * self.count_of_ratings
        new_total_rating = current_total_rating + rating
        self.count_of_ratings += 1
        calculated_rating = new_total_rating / self.count_of_ratings
        self.average_rating = round(calculated_rating, 1)
