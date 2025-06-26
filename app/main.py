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
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_rating: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_rating = count_of_rating

    def serve_cars(self, cars_list: list) -> None:
        income = 0
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                income += (
                    car.comfort_class
                    * (self.clean_power - car.clean_mark)
                    * self.average_rating
                    / self.distance_from_city_center
                )
                car.clean_mark = self.clean_power
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        cost = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(cost, 1)
