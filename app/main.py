class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list) -> int:
        price = 0
        for car in car_list:
            if car.clean_mark < self.clean_power:
                price += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return price

    def calculate_washing_price(self, car: Car) -> float:
        clean_diferent = self.clean_power - car.clean_mark
        rate_cof = self.average_rating / self.distance_from_city_center
        car_wash_price = round(car.comfort_class
                               * clean_diferent
                               * rate_cof, 1,)
        return car_wash_price

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, mark: int) -> None:
        count = self.count_of_ratings
        self.average_rating = round(((self.average_rating
                                    * count) + mark)
                                    / (count + 1), 1)
        self.count_of_ratings += 1
