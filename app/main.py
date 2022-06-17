class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
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

    def serve_cars(self, cars: list):
        income = 0
        fit_cars = []
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                fit_cars.append(car)

        for fit_car in fit_cars:
            self.wash_single_car(fit_car)

        return round(income, 1)

    def calculate_washing_price(self, other):
        price = other.comfort_class * (self.clean_power - other.clean_mark) * \
            (self.average_rating / self.distance_from_city_center)

        return round(price, 1)

    def wash_single_car(self, other):
        if self.clean_power > other.clean_mark:
            other.clean_mark = self.clean_power

        return other

    def rate_service(self, rating):
        all_ratings = self.average_rating * self.count_of_ratings + rating
        self.count_of_ratings += 1
        self.average_rating = round((all_ratings / self.count_of_ratings), 1)
