class Car:
    # write your code here
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    # write your code here
    def __init__(
            self,
            distance_from_city_center, clean_power,
            average_rating, count_of_ratings
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        income = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income, 1)

    def calculate_washing_price(self, car):
        washing_volume = self.clean_power - car.clean_mark
        rating_with_dist = self.average_rating / self.distance_from_city_center
        washing_price = car.comfort_class * washing_volume * rating_with_dist

        return round(washing_price, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark):
        all_marks = self.count_of_ratings * self.average_rating

        all_marks += mark
        self.count_of_ratings += 1
        self.average_rating = round(all_marks / self.count_of_ratings, 1)

        return self.average_rating, self.count_of_ratings
