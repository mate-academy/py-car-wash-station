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
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ) -> None:
        self.distance = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car: list) -> float:
        served_cars_list = []
        income = 0
        for item in car:
            if item.clean_mark < self.clean_power:
                served_cars_list.append(item)
        for car in served_cars_list:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: classmethod) -> float:
        return (car.comfort_class
                * (self.clean_power - car.clean_mark)
                * self.average_rating / self.distance)

    def wash_single_car(self, car: classmethod) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        self.average_rating = round(((self.count_of_ratings
                                      * self.average_rating + rate)
                                     / (self.count_of_ratings + 1)), 1)
        self.count_of_ratings += 1
