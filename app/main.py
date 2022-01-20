class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ):

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ):

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list):
        amount = 0

        for car in list_of_cars:
            if car.clean_mark < self.clean_power:
                amount += (self.calculate_washing_price(car))
                self.wash_single_car(car)

        return amount

    def calculate_washing_price(self, car):
        difference = self.clean_power - car.clean_mark
        division = self.average_rating / self.distance_from_city_center
        return round(car.comfort_class * difference * division, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark):
        new_average = self.average_rating * self.count_of_ratings + mark
        self.count_of_ratings += 1
        self.average_rating = round(new_average / self.count_of_ratings, 1)
