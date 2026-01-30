class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        result_price = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                result_price += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(result_price, 1)

    def wash_single_car(self, car: object) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: object) -> float:
        difference = self.clean_power - car.clean_mark
        dist = self.distance_from_city_center
        result = car.comfort_class * difference * self.average_rating / dist
        return round(result, 1)

    def rate_service(self, mark: int) -> None:
        count = self.count_of_ratings
        rate = self.average_rating
        self.count_of_ratings += 1
        self.average_rating = round((rate * count + mark) / (count + 1), 1)
