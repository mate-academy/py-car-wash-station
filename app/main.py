class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating : float,
                 count_of_ratings: int) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        return (car.comfort_class
                * (self.clean_power - car.clean_mark)
                * (self.average_rating / self.distance_from_city_center))

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            return CarWashStation.calculate_washing_price(self, car)
        return 0

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            income += CarWashStation.wash_single_car(self, car)
            income = round(income, 2)
            if car.clean_mark < self.clean_power:
                car.clean_mark = self.clean_power
        return income

    def rate_service(self, rate: int) -> None:
        self.count_of_ratings += 1
        old_price_component = (self.average_rating
                               * ((self.count_of_ratings - 1)
                                  / self.count_of_ratings))
        new_price_component = (rate * (1 / self.count_of_ratings))
        self.average_rating = (old_price_component + new_price_component)
        self.average_rating = round(self.average_rating, 1)
