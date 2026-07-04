class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        if (comfort_class < 1
                or comfort_class > 7
                or clean_mark < 1
                or clean_mark > 10):
            raise ValueError("Provided value is invalid")
        self.clean_mark = clean_mark
        self.comfort_class = comfort_class
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        if (distance_from_city_center < 1
                or distance_from_city_center > 10
                or average_rating < 1
                or average_rating > 5):
            raise ValueError("Provided value is invalid")
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        res = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                res += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(res, 1)

    def wash_single_car(self, car: Car) -> Car:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
        return car

    def calculate_washing_price(self, car: Car) -> float:
        income = (car.comfort_class * (self.clean_power - car.clean_mark)
                  * self.average_rating
                  / self.distance_from_city_center)
        return round(income, 1)

    def rate_service(self, rate: int) -> None:
        total = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(total / self.count_of_ratings, 1)
