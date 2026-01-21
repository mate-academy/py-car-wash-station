class Car:
    def __init__(self,
                 comfort_class_level: int,
                 clean_mark_score: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class_level
        self.clean_mark = clean_mark_score
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power_level: int,
                 average_service_rating: float,
                 total_service_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power_level
        self.average_rating = average_service_rating
        self.count_of_ratings = total_service_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        clean_diff = self.clean_power - car.clean_mark
        price = (car.comfort_class
                 * clean_diff
                 * self.average_rating
                 / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        pass

    def rate_service(self, single_rate: int) -> None:
        sum_rate = (self.average_rating * self.count_of_ratings) + single_rate
        total_count_rate = self.count_of_ratings + 1
        new_rate = round((sum_rate / total_count_rate), 1)
        self.average_rating = new_rate
        self.count_of_ratings = total_count_rate
