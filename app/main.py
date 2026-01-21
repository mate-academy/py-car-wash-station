class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> any:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self, distance_from_city_center: int, clean_power: int,
            average_rating: int, count_of_ratings: int
    ) -> any:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, lst_of_cars: list) -> any:
        income = 0
        for car in lst_of_cars:
            price = self.calculate_washing_price(car)
            income += price
            self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: object) -> any:
        if self.clean_power < car.clean_mark:
            return 0
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: object) -> any:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> any:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1),
            1,
        )
        self.count_of_ratings += 1
