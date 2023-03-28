class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: int,
                 count_of_ratings: int) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        wash_sub_rate = self.average_rating / self.distance_from_city_center
        clean_cof = self.clean_power - car.clean_mark
        calculate_price = car.comfort_class * clean_cof * wash_sub_rate

        return round(calculate_price, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:

        rating = ((self.average_rating * self.count_of_ratings) + rate) /\
                 (self.count_of_ratings + 1)

        self.average_rating = round(rating, 1)
        self.count_of_ratings += 1

    def serve_cars(self, cars: list) -> int:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return income
