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
                 distance_from_city_centre: int,
                 clean_power: int,
                 average_rating: int,
                 count_of_ratings: int) -> None:
        self.distance_from_city_centre = distance_from_city_centre
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, cars: Car | list) -> float:
        if not isinstance(cars, list):
            cars = [cars]
        cost = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                cost += (
                    car.comfort_class
                    * (self.clean_power - car.clean_mark)
                    * (self.average_rating / self.distance_from_city_centre)
                )
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> Car:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
        return car

    def rate_service(self, rate: int) -> None:
        total_rate = self.count_of_ratings * self.average_rating
        self.count_of_ratings += 1
        self.average_rating = round((total_rate + rate)
                                    / self.count_of_ratings, 1)

    def serve_cars(self, cars: list) -> float:
        final_price = 0
        final_price += self.calculate_washing_price(cars)
        for car in cars:
            self.wash_single_car(car)
        return round(final_price, 1)
