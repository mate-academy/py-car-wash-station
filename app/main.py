class Car:
    def __init__(self,
                 comfort_class=int,
                 clean_mark=int,
                 brand=str
                 ):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center=float,
                 clean_power=int,
                 average_rating=float,
                 count_of_ratings=int
                 ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars=list) -> float:
        income = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car):
        clean_requirement = self.clean_power - car.clean_mark
        rating_ratio = self.average_rating / self.distance_from_city_center
        total_price = clean_requirement * car.comfort_class * rating_ratio
        return round(total_price, 1)

    def rate_service(self, new_rate=int):
        all_ratings = self.average_rating * self.count_of_ratings + new_rate
        self.count_of_ratings += 1
        updated_rating = round((all_ratings / self.count_of_ratings), 1)
        self.average_rating = updated_rating
