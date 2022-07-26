class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars):
        income = 0
        for car in list_of_cars:
            if self.clean_power > car.clean_mark:
                income += round(self.calculate_washing_price(car), 1)
                car.clean_mark = self.clean_power
        return income

    def calculate_washing_price(self, car):
        # cost1 - calculates first part of the total cost
        cost1 = car.comfort_class * (self.clean_power - car.clean_mark)
        # cost - calculates the total price of washing
        cost = cost1 * (self.average_rating / self.distance_from_city_center)
        return round(cost, 1)

    def rate_service(self, rating):
        # average1 calculates first part of the rate_service
        average1 = self.average_rating * self.count_of_ratings + rating
        # self.average_rating - calculates total rate_service
        self.average_rating = round(average1 / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

    def wash_single_car(self, car):
        if self.clean_power >= car.clean_mark:
            self.clean_power = car.clean_mark
        return self.clean_power
