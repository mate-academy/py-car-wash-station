class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        washing_costs = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                washing_costs += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return washing_costs

    def calculate_washing_price(self, car: Car) -> float:
        washing_power_required = self.clean_power - car.clean_mark
        washing_station_demand = (self.average_rating
                                  / self.distance_from_city_center)
        single_washing_cost = round(
            car.comfort_class
            * washing_power_required
            * washing_station_demand,
            1)
        return single_washing_cost

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        sum_of_all_ratings = (self.average_rating
                              * self.count_of_ratings
                              + rating)
        self.count_of_ratings += 1
        self.average_rating = round(sum_of_all_ratings
                                    / self.count_of_ratings,
                                    1)
