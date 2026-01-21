class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
    pass


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: float,
                 average_rating: float, count_of_ratings: int) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = round(count_of_ratings, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:

        new_average_rating = ((self.average_rating
                              * self.count_of_ratings
                              + rate)
                              / (self.count_of_ratings + 1))

        self.average_rating = round(new_average_rating, 1)
        self.count_of_ratings = self.count_of_ratings + 1

    def calculate_washing_price(self, car: Car) -> float:

        return round(
            (car.comfort_class
             * (self.clean_power - car.clean_mark)
             * (self.average_rating / self.distance_from_city_center)),
            1)

    def serve_cars(self, cars: list[Car]) -> float:

        income = 0

        for car in cars:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
                print(income)

        return round(income, 1)
