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
            count_of_rating: float
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_rating

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, list_cars: list) -> float:
        washing_cost = 0
        for car in list_cars:
            if car.clean_mark < self.clean_power:
                washing_cost += round(self.calculate_washing_price(car), 1)
                self.wash_single_car(car)
        return washing_cost

    def rate_service(self, rating: float) -> None:
        total_average = self.average_rating * self.count_of_ratings
        total_average += rating
        self.count_of_ratings += 1
        self.average_rating = round(total_average / self.count_of_ratings, 1)
