class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        total = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                total += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return total

    def calculate_washing_price(self, car: Car) -> float:
        multiplier_1 = car.comfort_class * (self.clean_power - car.clean_mark)
        multiplier_2 = (self.average_rating / self.distance_from_city_center)
        result = round(multiplier_1 * multiplier_2, 1)
        return result

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark <= self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, mark: int) -> None:
        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings + mark)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
