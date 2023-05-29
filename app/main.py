class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int):
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

        return income

    def calculate_washing_price(self, car: Car) -> float:
        distance = self.distance_from_city_center
        rating = self.average_rating
        difference = self.clean_power - car.clean_mark
        price = car.comfort_class * difference * rating / distance

        return round(price, 1)

    def wash_single_car(self, car: Car) -> int:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

        return car.clean_mark

    def rate_service(self, rate: float) -> None:
        average_rating = self.average_rating * self.count_of_ratings
        count_of_ratings = self.count_of_ratings + 1

        new_rating = (average_rating + rate) / count_of_ratings

        self.count_of_ratings = count_of_ratings
        self.average_rating = round(new_rating, 1)
