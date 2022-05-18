class Car:
    def __init__(
            self,
            comfort_class,
            clean_mark,
            brand
    ):
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
        for washing_car in cars:
            if self.clean_power > washing_car.clean_mark:
                income += self.calculate_washing_price(washing_car)
                self.wash_single_car(washing_car)
        return round(income, 1)

    def calculate_washing_price(self, car):
        clean_rate = self.clean_power - car.clean_mark
        cost_for_wash = car.comfort_class * clean_rate * \
            self.average_rating / self.distance_from_city_center
        return round(cost_for_wash, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rate):
        total_rate = self.average_rating * self.count_of_ratings + new_rate
        self.count_of_ratings += 1
        self.average_rating = round(total_rate / self.count_of_ratings, 1)
