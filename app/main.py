class Car:
    def __init__(self,
                 comfort_class,
                 clean_mark, brand):

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center,
                 clean_power,
                 average_rating,
                 count_of_ratings):

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, Car):
        return round(
            Car.comfort_class * (self.clean_power - Car.
                                 clean_mark) * (self.average_rating / self.
                                                distance_from_city_center), 1)

    def serve_cars(self, income: list):
        result = 0
        for i in income:
            if i.clean_mark < self.clean_power:
                result += self.calculate_washing_price(i)
                self.wash_single_car(i)
        return result

    def rate_service(self, mark):
        self.average_rating = round(
            ((self.average_rating * self.
              count_of_ratings) + mark) / (self.count_of_ratings + 1),
            1)
        self.count_of_ratings += 1
        return self.average_rating, self.count_of_ratings

    def wash_single_car(self, Car):
        if Car.clean_mark <= self.clean_power:
            Car.clean_mark = self.clean_power
        return Car.clean_mark
