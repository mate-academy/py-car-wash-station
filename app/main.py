class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
        self.clean_before = clean_mark


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:

        return round(
            sum(self.calculate_washing_price(single_car)
                for single_car in cars
                if self.wash_single_car(single_car)), 1
        )

    def calculate_washing_price(self, single_car: Car) -> float:
        return (
                single_car.comfort_class * (self.clean_power -
                single_car.clean_before) * self.average_rating /
                self.distance_from_city_center
        )

    def wash_single_car(self, single_car: Car) -> bool:
        if self.clean_power > single_car.clean_mark:
            single_car.clean_mark = self.clean_power
            return True

    def rate_service(self, rate: int):
        self.average_rating = round(
            (self.average_rating
             * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1)
            , 1
        )
        self.count_of_ratings += 1


