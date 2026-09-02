class Car:
    def __init__(self,
                 comfort_class: str,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: object) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: object) -> float:
        diff = self.clean_power - car.clean_mark
        price = (car.comfort_class
                 * diff
                 * self.average_rating
                 / self.distance_from_city_center
                 )
        return round(price, 1)

    def rate_service(self, rate_service: int) -> None:
        self.average_rating = round(
            (self.average_rating
             * self.count_of_ratings
             + rate_service) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

    def serve_cars(self, cars: list) -> float:
        total_price = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_price += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_price, 1)
