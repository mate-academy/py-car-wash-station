class Car:
    def __init__(self,
                 comfort_class: int, clean_mark: int, brand: str) -> None:
        # if error set maximum value of comfort_class
        self.comfort_class = comfort_class if 1 <= comfort_class <= 7 else 7
        # if error set minimum value clean_mark
        self.clean_mark = clean_mark if 1 <= clean_mark <= 10 else 1
        self.brand = brand


class CarWashStation():
    def __init__(self,
                 distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        amount = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                amount += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return amount

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center,
            1)

    def rate_service(self, rating: float) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rating)
            / (self.count_of_ratings + 1),
            1)
        self.count_of_ratings += 1
