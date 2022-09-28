class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car):
        car.clean_mark = self.clean_power

    def calculate_washing_price(self, car):
        if car.clean_mark < self.clean_power:
            difference = self.clean_power - car.clean_mark
        elif car.clean_mark == self.clean_power:
            difference = 1
        return round(
            car.comfort_class * difference * self.average_rating
            / self.distance_from_city_center,
            1)

    def serve_cars(self, cars: list):
        price_of_one = self.calculate_washing_price
        wash_of_one = self.wash_single_car
        list_of_admitted_cars = [car for car in cars
                                 if car.clean_mark <= self.clean_power]
        result = sum(list(map(price_of_one, list_of_admitted_cars)))
        for car in list_of_admitted_cars:
            wash_of_one(car)
        return result

    def rate_service(self, rating):
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rating)
            / (self.count_of_ratings + 1),
            1)
        self.count_of_ratings += 1

