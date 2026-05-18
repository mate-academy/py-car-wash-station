class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        if self.distance_from_city_center <= 0:
            return 0.0
        price = (car.comfort_class
                 * (self.clean_power
                    - car.clean_mark)
                 * self.average_rating
                 / self.distance_from_city_center)
        return round(price, 1)

    def serve_cars(self, cars: list[Car]) -> float:
        total_price = 0.0
        for car in cars:
            total_price += self.wash_single_car(car)
        return total_price

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            price_for_one_car = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price_for_one_car
        return 0.0

    def rate_service(self, rate: float) -> float:
        new_average_rating = ((self.average_rating
                               * self.count_of_ratings
                               + rate)
                              / (self.count_of_ratings + 1))
        self.average_rating = round(new_average_rating, 1)
        self.count_of_ratings += 1
        return self.average_rating
