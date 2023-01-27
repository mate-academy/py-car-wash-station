class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_mark: int,
                 average_rating: float,
                 count_of_ratings: int
                 ):
        self.distance = distance_from_city_center
        self.clean_power = clean_mark
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        res = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                res += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return res

    def calculate_washing_price(self, car):
        clean_diff = self.clean_power - car.clean_mark
        car_wash_index = self.average_rating / self.distance
        price = round(
            car.comfort_class * clean_diff * car_wash_index,
            1)
        return price

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate):
        overall_rating = ((self.average_rating * self.count_of_ratings) + rate)
        self.average_rating = round(
            overall_rating / (self.count_of_ratings + 1),
            1)
        self.count_of_ratings += 1
