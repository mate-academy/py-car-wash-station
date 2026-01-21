class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ) -> None:
        self.income = 0
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_list: list) -> float:
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                self.income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(self.income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        comfort_class = car.comfort_class
        washing_operation = self.clean_power - car.clean_mark
        rating_div_dist = self.average_rating / self.distance_from_city_center
        washing_price = comfort_class * washing_operation * rating_div_dist

        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark: int) -> None:
        total_rating = self.average_rating * self.count_of_ratings + mark
        self.count_of_ratings += 1
        current_rating = round(total_rating / self.count_of_ratings, 1)
        self.average_rating = current_rating
