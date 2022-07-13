class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self, distance_from_city_center: float,
            clean_power: float,
            average_rating: float,
            count_of_ratings: int
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_cars):
        sum_all_car = 0
        for one_car in list_cars:
            if one_car.clean_mark <= self.clean_power:
                sum_all_car += self.calculate_washing_price(one_car)
                self.wash_single_car(one_car)
        return sum_all_car

    def calculate_washing_price(self, car):
        clean_car = self.clean_power - car.clean_mark
        rating_distance = self.average_rating / self.distance_from_city_center
        return round(
            car.comfort_class * clean_car * rating_distance, 1)

    def wash_single_car(self, wash_car):
        if wash_car.clean_mark < self.clean_power:
            wash_car.clean_mark = self.clean_power
        return wash_car.clean_mark

    def rate_service(self, rate):
        rating = self.average_rating * self.count_of_ratings + rate
        self.average_rating = round(rating / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
