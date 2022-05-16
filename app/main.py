class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self, distance_from_city_center,
            clean_power, average_rating,
            count_of_ratings
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        start_calc = self.clean_power - car.clean_mark
        midl_calc = car.comfort_class * start_calc * self.average_rating
        final_calc = midl_calc / self.distance_from_city_center
        return round(final_calc, 1)

    def serve_cars(self, cars: list):
        price = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return price

    def wash_single_car(self, car):
        car.clean_mark = self.clean_power

    def rate_service(self, rate):
        rates = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(rates / self.count_of_ratings, 1)
