class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.wash_single_car(car)
                car.clean_mark = self.clean_power
                income += price
        return round(income, 1)

    def calculate_washing_price(self, car: Car):
        if self.clean_power <= car.clean_mark:
            return 0.0
        diff = self.clean_power - car.clean_mark 
        price = car.comfort_class * diff * self.average_rating / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
        return price
    
    def rate_service(self, rating: int):
        new_count = self.count_of_ratings + 1
        new_average = (self.average_rating * self.count_of_ratings + rating) / new_count
        self.count_of_ratings = new_count
        self.average_rating = round(new_average, 1)
