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
            distance_from_city_center: (int, float),
            clean_power: int,
            average_rating: (int, float),
            count_of_ratings: int
    ) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return income

    def calculate_washing_price(self, car: Car) -> float:
        car_class = car.comfort_class
        cleaning_difference = self.clean_power - car.clean_mark
        wash_rate = self.average_rating
        distance = self.distance_from_city_center

        price = car_class * cleaning_difference * wash_rate / distance

        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        total_rate = self.average_rating * self.count_of_ratings + rate
        new_count = self.count_of_ratings + 1
        new_average_rating = round(total_rate / new_count, 1)

        self.average_rating = new_average_rating
        self.count_of_ratings += 1
