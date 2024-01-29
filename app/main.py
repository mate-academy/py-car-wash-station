class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class: int = comfort_class
        self.clean_mark: int = clean_mark
        self.brand: str = brand

class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center: float = distance_from_city_center
        self.clean_power: int = clean_power
        self.average_rating: float = average_rating
        self.count_of_ratings: int = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        total_income: 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                self.wash_single_car(car)
                total_income += self.calculate_washing_price(car)
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        if self.clean_power > car.clean_mark:
            wash_cost: float = (
                car.comfort_class *
                (self.clean_power - car.clean_mark) *
                self.average_rating / self.distance_from_city_center
            )
            return round(wash_cost, 1)
        else:
            return 0.0

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        new_total_rating: float = self.average_rating * self.count_of_ratings + rating
        self.count_of_ratings += 1
        self.average_rating = round(new_total_rating / self.count_of_ratings, 1)

    pass
