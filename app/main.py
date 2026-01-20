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

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if self.wash_single_car(car):
                wash_price = self.calculate_washing_price(car)
                income += wash_price
                car.clean_mark = self.clean_power
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        wash_price = (car.comfort_class * (self.clean_power - car.clean_mark)
                      * self.average_rating / self.distance_from_city_center)
        return round(wash_price, 1)

    def wash_single_car(self, car: Car) -> bool:
        return True if self.clean_power > car.clean_mark else False

    def rate_service(self, rate: int) -> None:
        new_count_of_ratings = self.count_of_ratings + 1
        temp_avg_rating = self.average_rating * self.count_of_ratings + rate
        self.average_rating = round(temp_avg_rating / new_count_of_ratings, 1)
        self.count_of_ratings = new_count_of_ratings
