class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center : float, clean_power: int, average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car : list[Car]) -> float:
        income = 0
        for car_class in car:
            if car_class.clean_mark > self.clean_power:
                continue
            income += self.calculate_washing_price(car_class) # no formula in README so asking GPT
            self.wash_single_car(car_class)
        return round(income, 1)

    def calculate_washing_price(self, car : Car) -> float:
        washing_price = (car.comfort_class * (self.clean_power - car.clean_mark)
                         * self.average_rating / self.distance_from_city_center)
        return round(washing_price, 1)

    def wash_single_car(self, car : Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power #we don't return result, just apply data inside class method,                                     # so maybe will need to rewrite this method after

    def rate_service(self, client_rating : float) -> None:
        self.count_of_ratings += 1
        self.average_rating = (self.average_rating * (self.count_of_ratings - 1) + client_rating) / self.count_of_ratings
        self.average_rating = round(self.average_rating,1)
