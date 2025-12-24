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
        if self.distance_from_city_center == 0:
            return 0
        power_difference = self.clean_power - car.clean_mark
        weighted_rating = power_difference * self.average_rating
        car_score = car.comfort_class * weighted_rating
        price = car_score / self.distance_from_city_center
        return round(price, 2)  # округлення до 2 знаків

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
            return self.calculate_washing_price(car)
        return 0

    def serve_cars(self, cars: list[Car]) -> float:
        total_price = 0
        for car in cars:
            price = self.wash_single_car(car)  # виклик лише один раз
            total_price += price
        return round(total_price, 2)

    def rate_service(self, rate: int) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += rate
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 2)
