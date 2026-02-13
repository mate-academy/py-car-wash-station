class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings


    def calculate_washing_price(self, car):
        diff = self.clean_power - car.clean_mark
        if diff <= 0:
            return  0.0
        price = car.comfort_class * diff * self.average_rating / self.distance_from_city_center
        return round(price, 1)


    def serve_cars(self, cars_list):
        total_income = 0.0

        for car in cars_list:
            price = self.calculate_washing_price(car)
            if price > 0.0:
                self.wash_single_car(car)
                total_income += price
        return round(total_income, 1)


    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power


    def rate_service(self, new_rate):
        new_avg = (self.average_rating * self.count_of_ratings + new_rate) / (self.count_of_ratings + 1)
        self.count_of_ratings += 1
        self.average_rating = round(new_avg, 1)