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

    def serve_cars(self, car_arr: list):
        cash = []
        for car in car_arr:
            cash.append(self.wash_single_car(car))
        return sum(cash)    # earned money for few cars

    def calculate_washing_price(self, car: Car):
        price = round(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center, 1)
        return price        # price for washing car

    def wash_single_car(self, car: Car):
        if car.clean_mark < self.clean_power:
            profit = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return profit    # money we earned for wash, car become clean as station power
        return 0             # car too clean for our station

    def rate_service(self, rate: int):
        new_rate = round(
            (self.average_rating * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
        self.average_rating = new_rate
