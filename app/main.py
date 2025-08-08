class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: float,
        brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: float,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list[Car]) -> float:
        total_cost = 0
        for car in car_list:
            total_cost += self.wash_single_car(car)
        return round(total_cost, 1)

    def calculate_washing_price(self, car: Car) -> float:
        cost_price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return cost_price

    def wash_single_car(self, car: Car) -> float:
        total_cost = 0
        if car.clean_mark < self.clean_power:
            total_cost = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
        return total_cost

    def rate_service(self, rate: float) -> None:
        total = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round((total + rate) / self.count_of_ratings, 1)
