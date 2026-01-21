class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
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

    def serve_cars(self, cars):
        income = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car):
        clean_rate = self.clean_power - car.clean_mark
        wash_price = car.comfort_class * clean_rate * \
                     self.average_rating / self.distance_from_city_center
        return round(wash_price, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, number):
        total_rate = self.count_of_ratings
        part_1 = total_rate / (total_rate + 1) * self.average_rating
        part_2 = 1 / (total_rate + 1) * number
        self.average_rating = round(part_1 + part_2, 1)
        self.count_of_ratings += 1
