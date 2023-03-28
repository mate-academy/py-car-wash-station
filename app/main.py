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
            count_of_ratings: float
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        total_price = 0
        if len(cars) == 1:
            if self.clean_power > cars[0].clean_mark:
                total_price = self.wash_single_car(cars[0])
        else:
            for car in cars:
                if self.clean_power > car.clean_mark:
                    total_price += self.calculate_washing_price(car)
                    car.clean_mark = self.clean_power
        if float(total_price) > 0:
            return round(total_price, 1)
        return total_price

    def calculate_washing_price(self, model: Car) -> float:
        price = model.comfort_class * (self.clean_power - model.clean_mark)\
            * self.average_rating / self.distance_from_city_center
        return price

    def wash_single_car(self, car: Car) -> float or None:
        price_one_car = self.calculate_washing_price(car)
        car.clean_mark = self.clean_power
        return price_one_car

    def rate_service(self, rate: int) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1), 1
        )
        self.count_of_ratings += 1
