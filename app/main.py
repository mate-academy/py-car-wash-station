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
        wash_station_income = 0

        for car in cars:
            wash_station_income += self.wash_single_car(car)

        return round(wash_station_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        result = (car.comfort_class * (self.clean_power - car.clean_mark)
                  * self.average_rating / self.distance_from_city_center)
        return round(result, 1)

    def wash_single_car(self, car: Car) -> float:
        income_of_car = 0

        if car.clean_mark < self.clean_power:
            income_of_car = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power

        return income_of_car

    def rate_service(self, rate: int) -> None:
        total_rate = self.count_of_ratings * self.average_rating

        self.count_of_ratings += 1
        self.average_rating = round(
            (total_rate + rate) / self.count_of_ratings, 1
        )
