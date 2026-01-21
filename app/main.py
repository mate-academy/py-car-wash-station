class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        if comfort_class not in range(1, 8):
            raise ValueError(
                f"Value must be in range from 1 to 7. Got {comfort_class}."
            )
        if clean_mark not in range(1, 11):
            raise ValueError(
                f"Value must be in range from 1 to 10. Got {clean_mark}."
            )

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
        if not 1.0 <= distance_from_city_center <= 10.1:
            raise ValueError(
                f"Value must be in range from 1.0 to 10.0. "
                f"Got {distance_from_city_center}."
            )
        if not 1.0 <= average_rating <= 5.1:
            raise ValueError(
                f"Value must be in range from 1.0 to 5.0. "
                f"Got {average_rating}"
            )
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        one_car_income = []
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                one_car_income.append(price)
                self.wash_single_car(car)
        return round(sum(one_car_income), 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * (self.average_rating / self.distance_from_city_center), 1)
        return price

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rating: int) -> None:
        sum_of_ratings = self.average_rating * self.count_of_ratings
        sum_of_ratings += new_rating
        self.count_of_ratings += 1
        new_avg_rating = round(sum_of_ratings / self.count_of_ratings, 1)
        self.average_rating = new_avg_rating
