class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int,
                 clean_power: int,
                 average_rating: int,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        cost = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                cost += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return cost

    def calculate_washing_price(self, car: Car) -> float:
        dif = self.clean_power - car.clean_mark
        class_rating = car.comfort_class * self.average_rating
        calc_wash_price = class_rating * dif / self.distance_from_city_center
        return round(calc_wash_price, 1)

    def wash_single_car(self, car: Car) -> Car:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        new_rating_sum = self.average_rating * self.count_of_ratings + rate
        new_count_of_rating = self.count_of_ratings + 1
        self.count_of_ratings += 1
        self.average_rating = round(new_rating_sum / new_count_of_rating, 1)
