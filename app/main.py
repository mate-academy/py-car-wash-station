class Car:

    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_cars: list):
        income_list: list = []
        for car in list_cars:
            if car.clean_mark < self.clean_power:
                income_list.append(self.calculate_washing_price(car))
                self.wash_single_car(car)
        return round(sum(income_list), 1)

    def calculate_washing_price(self, car: Car):
        temp = (car.comfort_class * (self.clean_power - car.clean_mark))
        result = temp * self.average_rating / self.distance_from_city_center
        return round(result, 1)

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float):
        self.count_of_ratings += 1
        temp = self.count_of_ratings - 1
        sum_of_ratings = (self.average_rating * temp) + rating
        result = sum_of_ratings / self.count_of_ratings
        self.average_rating = round(result, 1)
