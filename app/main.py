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
            distance_from_city_center: int,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        total_wash_price = 0
        for car in cars:
            if self.wash_single_car(car):
                total_wash_price += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power

        return total_wash_price

    def calculate_washing_price(self, car: Car) -> float:
        multiplication_top = (car.comfort_class * self.average_rating
                              * (self.clean_power - car.clean_mark))
        return round(multiplication_top / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> bool:
        return car.clean_mark < self.clean_power

    def rate_service(self, service_mark: int) -> None:
        multiplication_top = (self.average_rating
                              * self.count_of_ratings + service_mark)
        self.average_rating = round(multiplication_top
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
