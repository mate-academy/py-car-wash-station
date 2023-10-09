class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str)\
            -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> int:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = car.comfort_class * (self.clean_power - car.clean_mark)
        calc_price = price * self.average_rating
        return round(calc_price / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        new_rating = total_rating + rating
        self.count_of_ratings += 1
        new_average_rating = new_rating / self.count_of_ratings
        self.average_rating = round(new_average_rating, 1)
