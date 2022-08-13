class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance: float,
                 clean_power: int,
                 avr_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance
        self.clean_power = clean_power
        self.average_rating = avr_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car):
        price_dif = self.clean_power - car.clean_mark
        price_mult = car.comfort_class * price_dif * self.average_rating
        price = price_mult / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int):
        current_rating = self.count_of_ratings * self.average_rating
        new_raring = current_rating + rate
        self.count_of_ratings += 1
        self.average_rating = round(new_raring / self.count_of_ratings, 1)
