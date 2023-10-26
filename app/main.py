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
        price = sum(self.wash_single_car(car) for car in cars)
        return round(price, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return (car.comfort_class
                * (self.clean_power - car.clean_mark)
                * self.average_rating
                / self.distance_from_city_center)

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return round(price, 1)
        return 0

    def rate_service(self, grade: int) -> None:
        new_grade = ((self.average_rating * self.count_of_ratings + grade)
                     / (self.count_of_ratings + 1))
        self.average_rating = round(new_grade, 1)
        self.count_of_ratings += 1
