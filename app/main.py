class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: float,
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

    def calculate_washing_price(self, car: Car) -> float:
        price_washing = 0
        work_done = self.clean_power - car.clean_mark
        price_comfort = work_done * car.comfort_class
        plus_price = price_comfort * self.average_rating
        bonus_price = plus_price / self.distance_from_city_center
        price_washing = round(bonus_price, 1)
        return price_washing

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> float:
        checkout = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                checkout += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(checkout, 1)

    def rate_service(self, rate: float) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += rate
        self.count_of_ratings += 1
        self.average_rating = total_rating / self.count_of_ratings
        self.average_rating = round(self.average_rating, 1)
