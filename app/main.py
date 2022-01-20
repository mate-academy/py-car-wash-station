class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: int,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list):
        income = 0
        for one_car in list_of_cars:
            income += self.calculate_washing_price(one_car)
            self.wash_single_car(one_car)
        return income

    def calculate_washing_price(self, car: Car):
        if car.clean_mark < self.clean_power:
            price = car.comfort_class \
                     * (self.clean_power - car.clean_mark) \
                     * self.average_rating / self.distance_from_city_center
            return round(price, 2)
        else:
            return 0

    def wash_single_car(self, single_car: Car) -> None:
        if single_car.clean_mark < self.clean_power:
            single_car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        new_rating = (self.average_rating * self.count_of_ratings) + rate
        new_average_rating = new_rating / (self.count_of_ratings + 1)
        self.average_rating = round(new_average_rating, 1)
        self.count_of_ratings += 1
