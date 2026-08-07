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
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            (car.comfort_class
             * (self.clean_power - car.clean_mark)
             * (self.average_rating / self.distance_from_city_center)
             ),
            1
        )

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        result = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                result += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return result

    def rate_service(self, rating: int) -> None:
        if 0 <= rating <= 5:
            self.count_of_ratings += 1
            self.average_rating = round(
                ((self.average_rating * (self.count_of_ratings - 1) + rating)
                 / self.count_of_ratings
                 ),
                1
            )
        else:
            print("Please enter correct rating in range 0 to 5")
