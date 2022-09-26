class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center,
                 clean_power, average_rating, count_of_ratings):
        self.distance = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car):
        if self.clean_power >= car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars):
        income = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car):
        dif = self.clean_power - car.clean_mark
        washing_price = (
            car.comfort_class * dif * self.average_rating / self.distance)
        return round(washing_price, 1)

    def rate_service(self, rate):
        mul = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = (
            round((mul + rate) / self.count_of_ratings, 1)
        )
