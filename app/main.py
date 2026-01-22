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
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        summary = 0.0
        for car in cars:
            summary += self.wash_single_car(car)
        return summary

    def calculate_washing_price(self, car: Car) -> float:
        clean_delta = self.clean_power - car.clean_mark
        basic_price = car.comfort_class * clean_delta * self.average_rating
        return round((basic_price / self.distance_from_city_center), 1)

    def wash_single_car(self, car: Car) -> float:
        if self.clean_power > car.clean_mark:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price
        return 0.0

    def rate_service(self, mark: int) -> None:
        unpacked_rating = self.average_rating * self.count_of_ratings
        updated_rating = unpacked_rating + mark
        self.count_of_ratings += 1
        self.average_rating = round(
            (updated_rating / self.count_of_ratings),
            1
        )
