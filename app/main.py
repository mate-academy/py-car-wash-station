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
            count_of_ratings: int
    ) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def rate_service(self, rate: int) -> None:
        self.average_rating = round(((self.count_of_ratings
                                      * self.average_rating + rate)
                                     / (self.count_of_ratings + 1)), 1)
        self.count_of_ratings += 1

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        diff = self.clean_power - car.clean_mark
        return round((car.comfort_class * diff
                      * self.average_rating)
                     / self.distance_from_city_center, 1)

    def serve_cars(self, car_list: list) -> float:
        total_income = 0
        for car in car_list:
            if car.clean_mark < self.clean_power:
                washing_price = self.calculate_washing_price(car)
                self.wash_single_car(car)
                total_income += washing_price
        return round(total_income, 1)
