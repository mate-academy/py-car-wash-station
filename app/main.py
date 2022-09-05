class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power,
        average_rating: float,
        count_of_ratings: int,
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list[Car]):
        total_income = 0
        for car in list_of_cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return total_income

    def calculate_washing_price(self, car: Car):
        washing_price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(washing_price, 1)

    def wash_single_car(self, car: Car):
        car.clean_mark = self.clean_power

    def rate_service(self, rate: float):
        self.count_of_ratings += 1
        new_rating = (
            self.average_rating * (self.count_of_ratings - 1) + rate
        ) / self.count_of_ratings
        self.average_rating = round(new_rating, 1)


# bmw = Car(3, 3, "BMW")
# audi = Car(4, 9, "Audi")
# mercedes = Car(7, 1, "Mercedes")
#
# ws = CarWashStation(6, 8, 3.9, 11)
#
# income = ws.serve_cars([bmw, audi, mercedes])
#
# print(income)
#
# ws.rate_service(5)
#
# print(ws.average_rating)
