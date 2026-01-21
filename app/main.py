class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = round(distance_from_city_center, 1)
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        price = (car.comfort_class * (self.clean_power - car.clean_mark)
                 * self.average_rating / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> bool:
        result = car.clean_mark < self.clean_power
        return result

    def serve_cars(self, cars: list) -> float:
        result = 0.0
        for car in cars:
            if self.wash_single_car(car):
                result += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return result

    def rate_service(self, num: int) -> None:
        self.average_rating = round(((self.count_of_ratings
                                     * self.average_rating + num)
                                    / (self.count_of_ratings + 1)), 1)
        self.count_of_ratings += 1
