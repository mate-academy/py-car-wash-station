class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        diff = self.clean_power - car.clean_mark
        base = car.comfort_class * diff
        return base * self.average_rating / self.distance_from_city_center

    def serve_cars(self, cars: list) -> float:
        sum_income = 0
        for car in cars:
            sum_income += self.wash_single_car(car)
        return round(sum_income, 1)

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            income = round(self.calculate_washing_price(car), 1)
            car.clean_mark = self.clean_power
            return income
        else:
            return 0

    def rate_service(self, rating: float) -> None:
        rating_sum = (self.average_rating * self.count_of_ratings + rating)
        self.count_of_ratings = self.count_of_ratings + 1
        self.average_rating = round(rating_sum / self.count_of_ratings, 1)
