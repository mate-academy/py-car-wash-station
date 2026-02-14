class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: float, brand: str) -> None:
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

    def calculate_washing_price(self, car: Car) -> float:
        if self.clean_power <= car.clean_mark:
            return 0.0

        clean_dif = self.clean_power - car.clean_mark
        washing_price_1 = car.comfort_class * clean_dif
        washing_price_2 = washing_price_1 * self.average_rating
        washing_price = washing_price_2 / self.distance_from_city_center
        return round(washing_price, 1)

    def serve_cars(self, cars_list: list[Car]) -> float:
        total = 0.0
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                total += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        new_sum = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(new_sum / self.count_of_ratings, 1)
