class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str) -> None:

        if not 1 <= comfort_class <= 7:
            raise ValueError()

        if not 1 <= clean_mark <= 10:
            raise ValueError()

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: float,
            average_rating: float,
            count_of_ratings: int) -> None:

        if not 1.0 <= distance_from_city_center <= 10.0:
            raise ValueError()

        if not 1.0 <= average_rating <= 5.0:
            raise ValueError()

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        total = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                total += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(total, 1)

    def calculate_washing_price(self, car: Car) -> float:
        difference = self.clean_power - car.clean_mark

        return round(
            car.comfort_class
            * difference
            * self.average_rating / self.distance_from_city_center,
            1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:

        if not 1.0 <= rate <= 5.0:
            raise ValueError()

        new_total_skore = self.average_rating * self.count_of_ratings + rate

        self.average_rating = round(
            new_total_skore
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
