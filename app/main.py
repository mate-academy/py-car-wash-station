class Car (object):
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation (object):
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        total_price = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                total_price += self.calculate_washing_price(car)
                total_price = round(total_price, 1)
                self.wash_single_car(car)

        return total_price

    def calculate_washing_price(self, car: Car) -> float:
        price = car.comfort_class \
            * (self.clean_power - car.clean_mark) \
            * (self.average_rating / self.distance_from_city_center)

        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        total_rates = (self.average_rating * self.count_of_ratings + rate)
        self.average_rating = total_rates / (self.count_of_ratings + 1)
        self.average_rating = round(self.average_rating, 1)
        self.count_of_ratings += 1
