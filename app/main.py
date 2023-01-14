class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_list: list) -> float:
        ability_wash = [
            i for i in cars_list if self.clean_power > i.clean_mark
        ]
        prices = [self.calculate_washing_price(cleaning)
                  for cleaning in ability_wash]
        for x_car in ability_wash:
            self.wash_single_car(x_car)
        return sum(prices)

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center, 1
        )

    def wash_single_car(self, other: Car) -> None:
        other.clean_mark = self.clean_power

    def rate_service(self, number: int) -> None:
        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings + number
                                     ) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
