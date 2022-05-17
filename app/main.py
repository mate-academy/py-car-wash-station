class Car:
    def __init__(
            self,
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

    def serve_cars(self, cars):
        income = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income, 1)

    def calculate_washing_price(self, car):
        clean_rate = self.clean_power - car.clean_mark
        cost_for_wash = car.comfort_class * clean_rate * \
            self.average_rating / self.distance_from_city_center

        return round(cost_for_wash, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, number):
        quantity = self.count_of_ratings
        first_part = quantity / (quantity + 1) * self.average_rating
        second_part = 1 / (quantity + 1) * number
        self.average_rating = round(first_part + second_part, 1)
        self.count_of_ratings += 1
