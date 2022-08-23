class Car:
    def __init__(self, comfort_class: float, clean_mark: float, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: float,
                 average_rating: float, count_of_ratings: float):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car):
        if self.clean_power >= car.clean_mark:
            difference = (self.clean_power - car.clean_mark)
            division = self.average_rating / self.distance_from_city_center
            return round(car.comfort_class * difference * division, 1)

    def serve_cars(self, cars: list):
        amount = 0
        for car in cars:
            if self.clean_power >= car.clean_mark:
                amount += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return amount

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int):
        sum_rating = self.average_rating * self.count_of_ratings
        sum_rating += rate
        self.count_of_ratings += 1
        new_average_rating = sum_rating / self.count_of_ratings
        self.average_rating = round(new_average_rating, 1)
