class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        money_list = []
        for car in cars:
            if car.clean_mark <= self.clean_power:
                money_list.append(
                    CarWashStation.calculate_washing_price(self, car=car))
                CarWashStation.wash_single_car(self, car=car)
        return round(sum(money_list), 1)

    def calculate_washing_price(self, car: str) -> float:
        income = (car.comfort_class * (self.clean_power - car.clean_mark)
                  * self.average_rating) / self.distance_from_city_center
        return income

    def wash_single_car(self, car: str) -> float:
        car.clean_mark = self.clean_power
        return car.clean_mark

    def rate_service(self, rate: int) -> float:
        new_rating = ((self.average_rating * self.count_of_ratings)
                      + rate) / (self.count_of_ratings + 1)
        self.count_of_ratings += 1
        self.average_rating = round(new_rating, 1)
        return self.average_rating
