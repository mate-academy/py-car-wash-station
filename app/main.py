class Car:
    def __init__(
        self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self, distance_from_city_center: int, clean_power: int,
        average_rating: float, count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> int:
        total_cost = 0
        has_cleaned_cars = False
        for car in cars:
            if self.clean_power > car.clean_mark:
                single_car_wash_cost = self.calculate_washing_price(car)
                total_cost += single_car_wash_cost
                has_cleaned_cars = True
            self.wash_single_car(car)
        return round(total_cost, 1) if has_cleaned_cars else 0

    def calculate_washing_price(self, car: Car) -> float:
        new_clean_mark = self.clean_power - car.clean_mark
        return (
            (car.comfort_class * new_clean_mark)
            / self.distance_from_city_center
            * self.average_rating
        )

    def wash_single_car(self, car: Car) -> str:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
            return f"{car.brand} помито."
        return "Not worthy enough"

    def rate_service(self, new_rate: int) -> float:
        old_counted_ratings = self.count_of_ratings
        self.count_of_ratings += 1
        new_rating = (
            (self.average_rating * old_counted_ratings + new_rate)
            / self.count_of_ratings
        )
        self.average_rating = round(new_rating, 1)
        return self.average_rating
