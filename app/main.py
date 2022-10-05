class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str):
        self.comfort_class = comfort_class
        self. clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        washing_price = (car.comfort_class
                         * (self.clean_power - car.clean_mark)
                         * self.average_rating
                         / self.distance_from_city_center)
        return round(washing_price, 1) if washing_price > 0 else 0

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate):
        self.average_rating = round((self.count_of_ratings
                                     * self.average_rating
                                     + rate)
                                    / (self.count_of_ratings + 1),
                                    1)
        self.count_of_ratings += 1

    def serve_cars(self, cars):
        income = 0
        for car in cars:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return income
