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
            count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: list) -> list:
        price = car.comfort_class * (self.clean_power - car.clean_mark)
        total_price = price * self.average_rating
        result = total_price / self.distance_from_city_center
        return round(result, 1)

    def wash_single_car(self, car: list) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: list) -> None:
        result = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        result += rate
        self.average_rating = round(result / self.count_of_ratings, 1)

    def serve_cars(self, cars: list) -> int:
        result = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                result += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return result
