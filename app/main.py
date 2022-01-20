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
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_cars):
        income_per_cars = 0

        for i in list_cars:
            if i.clean_mark < self.clean_power:
                income_per_cars += self.calculate_washing_price(i)
                self.wash_single_car(i)

        return round(income_per_cars, 1)

    def calculate_washing_price(self, car):
        difference_between_cars = self.clean_power - car.clean_mark
        comfort_minus_difference = car.comfort_class * difference_between_cars
        price_per_car = comfort_minus_difference * self.average_rating

        return round(price_per_car / self.distance_from_city_center, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        return car

    def rate_service(self, rate):
        self.count_of_ratings += 1
        full_rate = self.average_rating * (self.count_of_ratings - 1)
        temp_average_rating = full_rate + rate

        self.average_rating = round(
            temp_average_rating / self.count_of_ratings, 1
        )
