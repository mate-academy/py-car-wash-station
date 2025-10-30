class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list[Car]) -> float:
        result = 0.0
        for car in list_of_cars:
            result += self.wash_single_car(car)

        return result

    def calculate_washing_price(self, car: Car) -> float:
        clean_difference = self.clean_power - car.clean_mark
        pre_result = car.comfort_class * clean_difference * self.average_rating
        return pre_result / self.distance_from_city_center

    def wash_single_car(self, car: Car) -> float:
        if self.clean_power > car.clean_mark:
            result = round(self.calculate_washing_price(car), 1)
            car.clean_mark = self.clean_power
            return result

        return 0.0

    def rate_service(self, rate: int) -> None:
        total_previous_rating = self.average_rating * self.count_of_ratings
        new_total_rating = total_previous_rating + rate
        self.average_rating = round(
            new_total_rating / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
