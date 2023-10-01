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
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
        self.income = 0.0

    def serve_cars(self, list_of_cars: list) -> float:
        for car in list_of_cars:
            self.wash_single_car(car)
        return self.income

    def calculate_washing_price(self, car: Car) -> float:
        washing_cost = round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
            , 1)
        return washing_cost

    def rate_service(self, new_rate: int) -> float:
        new_sum = (self.average_rating * self.count_of_ratings) + new_rate
        self.count_of_ratings += 1

        self.average_rating = round(new_sum / self.count_of_ratings, 1)

        return self.average_rating

    def wash_single_car(self, car: Car) -> float:
        if self.clean_power > car.clean_mark:
            self.income += self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
        return self.income
