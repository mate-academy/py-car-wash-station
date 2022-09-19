class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        cost = 0
        # calculate total cost of washing all cars
        for car in cars:
            if self.clean_power > car.clean_mark:
                cost += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(cost, 1)

    def calculate_washing_price(self, car):
        # calculate cost of washing single car in 2 steps
        cost = car.comfort_class * (self.clean_power - car.clean_mark)
        cost *= self.average_rating / self.distance_from_city_center
        return round(cost, 1)

    def wash_single_car(self, car):
        # equals clean_mark of current washed car to washing station's clean_power
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate):
        # calculate new average rating after adding new mark
        self.average_rating =\
            round((rate + self.average_rating * self.count_of_ratings)
                  / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
