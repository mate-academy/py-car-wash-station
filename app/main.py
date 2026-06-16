class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
    ) -> None:
        if not 1 <= comfort_class <= 7:
            raise ValueError("Class must be in 1 to 7")
        if not 1 <= clean_mark <= 10:
            raise ValueError("Mark must be in 1 to 10")
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
        if not 1.0 <= distance_from_city_center <= 10.0:
            raise ValueError("Distance must be in 1.0 to 10.0")
        if not 1.0 <= average_rating <= 5.0:
            raise ValueError("Rating must be in 1.0 to 5.0")
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_list: list[Car]) -> float:
        total_price = sum(
            [
                self.calculate_washing_price(car)
                for car in cars_list
                if car.clean_mark < self.clean_power
            ]
        )
        for car in cars_list:
            self.wash_single_car(car)
        return round(total_price, 1)

    def calculate_washing_price(self, car: Car) -> float:
        washing_price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )

        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> Car | None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
            return car
        return None

    def rate_service(self, rating: int) -> None:
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be in 1 to 5")
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rating)
            / (self.count_of_ratings + 1),
            1,
        )
        self.count_of_ratings += 1
