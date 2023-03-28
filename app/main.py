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
                 clean_power: int,
                 average_rating: float,
                 count_of_rating: int) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_rating

    def wash_single_car(self, car: Car) -> float:
        price = self.calculate_washing_price(car)
        car.clean_mark = self.clean_power
        return price

    def serve_cars(self, cars: list) -> float:
        return sum([self.wash_single_car(car) for car in cars
                    if car.clean_mark < self.clean_power])

    def calculate_washing_price(self, car: Car) -> float:
        ls = (car.comfort_class
              * (self.clean_power
                 - car.clean_mark)
              * self.average_rating
              / self.distance_from_city_center)

        return round(ls, 1)

    def rate_service(self, single_rating: int) -> None:
        self.average_rating = round((single_rating
                                     + self.average_rating
                                     * self.count_of_ratings)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
