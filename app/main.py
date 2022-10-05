class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: float,
                 average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_cars: list) -> int:

        wash_price = 0
        for car in list_cars:
            if car.clean_mark <= self.clean_power:
                wash_price += self.calculate_washing_price(car)
                self.wash_single_car(car)
                car.clean_mark = self.clean_power
        return wash_price

    def calculate_washing_price(self, car) -> int:

        return round(car.comfort_class
                     * (self.clean_power - car.clean_mark)
                     * (self.average_rating
                        / self.distance_from_city_center), 1)

    def wash_single_car(self, car) -> None:

        return car.clean_mark <= self.clean_power

    def rate_service(self, rating: float) -> None:

        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings + rating)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
