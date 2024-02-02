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

    def calculate_washing_price(self, car: object) -> float:
        cost_for_wash = round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center,
            1
        )
        return cost_for_wash

    def wash_single_car(self, car: object) -> None:
        if car.clean_mark <= self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rate: int) -> None:
        fully_old_rate = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round(
            (fully_old_rate + new_rate) / self.count_of_ratings,
            1
        )

    def serve_cars(self, cars_box: list[object]) -> float:
        sum_of_washed_car = 0
        for car_object in cars_box:
            if car_object.clean_mark < self.clean_power:
                sum_of_washed_car += self.calculate_washing_price(car_object)
                self.wash_single_car(car_object)
        return sum_of_washed_car
