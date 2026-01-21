class Car:
    def __init__(
            self,
            comfort_class: int = 1,
            clean_mark: int = 1,
            brand: str = None
    ) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float = 1.0,
        clean_power: int = 1,
        average_rating: float = 1.0,
        count_of_ratings: int = None
    ) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:

        return sum(
            self.wash_single_car(car)
            for car in cars
        )

    def calculate_washing_price(self, car: Car) -> float:
        clear = float(self.clean_power - car.clean_mark)
        price = (
            float(car.comfort_class)
            * clear
            * self.average_rating
            / self.distance_from_city_center
        )

        return round(price, 1)

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price

        return 0

    def rate_service(self, rate: float) -> None:
        summ_rates = self.average_rating * float(self.count_of_ratings) + rate
        new_avr_rate = summ_rates / float(self.count_of_ratings + 1)

        self.average_rating = round(new_avr_rate, 1)
        self.count_of_ratings += 1
