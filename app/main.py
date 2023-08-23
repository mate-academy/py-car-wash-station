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
                 clean_power: float,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        all_cost = 0
        if cars:
            for car in cars:
                all_cost += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return all_cost

    def calculate_washing_price(self, car: Car) -> int:
        if car.clean_mark <= self.clean_power:
            cost_of_washing = round(
                car.comfort_class * (self.clean_power - car.clean_mark)
                * self.average_rating / self.distance_from_city_center, 1
            )
        else:
            cost_of_washing = 0
        return cost_of_washing

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        self.count_of_ratings += 1
        self.average_rating = round(
            (self.average_rating * (self.count_of_ratings - 1) + rating)
            / self.count_of_ratings, 1)
