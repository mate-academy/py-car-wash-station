class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str

                 ) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int

                 ) -> None:

        self.distance = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self,
                        car: Car

                        ) -> None:

        car.clean_mark = self.clean_power

    def calculate_washing_price(self,
                                car: Car
                                ) -> float:

        first_operation = (car.comfort_class
                           * (self.clean_power - car.clean_mark))
        second_operation = (first_operation
                            * (self.average_rating / self.distance))
        washing_price = round(second_operation, 1)

        return washing_price

    def rate_service(self,
                     rating: int
                     ) -> None:

        if 1.0 <= rating <= 5.0:
            self.average_rating *= self.count_of_ratings
            self.average_rating += rating
            self.count_of_ratings += 1
            self.average_rating = (round(self.average_rating
                                         / self.count_of_ratings, 1))

    def serve_cars(self,
                   cars: list[Car]
                   ) -> float:

        total = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                self.wash_single_car(car)

                total += price

        return round(total, 1)
