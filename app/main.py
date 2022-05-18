class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ):
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

    def can_wash_car(self, car):
        return self.clean_power >= car.clean_mark

    def calculate_washing_price(self, car):
        if self.can_wash_car(car):
            return round(
                car.comfort_class * (
                    self.clean_power - car.clean_mark
                ) * self.average_rating / self.distance_from_city_center,
                1)

    def serve_cars(self, list_of_cars: list):
        income = 0
        for car in list_of_cars:
            if self.can_wash_car(car):
                income += (
                    car.comfort_class * (
                        self.clean_power - car.clean_mark
                    ) * self.average_rating / self.distance_from_city_center
                )
                car.clean_mark = self.clean_power
        return round(income, 1)

    def wash_single_car(self, car):
        if self.can_wash_car(car):
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int):
        rating = (self.average_rating * self.count_of_ratings + rate) / \
                 (self.count_of_ratings + 1)
        self.average_rating = round(rating, 1)
        self.count_of_ratings += 1
