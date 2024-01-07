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
        price_per_wash = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price_per_wash += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(price_per_wash, 1)

    def calculate_washing_price(self, car: Car) -> float:
        comfort = car.comfort_class
        power = self.clean_power
        rating = self.average_rating
        distance = self.distance_from_city_center

        cost_wash = comfort * (power - car.clean_mark) * rating / distance

        return round(cost_wash, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        sum_rate = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(sum_rate / self.count_of_ratings, 1)
