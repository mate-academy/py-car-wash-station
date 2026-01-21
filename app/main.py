def validate(
        real_value: int = 1,
        min_val: int | float = 1,
        max_val: int | float = 1
) -> int | float:
    return real_value if min_val <= real_value <= max_val else min_val


class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = validate(comfort_class, 1, 7)
        self.clean_mark = validate(clean_mark, 1, 10)
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: int,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = (
            validate(distance_from_city_center, 1.0, 10.0)
        )
        self.clean_power = clean_power
        self.average_rating = validate(average_rating, 1.0, 5.0)
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        difference = self.clean_power - car.clean_mark
        multiply = car.comfort_class * difference * self.average_rating
        cost = multiply / self.distance_from_city_center
        return round(cost, 1)

    def serve_cars(self, cars: Car) -> int:
        total = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return total

    def rate_service(self, rate: int) -> None:
        total_rate = self.count_of_ratings * self.average_rating
        total_rate += rate
        self.count_of_ratings += 1
        self.average_rating = round(total_rate / self.count_of_ratings, 1)
