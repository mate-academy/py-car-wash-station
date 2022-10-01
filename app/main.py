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
            count_of_ratings,
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars):
        income = 0
        for car in list_of_cars:
            if self.calculate_washing_price(car) > 0:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car):
        to_wash = self.clean_power - car.clean_mark
        cost = car.comfort_class * to_wash * self.average_rating
        return round(
            cost / self.distance_from_city_center, 1
        )

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark):
        sum_of_marks = self.average_rating * self.count_of_ratings + mark
        self.count_of_ratings += 1
        self.average_rating = round(sum_of_marks / self.count_of_ratings, 1)
