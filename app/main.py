class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power,
                 average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        income = 0
        for car in cars:
            if self.clean_power >= car.clean_mark:
                income += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return income

    def calculate_washing_price(self, car):
        price = car.comfort_class * (self.clean_power - car.clean_mark) \
            * self.average_rating / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car):
        if self.clean_power >= car.clean_mark:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price

    def rate_service(self, rating):
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rating)
            / (self.count_of_ratings + 1), 1
        )
        self.count_of_ratings += 1
