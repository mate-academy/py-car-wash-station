class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center,
            clean_power,
            average_rating,
            count_of_ratings
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list):
        cars = [
            auto
            for auto in car_list
            if auto.clean_mark <= self.clean_power
        ]
        income = sum([self.calculate_washing_price(car) for car in cars])
        for c in cars:
            c.clean_mark = self.clean_power
        return income

    def calculate_washing_price(self, auto: Car):
        if auto.clean_mark <= self.clean_power:
            rate_diff = self.clean_power - auto.clean_mark
            coff_rates = auto.comfort_class * rate_diff * self.average_rating
            price_for_one = (coff_rates / self.distance_from_city_center)
            return round(price_for_one, 1)

    def wash_single_car(self, auto: Car):
        return True if auto.clean_mark <= self.clean_power else False

    def rate_service(self, rate: int):
        all_rates = (self.average_rating * self.count_of_ratings + rate)
        self.average_rating = round(
            (all_rates / (self.count_of_ratings + 1)), 1
        )
        self.count_of_ratings = (self.count_of_ratings + 1)
        return
