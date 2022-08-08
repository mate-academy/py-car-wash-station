class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center: float,
                 clean_power: int,
                 rate: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = rate
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car):
        part_price = car.comfort_class * car.clean_mark * self.average_rating
        price = part_price / self.distance_from_city_center
        return round(price, 1)

    def serve_cars(self, list_of_cars: list) -> object:
        lst = [car for car in list_of_cars
               if car.clean_mark < self.clean_power]
        total = 0
        for car in lst:
            if self.clean_power > car.clean_mark:
                car.clean_mark = self.clean_power - car.clean_mark
                total += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark):
        val_marks = self.average_rating * self.count_of_ratings + mark
        self.average_rating = round(val_marks / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
