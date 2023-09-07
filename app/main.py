class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int,
                 average_rating: int, count_of_ratings: int) -> None:
        self.distance = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            income = ((self.clean_power
                       - car.clean_mark)
                      * car.comfort_class
                      * self.average_rating / self.distance)
            return round(income, 1)
        return 0

    def rate_service(self, mark: int) -> None:
        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings + mark)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
