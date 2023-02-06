class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for car in cars:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income, 1)  # pytest

    def calculate_washing_price(self, car: Car) -> float:
        clean_car = self.clean_power - car.clean_mark
        service_level = clean_car * car.comfort_class  # service_level car
        quality_service = service_level * self.average_rating
        price = quality_service / self.distance_from_city_center
        return price

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power >= car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        self.count_of_ratings += 1
        rate_point = ((self.count_of_ratings - 1) * self.average_rating) + rate
        overall_rate = rate_point / self.count_of_ratings
        self.average_rating = round(overall_rate, 1)
