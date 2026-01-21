class Car:
    def __init__(
            self, comfort_class: int, clean_mark: int, brand: int) -> None:
        if not (1 <= comfort_class <= 7):
            raise ValueError("comfort_class must be between 1 and 7")
        if not (1 <= clean_mark <= 10):
            raise ValueError("clean_mark must be between 1 and 10")
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: int,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        if not (1 <= distance_from_city_center <= 10):
            raise ValueError(
                "distance_from_city_center must be between 1 and 10"
            )
        if not (0.0 <= average_rating <= 5.0):
            raise ValueError("average_rating must be between 0.0 and 5.0")
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        factor2 = self.clean_power - car.clean_mark
        factor3 = self.average_rating / self.distance_from_city_center
        return (car.comfort_class * factor2 * factor3)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def serve_cars(self, car_list: list) -> float:
        cust = 0
        for car in car_list:
            if car.clean_mark < self.clean_power:
                cust = cust + round(self.calculate_washing_price(car), 1)
                self.wash_single_car(car)
        return cust

    def rate_service(self, rating: int) -> None:
        sum_rating = self.average_rating * self.count_of_ratings
        new_sum = sum_rating + rating
        self.count_of_ratings += 1
        self.average_rating = round(new_sum / self.count_of_ratings, 1)
