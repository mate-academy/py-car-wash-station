class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list[Car]) -> float:
        income = 0
        result_list = [car for car in list_of_cars
                       if car.clean_mark < self.clean_power]
        for car in result_list:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        comfort = car.comfort_class
        delta = self.clean_power - car.clean_mark
        a_rate = self.average_rating
        distance = self.distance_from_city_center
        return round(comfort * delta * a_rate / distance, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rate: int) -> None:
        self.count_of_ratings += 1
        the_rate = round((self.average_rating
                          * (self.count_of_ratings - 1) + new_rate)
                         / self.count_of_ratings, 1)
        self.average_rating = the_rate
