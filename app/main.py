class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:

        if comfort_class not in range(1, 8):
            self.comfort_class = 1
        else:
            self.comfort_class = comfort_class

        if clean_mark not in range(1, 11):
            self.clean_mark = 1
        else:
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

        if not 1.0 <= distance_from_city_center <= 10.0:
            self.distance_from_city_center = 1
        else:
            self.distance_from_city_center = distance_from_city_center

        self.clean_power = clean_power

        if not 1.0 <= average_rating <= 5.0:
            self.average_rating = 1
        else:
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
        clean_diff = self.clean_power - car.clean_mark
        if clean_diff <= 0:
            return 0.0
        washing_price = (car.comfort_class
                         * clean_diff
                         * self.average_rating
                         / self.distance_from_city_center)

        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        if 1 <= rate <= 5:
            new_count_of_ratings = self.count_of_ratings + 1
            new_average_rating = (
                self.average_rating * self.count_of_ratings
                + rate
            ) / new_count_of_ratings

            self.average_rating = round(new_average_rating, 1)
            self.count_of_ratings = new_count_of_ratings
