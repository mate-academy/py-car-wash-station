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

    def calculate_washing_price(self, car: Car) -> float:
        price = 0.0
        if car.clean_mark < self.clean_power:
            clean_pos = self.clean_power - car.clean_mark
            formula_up = car.comfort_class * clean_pos * self.average_rating
            price += formula_up / self.distance_from_city_center
        return round(price, 1)

    def serve_cars(self, cars: list) -> float:
        revenue = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                clean_pos = self.clean_power - car.clean_mark
                form_up = car.comfort_class * clean_pos * self.average_rating
                revenue += form_up / self.distance_from_city_center
                self.wash_single_car(car)
        return round(revenue, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        form_up = self.average_rating * self.count_of_ratings + rate
        self.average_rating = round(form_up / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
