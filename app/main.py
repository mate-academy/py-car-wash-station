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
        difference = self.clean_power - car.clean_mark
        cost_of_single_wash = car.comfort_class * difference * \
            self.average_rating / self.distance_from_city_center

        cost_of_single_wash = round(cost_of_single_wash, 1)

        return cost_of_single_wash

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rate):
        amount = self.count_of_ratings
        first_part = amount / (amount + 1) * self.average_rating
        second_part = 1 / (amount + 1) * new_rate

        self.average_rating = round(first_part + second_part, 1)
        self.count_of_ratings += 1
