class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
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
        cash = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                cash += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(cash, 1)

    def calculate_washing_price(self, other):
        price = other.comfort_class * (self.clean_power - other.clean_mark) * \
            (self.average_rating / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, other):
        if self.clean_power > other.clean_mark:
            other.clean_mark = self.clean_power

    def rate_service(self, grade):
        sum_grade = self.average_rating * self.count_of_ratings + grade
        self.count_of_ratings += 1
        self.average_rating = round(sum_grade / self.count_of_ratings, 1)
