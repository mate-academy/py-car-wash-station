class Car:
    def __init__(
            self, comfort_class: int,
            clean_mark: int,
            brand: str
    ):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int
                 ):

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        income = 0

        for auto in cars:
            if auto.clean_mark < self.clean_power:
                income += self.calculate_washing_price(auto)
            self.wash_single_car(auto)

        return round(income, 1)

    def calculate_washing_price(self, auto):
        mark_diff = self.clean_power - auto.clean_mark
        price = auto.comfort_class *\
            mark_diff * self.average_rating /\
            self.distance_from_city_center

        return price

    def wash_single_car(self, auto):
        if auto.clean_mark < self.clean_power:
            auto.clean_mark = self.clean_power

    def rate_service(self, rate: int):
        sum_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating =\
            round((sum_rating + rate) / self.count_of_ratings, 1)

        return self.average_rating
