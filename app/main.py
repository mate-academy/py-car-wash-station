class Car:
    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self, distance_from_city_center: int,
            clean_power: int,
            average_rating: int,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: object) -> float:
        result_calculate = ((car.comfort_class * self.average_rating
                             * (self.clean_power - car.clean_mark))
                            / self.distance_from_city_center)
        return round(result_calculate, 1)

    def wash_single_car(self, car: object) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, list_cars: list) -> float:
        result_cost = sum(
            self.calculate_washing_price(car)
            for car in list_cars
            if self.clean_power > car.clean_mark
        )
        for car in list_cars:
            self.wash_single_car(car)
        return result_cost

    def rate_service(self, rate: int) -> None:
        result_new_rate = (((self.average_rating * self.count_of_ratings)
                            + rate) / (self.count_of_ratings + 1))

        self.average_rating = round(result_new_rate, 1)
        self.count_of_ratings += 1
