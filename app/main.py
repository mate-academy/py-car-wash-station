class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def rate_service(self, rate: int) -> tuple:
        self.average_rating = round(
            ((self.average_rating * self.count_of_ratings) + rate)
            / (self.count_of_ratings + 1), 1
        )
        self.count_of_ratings += 1
        return self.average_rating, self.count_of_ratings

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        difference_power_and_mark = self.clean_power - car.clean_mark
        multiplied_parameters = (
            car.comfort_class
            * difference_power_and_mark
            * self.average_rating
        )
        result = round(
            multiplied_parameters / self.distance_from_city_center, 1
        )
        return result

    def serve_cars(self, cars: list) -> int:
        result = 0

        for car in cars:
            if self.clean_power > car.clean_mark:
                result += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return result
