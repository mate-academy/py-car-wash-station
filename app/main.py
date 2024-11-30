class Car:

    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(
            self,
            distance_from_city_center,
            clean_power,
            average_rating,
            count_of_ratings
    ):
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
        return income

    def calculate_washing_price(self, car):
        clean_rate = self.clean_power - car.clean_mark
        branch_rate = self.average_rating / self.distance_from_city_center
        washing_price = car.comfort_class * clean_rate * branch_rate

        return round(washing_price, 1)

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate_mark):
        total_of_marks = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        new_rate = (total_of_marks + rate_mark) / self.count_of_ratings
        self.average_rating = round(new_rate, 1)
