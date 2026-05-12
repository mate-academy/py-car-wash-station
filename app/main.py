class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        handled_cars = [car for car in cars
                        if car.clean_mark < self.clean_power]
        for handled_car in handled_cars:
            income += self.calculate_washing_price(handled_car)
            self.wash_single_car(handled_car)
        income = round(income, 1)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        difference_clean = self.clean_power - car.clean_mark
        comfort_clean = car.comfort_class * difference_clean
        rating_clean = comfort_clean * self.average_rating
        cost = round(rating_clean / self.distance_from_city_center, 1)
        return cost

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rating: int) -> None:
        new_average_rating = round(((self.average_rating
                                     * self.count_of_ratings)
                                    + new_rating)
                                   / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
        self.average_rating = new_average_rating
