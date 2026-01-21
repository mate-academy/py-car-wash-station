class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
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
        income = 0
        for car in cars:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, single_car):
        power = self.clean_power
        distance = self.distance_from_city_center
        part_price = single_car.comfort_class * (power - single_car.clean_mark)
        price = part_price * self.average_rating / distance
        if single_car.clean_mark < power:
            return round(price, 1)
        return 0

    def wash_single_car(self, single_car):
        if single_car.clean_mark < self.clean_power:
            single_car.clean_mark = self.clean_power

    def rate_service(self, rate: int):
        new_count_of_ratings = self.count_of_ratings + 1
        all_rates = self.average_rating * self.count_of_ratings
        new_rate = (all_rates + rate) / new_count_of_ratings
        self.average_rating = round(new_rate, 1)
        self.count_of_ratings = new_count_of_ratings
