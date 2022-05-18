class Car:

    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        cash = []
        for car in cars:
            if car.clean_mark < self.clean_power:
                cash.append(self.calculate_washing_price(car))
                self.wash_single_car(car)
        return sum(cash)

    def calculate_washing_price(self, one_car: Car):
        difference_clean = self.clean_power - one_car.clean_mark
        rating = self.average_rating / self.distance_from_city_center
        price = one_car.comfort_class * difference_clean * rating
        return round(price, 1)

    def wash_single_car(self, single_car: Car):
        if single_car.clean_mark < self.clean_power:
            single_car.clean_mark = self.clean_power
        return single_car

    def rate_service(self, rating):
        overall_score = self.average_rating * self.count_of_ratings + rating
        self.count_of_ratings = self.count_of_ratings + 1
        self.average_rating = round(overall_score / self.count_of_ratings, 1)
        return self.average_rating
