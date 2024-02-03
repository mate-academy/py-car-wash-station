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
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list) -> float:
        money = []
        for car in car_list:
            if car.clean_mark < self.clean_power:
                cash = self.calculate_washing_price(car)
                money.append(cash)
                self.wash_single_car(car)
        return round(sum(money), 1)

    def calculate_washing_price(self, car: Car) -> float:
        result = round(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center,
            1
        )
        return result

    def wash_single_car(self,
                        car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        self.count_of_ratings += 1
        new_rating = (
                             (self.average_rating * (self.count_of_ratings - 1))
                      + rating) / self.count_of_ratings
        self.average_rating = round(new_rating, 1)
