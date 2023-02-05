class Car:

    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        if not isinstance(comfort_class and clean_mark, int):
            raise TypeError(" Comfort class and clean mark"
                            " must be only positive integer")
        if not isinstance(brand, str):
            raise TypeError("Brand must be only string")
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

    def __str__(self) -> str:
        return f"Comfort class - {self.comfort_class}, " \
               f"clean mark - {self.clean_mark}, brand - {self.brand}"


class CarWashStation:

    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        if not isinstance(clean_power and count_of_ratings, int):
            raise TypeError("Clean power and count of ratings"
                            " must be only positive integer")
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        first_part = car.comfort_class * (self.clean_power - car.clean_mark)
        sec_part = (self.average_rating / self.distance_from_city_center)
        return round(first_part * sec_part, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, tax: float) -> None:
        average = self.average_rating * self.count_of_ratings
        self.average_rating =\
            round(((average + tax) / (self.count_of_ratings + 1)), 1)
        self.count_of_ratings += 1

    def __str__(self) -> str:
        return f"Distance from center - {self.distance_from_city_center}, " \
               f"clean power - {self.clean_power}, " \
               f"average rating - {self.average_rating}," \
               f" count of ratings - {self.count_of_ratings}"
