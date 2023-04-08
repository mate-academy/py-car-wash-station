class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_cars: list[Car]) -> float:
        wash_sum = 0
        for car_mark in list_cars:
            if car_mark.clean_mark < self.clean_power:
                wash_sum += self.calculate_washing_price(car_mark)
                self.wash_single_car(car_mark)
        return round(wash_sum, 1)

    def calculate_washing_price(self, car_mark: Car) -> float:
        return round(car_mark.comfort_class *
                     (self.clean_power - car_mark.clean_mark) *
                     self.average_rating /
                     self.distance_from_city_center, 1)

    def wash_single_car(self, car_mark: Car) -> None:
        car_mark.clean_mark = self.clean_power

    def rate_service(self, info_rating: float) -> None:
        self.average_rating = round((
                                self.average_rating *
                                self.count_of_ratings +
                                info_rating) /
                                (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
