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
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        clean_difference = self.clean_power - car.clean_mark
        mul_coeff = car.comfort_class * clean_difference * self.average_rating
        return round(mul_coeff / self.distance_from_city_center, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, list_of_cars):
        income = []
        for car in list_of_cars:
            if car.clean_mark < self.clean_power:
                income.append(self.calculate_washing_price(car))
            self.wash_single_car(car)
        return sum(income)

    def rate_service(self, rate):
        new_rating = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(new_rating / self.count_of_ratings, 1)
