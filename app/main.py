class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: int,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> int:
        income = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        power_mark_difference = self.clean_power - car.clean_mark
        washing_price = (car.comfort_class
                         * power_mark_difference
                         * self.average_rating
                         / self.distance_from_city_center)
        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        return None

    def rate_service(self, rating: int) -> None:
        new_average = round(
            (self.count_of_ratings * self.average_rating + rating)
            / (self.count_of_ratings + 1),
            1)
        self.count_of_ratings += 1
        self.average_rating = new_average
        return None
