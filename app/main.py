class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center,
                 clean_power, average_rating,
                 count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car):
        comf_clss = car.comfort_class
        cln_pwr = self.clean_power
        cln_mrk = car.clean_mark
        average = self.average_rating
        distance = self.distance_from_city_center
        return round(comf_clss * (cln_pwr - cln_mrk) * (average / distance), 1)

    def wash_single_car(self, car):
        if self.clean_power >= car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate):
        # average = self.average_rating
        ratings = self.count_of_ratings
        self.average_rating = round(
            (self.average_rating * ratings + rate) / (ratings + 1), 1)
        self.count_of_ratings += 1
