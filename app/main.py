class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self. brand = brand

class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int):
       self.distance_from_city_center = distance_from_city_center
       self.clean_power = clean_power
       self.average_rating = average_rating
       self.count_of_ratings =count_of_ratings

       def serve_cars(self, cars):

           pass

       def calculate_washing_price(self, car):
           if self.clean_power > car.clean_mark:
               cost = car.comfort_class * (self.clean_power - car.clean_mark) * (
                               self.average_rating / self.distance_from_city_center)
               return round(cost, 1)
            else:
               return 0.0

       def wash_single_car(self, car):
           pass

       def rate_service(self, new_rating):
           pass