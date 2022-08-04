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
            count_of_ratings):

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars):
        income = 0
        for car in list_of_cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car):
        # difference of car's power and car's clean mark
        difference = self.clean_power - car.clean_mark
        # multiplication of car's comfort class, difference of car's power,
        # car's clean mark and average rating
        numerator = car.comfort_class * difference * self.average_rating
        income = round(numerator / self.distance_from_city_center, 1)
        return income

    def wash_single_car(self, car):
        car.clean_mark = self.clean_power

    def rate_service(self, rate: float):
        old_count_of_ratings = self.count_of_ratings
        self.count_of_ratings += 1
        # multiplication of old average rating, old count of ratings
        # plus current rate
        numerator = (self.average_rating * old_count_of_ratings) + rate
        self.average_rating = round(numerator / self.count_of_ratings, 1)
