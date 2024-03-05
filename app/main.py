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
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        count_washstation = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price_one_car = self.calculate_washing_price(car)
                count_washstation += price_one_car
                self.wash_single_car(car)
        return round(count_washstation, 1)

    def calculate_washing_price(self, car: Car) -> float:
        count_one_washing = (car.comfort_class * (self.clean_power - car.clean_mark)  # noqa: E501
                             * (self.average_rating / self.distance_from_city_center))  # noqa: E501
        return round(count_one_washing, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, nums: float) -> tuple:
        self.average_rating = round(((self.average_rating * self.count_of_ratings + nums)  # noqa: E501
                                     / (self.count_of_ratings + 1)), 1)
        self.count_of_ratings += 1
        return self.average_rating, self.count_of_ratings
