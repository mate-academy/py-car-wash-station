class Car:
    def __init__(self, comfort_class: str, clean_mark: str, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
    def serve_cars(self, cars: list[Car]):
        total_cost = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.clean_power - car.clean_mark
                total_cost += price
                car.clean_mark = self.clean_power  
     def calculate_washing_price(self, price_of_washing):
         self.price_of_washing = price_of_washing
         price_of_washing = car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center
         return price_of_washing
     def wash_single_car(self, car: Car):
        car.clean_mark = self.clean_power
        min_value = 1
        max_value = 10
        min_value<=clean_mark<max_value
        return clean_mark
    def rate_service(self, rating: int):
        self.average_rating = (self.average_rating * self.count_of_ratings + new_rating) / (self.count_of_ratings + 1)
        self.count_of_ratings += 1
