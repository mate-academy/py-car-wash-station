class Car:
    def __init__(
            self,
            comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float, clean_power: int,
            average_rating: float, count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                rounded_rating = round(self.average_rating, 1)
                difference_of_purity = self.clean_power - car.clean_mark
                clean_rating = difference_of_purity * rounded_rating
                cost_multiplier = car.comfort_class * clean_rating
                income += cost_multiplier / self.distance_from_city_center
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        income = 0
        if self.clean_power > car.clean_mark:
            rounded_rating = round(self.average_rating, 1)
            difference_of_purity = self.clean_power - car.clean_mark
            clean_rating = difference_of_purity * rounded_rating
            cost_multiplier = car.comfort_class * clean_rating
            income += cost_multiplier / self.distance_from_city_center
        return round(income, 1)

    def wash_single_car(self, car: Car) -> Car:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
            return car

    def rate_service(self, rating: int) -> None:
        rounded_rating = round(self.average_rating, 1)
        total_score = self.count_of_ratings * rounded_rating + rating
        self.count_of_ratings += 1
        self.average_rating = round(total_score / self.count_of_ratings, 1)
