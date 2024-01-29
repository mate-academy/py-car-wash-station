class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(
            self,
            distance_from_city_center: int,
            clean_power: int,
            average_rating: float,
            count_of_ratings: float) -> None:
        self.clean_power = clean_power
        self.count_of_ratings = count_of_ratings
        self.distance_from_city_center = distance_from_city_center
        self.average_rating = average_rating

    def serve_cars(self, cars: list) -> float:
        total_price = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                total_price += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_price, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = (car.comfort_class * (self.clean_power - car.clean_mark)
                 * self.average_rating / self.distance_from_city_center)
        return price

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, single_rate: int) -> None:
        self.count_of_ratings += 1
        new_average = (single_rate + self.average_rating
                       * (self.count_of_ratings - 1)) / self.count_of_ratings
        self.average_rating = round(new_average, 1)
