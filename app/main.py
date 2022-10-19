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

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        distance = self.distance_from_city_center
        cleaning = (self.clean_power - car.clean_mark)
        price = round(
            car.comfort_class * cleaning * self.average_rating / distance,
            1
        )
        return price

    def wash_single_car(self, car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, n: int) -> None:
        rating = self.average_rating
        count = self.count_of_ratings
        self.average_rating = round((rating * count + n) / (count + 1), 1)
        self.count_of_ratings += 1
