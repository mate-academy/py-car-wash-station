class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self, distance_from_city_center, clean_power,
        average_rating, count_of_ratings
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                income += price
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car):
        car_wash_cost = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center
        )
        return round(car_wash_cost, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rating):
        new_average_rating = (
            self.average_rating * self.count_of_ratings
            + new_rating) / (self.count_of_ratings + 1)
        new_average_rating = round(new_average_rating, 1)
        self.average_rating = new_average_rating
        self.count_of_ratings += 1
        return new_average_rating
